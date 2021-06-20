import json, re, bcrypt, jwt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .utils       import login_decorator
from .models      import User
from my_settings  import SECRET_KEY, ALGORITHM

# class UserView(View):
#     @login_decorator
#     def get(self, request):
#         user = {
#             "id"   : "",
#             "name" : "",
#             "phone" : "",
#             "address" : ""
#         }
#         return user 


class UserIdentityCheck(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(identity=data['identity']).exists():
                return JsonResponse({'message' : 'IDENTITY_ALREADY_EXISTS'}, status=400)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
   
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class UserSignUp(View):
    def post(self, request):
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

class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            identity = data ['identity']
            password = data ['password']
            
            if not User.objects.filter(identity = identity).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401) 

            user = User.objects.get(identity=identity)
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
        
            return JsonResponse({'acess_token' : jwt.encode({'id':user.id}, SECRET_KEY, ALGORITHM)}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class UserView(View):
    @login_decorator
    def get(self, request):
        try:
            user = request.user
            
            user_list = {
                'name'    : user.name,
                'phone'   : user.phone,
                'address' : user.address
            }
            return JsonResponse({'user' : user_list}, status=200)

        except KeyError:
            JsonResponse({'message' : 'KEY_ERROR'}, status=400)