from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import MarqueeMessage, Profile, Presence

# Administration personnalisée pour les Présences
@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'emoji_display', 'status', 'locked', 'week_info']
    list_filter = ['status', 'locked', 'date', 'user']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    date_hierarchy = 'date'
    ordering = ['-date', 'user__username']
    list_editable = ['locked']
    readonly_fields = ['emoji_display']

    fieldsets = (
        ('Informations générales', {
            'fields': ('user', 'date', 'status', 'locked')
        }),
        ('Affichage', {
            'fields': ('emoji', 'emoji_display'),
            'description': 'L\'emoji affiché dans le tableau de présences'
        }),
    )
    
    def emoji_display(self, obj):
        """Affiche l'emoji avec une taille plus grande"""
        if obj.emoji:
            return format_html('<span style="font-size: 1.5em;">{}</span>', obj.emoji)
        return '-'
    emoji_display.short_description = 'Emoji'
    
    def week_info(self, obj):
        """Affiche des informations sur la semaine"""
        from datetime import datetime, timedelta
        week_start = obj.date - timedelta(days=obj.date.weekday())
        week_end = week_start + timedelta(days=6)
        return f"Semaine du {week_start.strftime('%d/%m')} au {week_end.strftime('%d/%m')}"
    week_info.short_description = 'Semaine'

# Administration personnalisée pour les Profils
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'visible_in_tableau', 'user_email', 'user_is_staff']
    list_filter = ['visible_in_tableau']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email']
    list_editable = ['visible_in_tableau']
    
    fieldsets = (
        ('Utilisateur', {
            'fields': ('user',)
        }),
        ('Paramètres d\'affichage', {
            'fields': ('visible_in_tableau',),
            'description': 'Contrôle si l\'utilisateur apparaît dans le tableau de présences'
        }),
    )
    
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'
    
    def user_is_staff(self, obj):
        if obj.user.is_staff:
            return mark_safe('<span style="color: green;">✓ Admin</span>')
        return mark_safe('<span style="color: gray;">Utilisateur</span>')
    user_is_staff.short_description = 'Statut'

# Administration personnalisée pour les Messages Marquee
@admin.register(MarqueeMessage)
class MarqueeMessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'afficher', 'created_at', 'message_preview']
    list_filter = ['afficher', 'created_at']
    search_fields = ['message']
    list_editable = ['afficher']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Message', {
            'fields': ('message', 'afficher'),
            'description': 'Message qui s\'affiche dans la barre de défilement en haut de la page'
        }),
        ('Informations', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at']
    
    def message_preview(self, obj):
        """Aperçu du message avec limitation de caractères"""
        if len(obj.message) > 50:
            return obj.message[:50] + '...'
        return obj.message
    message_preview.short_description = 'Aperçu'

# Personnalisation de l'administration des utilisateurs
class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'          # 🔴 IMPORTANT
    can_delete = False
    verbose_name_plural = 'Profil'
    fields = ['visible_in_tableau']
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['is_staff', 'is_active', 'date_joined', 'profile__visible_in_tableau']

# Désinscrire l'admin par défaut et réinscrire avec notre version personnalisée
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Personnalisation de l'interface d'administration
admin.site.site_header = "Administration Presencite"
admin.site.site_title = "Presencite Admin"
admin.site.index_title = "Gestion des présences Attineos"
