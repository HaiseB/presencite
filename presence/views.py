from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .forms import SemainePresenceForm
from .models import Presence, Profile
import datetime
import os
import markdown
from django.contrib.auth import get_user_model
from django.conf import settings

@login_required
def voir_semaine(request):
    today = timezone.now().date()
    lundi = today - datetime.timedelta(days=today.weekday())
    jours = [lundi + datetime.timedelta(days=i) for i in range(5)]
    User = get_user_model()
    users = [u for u in User.objects.all() if hasattr(u, 'profile') and u.profile.visible_in_tableau]
    presences = Presence.objects.filter(date__in=jours)
    tableau = []
    utilisateurs_non_remplis = []

    # Gestion du formulaire de présence pour l'utilisateur connecté
    user = request.user
    user_presences = presences.filter(user=user)
    semaine_verrouillee = user_presences.exists() and all(p.locked for p in user_presences)

    if request.method == 'POST' and not semaine_verrouillee:
        form = SemainePresenceForm(request.POST)
        if form.is_valid():
            for i, jour in enumerate(jours):
                emoji = form.cleaned_data[f'emoji_{i}']
                status = 'present' if emoji in ['✅'] else 'absent'
                presence, created = Presence.objects.get_or_create(user=user, date=jour)
                presence.emoji = emoji
                presence.status = status
                presence.locked = True
                presence.save()
            return redirect('presence:voir_semaine')
    else:
        # Pré-remplir le formulaire si déjà rempli
        initial = {}
        for i, jour in enumerate(jours):
            p = user_presences.filter(date=jour).first()
            if p:
                initial[f'emoji_{i}'] = p.emoji
        form = SemainePresenceForm(initial=initial)

    for user in users:
        ligne = {'user': user, 'jours': []}
        jours_remplis = 0
        for jour in jours:
            p = presences.filter(user=user, date=jour).first()
            if p:
                ligne['jours'].append(p.emoji)
                jours_remplis += 1
            else:
                ligne['jours'].append('')
        if jours_remplis == len(jours):
            tableau.append(ligne)
        else:
            utilisateurs_non_remplis.append(user)

    total_presences_par_jour = []
    for jour in jours:
        total = presences.filter(date=jour, status='present').count()
        total_presences_par_jour.append((jour, total))

    return render(request, 'presence/voir_semaine.html', {
        'form': form,
        'semaine_verrouillee': semaine_verrouillee,
        'tableau': tableau,
        'jours': jours,
        'utilisateurs_non_remplis': utilisateurs_non_remplis,
        'total_presences_par_jour': total_presences_par_jour,
    })

def get_changelog(request):
    """Vue pour récupérer le contenu du changelog en format HTML"""
    try:
        # Chemin vers le fichier changelog.md
        changelog_path = os.path.join(settings.BASE_DIR, 'changelog.md')
        
        # Obtenir la date de dernière modification
        last_modified = os.path.getmtime(changelog_path)
        from datetime import datetime
        last_modified_date = datetime.fromtimestamp(last_modified).strftime('%d/%m/%Y à %H:%M')
        
        # Lire le fichier markdown
        with open(changelog_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Convertir le markdown en HTML
        html_content = markdown.markdown(markdown_content, extensions=['extra', 'codehilite'])
        
        # Remplacer le titre H1 "Changelog" par la date de dernière modification
        import re
        html_content = re.sub(r'<h1>Changelog</h1>', f'<h4 class="text-muted"><i class="fa-solid fa-clock me-2"></i>Dernière mise à jour: {last_modified_date}</h4>', html_content)
        
        return JsonResponse({
            'success': True,
            'content': html_content
        })
    except FileNotFoundError:
        return JsonResponse({
            'success': False,
            'error': 'Fichier changelog.md non trouvé'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erreur lors de la lecture du changelog: {str(e)}'
        })
