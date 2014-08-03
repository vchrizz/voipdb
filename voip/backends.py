from django.contrib.auth.models import User, check_password
from voip.models import members
#import django.contrib.auth as auth

class RedeemerAuth(object): #auth.backends.ModelBackend):
    def authenticate(self, username=None, password=None):    
        # Check the username/password and return a User.
        try:
            user = members.objects.get(nickname=username)
            if user.check_password(password):
                return user
        except members.DoesNotExist:
            return None 

    def get_user(self, user_id):
        try:
#            return User.objects.get(id=user_id)
            return members.objects.get(pk=id)
        except members.DoesNotExist:
           return None

