from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import SemainePresenceForm
from .models import Presence
import datetime
from django.contrib.auth import get_user_model

@login_required
def remplir_semaine(request):
    user = request.user
    today = timezone.now().date()
    lundi = today - datetime.timedelta(days=today.weekday())
    jours = [lundi + datetime.timedelta(days=i) for i in range(5)]

    # Vérifier si la semaine est déjà verrouillée
    presences = Presence.objects.filter(user=user, date__in=jours)
    if presences.exists() and all(p.locked for p in presences):
        return render(request, 'presence/semaine_verrouillee.html', {'presences': presences, 'jours': jours})

    if request.method == 'POST':
        form = SemainePresenceForm(request.POST)
        if form.is_valid():
            for i, jour in enumerate(jours):
                emoji = form.cleaned_data[f'emoji_{i}']
                status = 'present' if emoji in ['✅', '🏢'] else 'absent'
                presence, created = Presence.objects.get_or_create(user=user, date=jour)
                presence.emoji = emoji
                presence.status = status
                presence.locked = True  # On verrouille la saisie après validation
                presence.save()
            return redirect('presence:remplir_semaine')
    else:
        # Pré-remplir le formulaire si déjà rempli
        initial = {}
        for i, jour in enumerate(jours):
            p = presences.filter(date=jour).first()
            if p:
                initial[f'emoji_{i}'] = p.emoji
        form = SemainePresenceForm(initial=initial)

    return render(request, 'presence/remplir_semaine.html', {'form': form, 'jours': jours})

@login_required
def voir_semaine(request):
    today = timezone.now().date()
    lundi = today - datetime.timedelta(days=today.weekday())
    jours = [lundi + datetime.timedelta(days=i) for i in range(5)]
    User = get_user_model()
    users = User.objects.all()
    presences = Presence.objects.filter(date__in=jours)
    tableau = []
    utilisateurs_non_remplis = []

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
            tableau.append(ligne)  # Ajoute au tableau SEULEMENT si la semaine est complète
        else:
            utilisateurs_non_remplis.append(user)

    return render(request, 'presence/voir_semaine.html', {
        'tableau': tableau,
        'jours': jours,
        'utilisateurs_non_remplis': utilisateurs_non_remplis,
    })
