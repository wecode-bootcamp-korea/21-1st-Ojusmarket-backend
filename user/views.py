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

            re_identity = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{5,15}$)'
            re_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^~@$!%*#?&])[A-Za-z\d^~@$!#%*?&]{8,18}$'
            re_phone    = '^[0-9]{3}[0-9]{4}[0-9]{4}$'
            re_name     = '^[가-힣]+'
            re_email    = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

            if not re.match(re_identity, data['identity']) or\
               not re.match(re_password, data['password']) or\
               not re.match(re_phone, data['phone']) or\
               not re.match(re_name, data['name']) or\
               not re.match(re_email, data['email']):

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

