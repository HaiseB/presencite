from django.db import models
from django.contrib.auth.models import User

class Presence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    STATUS_CHOICES = [
        ('present', 'Présent'),
        ('absent', 'Absent'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    emoji = models.CharField(max_length=2)  # 2 caractères suffisent pour un émoji
    locked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['date']

    def __str__(self):
        return f"{self.user.username} - {self.date} : {self.emoji}"

class MarqueeMessage(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    afficher = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visible_in_tableau = models.BooleanField(default=True)

    def __str__(self):
        return f"Profil de {self.user.username}"
