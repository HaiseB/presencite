from django import forms
from .models import Presence
import datetime

EMOJI_CHOICES = [
    ('✅', 'Présent (✅)'),
    ('🏢', 'Présent (🏢)'),
    ('❌', 'Absent (❌)'),
    ('🎓', 'Absent (🎓)'),
    ('🌴', 'Absent (🌴)'),
    ('👮', 'Absent (👮)'),
]

JOURS_SEMAINE = [
    (0, 'Lundi'),
    (1, 'Mardi'),
    (2, 'Mercredi'),
    (3, 'Jeudi'),
    (4, 'Vendredi'),
]

class SemainePresenceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = datetime.date.today()
        # Trouver le lundi de la semaine en cours
        lundi = today - datetime.timedelta(days=today.weekday())
        for i, nom_jour in JOURS_SEMAINE:
            jour = lundi + datetime.timedelta(days=i)
            self.fields[f'emoji_{i}'] = forms.ChoiceField(
                label=f"{nom_jour} ({jour.strftime('%d/%m')})",
                choices=EMOJI_CHOICES,
                widget=forms.RadioSelect,
                required=True
            )
