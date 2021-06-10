import json
import re
import bcrypt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models      import User

class UserIdentityCheck(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(identity=data['identity']).exists():
                return JsonResponse({'message' : 'IDENTITY_ALREADY_EXISTS'}, status=400)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
   
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class UserSignUp(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            REGEX_USER_IDENTITY = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{5,15}$)'
            REGEX_PASSWORD      = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^~@$!%*#?&])[A-Za-z\d^~@$!#%*?&]{8,18}$'
            REGEX_PHONE         = '^[0-9]{3}[0-9]{4}[0-9]{4}$'
            REGEX_NAME          = '^[가-힣]+'
            REGEX_EMAIL         = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

            if not re.match(REGEX_USER_IDENTITY, data['identity']) or\
               not re.match(REGEX_PASSWORD, data['password']) or\
               not re.match(REGEX_PHONE, data['phone']) or\
               not re.match(REGEX_NAME, data['name']) or\
               not re.match(REGEX_EMAIL, data['email']):

                return JsonResponse({'message':'INVALID_INPUT'}, status=400)

            if User.objects.filter(
                Q(identity=data['identity'])|
                Q(phone=data['phone'])|
                Q(email=data['email'])
            ).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=409)

            User.objects.create(
                identity = data['identity'],
                password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                name     = data['name'],
                phone    = data['phone'],
                email    = data['email'],
                address  = data['address']
                )
            return JsonResponse({'message':'SUCCESS'}, status=201)
            
        except KeyError :
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

