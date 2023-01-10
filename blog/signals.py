from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_user_success(sender, request, user, **kwargs):
    print("Login successful......")
    user_ip = request.META.get('REMOTE_ADDR')
    print('Client IP:',user_ip)
    request.session['user_ip'] = user_ip