from rest_framework.authentication import *
from generic.models import Integradora

class AUTAAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY') # get the api-key from paysmart
        if not api_key: # no api-key passed in request headers
            return None # authentication did not succeed

        try:
            integradora = Integradora.objects.get(api_key=api_key)
            user = integradora.user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, None) # authentication successful