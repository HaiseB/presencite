from .models import MarqueeMessage

def marquee_message(request):
    message = MarqueeMessage.objects.filter(afficher=True).order_by('-created_at').first()
    return {'marquee_message': message.message if message else ''} 