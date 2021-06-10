import json, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse

from .models      import User
from my_settings  import SECRET_KEY, ALGORITHM

class SigninView(View):
    def POST(self,request):
        try:
            data     = json.loads(request.body)
            identity = data ['identity']
            password = data ['password']
            
            if not User.objects.filter(identity = identity).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401) 
        
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('uft-8')):
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
        
            return JsonResponse({'message': 'SUCCESS', 'user_token' : jwt.encode({'id:user.id'}, SECRET_KEY, ALGORITHM)}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
