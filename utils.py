import jwt

from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM
from user.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
      try:
          identity_token = request.headers.get('Authorization', None)
          payload        = jwt.decode(identity_token, SECRET_KEY, ALGORITHM)
          user           = User.objects.get(id = payload['id'])
          request.user   = user
          print(request.user)
      except jwt.exceptions.DecodeError:
          return JsonResponse({'message': 'INAVLID TOKEN'}, status=400)       
      except User.DoesNotExist:
          return JsonResponse({'message': 'THIS ACCOUNT DOES NOT EXIST'}, status=400)
      
      return func(self, request, *args, **kwargs)
      
    return wrapper 