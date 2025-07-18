'''
⭐) Implement Basic User authentication (views2.py)  and  Protecting Routes with Middleware

'''

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.models import User   # So even if you don’t define your own model, Django is using User model under the hood to store these values in the auth_user table in the database.

from django.contrib.auth import authenticate , login , logout

from django.contrib.auth.decorators import login_required

from django.middleware.csrf import get_token

import json

@csrf_exempt
def register(request):
    
    if request.method == "POST":
        try :
              
              # data = request.POST  
              '''
                  Note :- request.POST is used for x-www-form-urlencoded or multipart/form-data (i.e. HTML forms or file uploads).
              '''

              data = json.loads(request.body)

              print("Incoming JSON:", data)

              username = data.get('username')

              email = data.get('email')

              password = data.get('password')
            
              # Your password is being sent as a number, not a string. That breaks create_user() which expects a string — and Django throws an internal error. To prevent facing issue do this :- 
              if password is not None:
                  password = str(password)


              if not username or not email or not password:
                   return JsonResponse({
                      'error' : 'Username email , and password are required '
                }, status=400)    # 400 indicates bad request
        

              if User.objects.filter(username=username).exists():
                    return JsonResponse({
                          'error' : f'Username :- {username}  already exits .'
                    }, status=400)
       
              if User.objects.filter(email=email).exists():
                    return JsonResponse({
                         'error' : f'Email  :-  {email} already exits .'
                    } , status=400)

        
              user = User.objects.create_user(username=username , email = email , password = password)
              user.save()

              return JsonResponse({
                    'message' : 'User registered successfully'
                }, status=201)
        except json.JSONDecodeError :
                return JsonResponse({
                  'error' : 'Invalid JSON'
            }, status=400)
    return JsonResponse({
          'message' : 'Only POST method is allowed'
    }, status=405)   # 405 indicates method not allowed 



'''

Input :-   Path :- http://127.0.0.1:8000/register/

{
    "username" : "Madhav P",
    "email" : "madhavp2023@gmail.com",
    "password" : 12345
}


Output :- 


{
    "message": "User registered successfully"
}

'''





@csrf_exempt
def user_login(request):
    if request.method == "POST":

        # data = request.POST  
        data = json.loads(request.body)

        username = data.get('username')

        password = data.get('password')

        print(username , password)   # Output :-  Madhav P 12345


        if not username or not password:
            return JsonResponse({
                'error' : 'Username and password are required'
            } , status=400)
        

        user = authenticate(request , username=username, password =password)

        if user is not None:
            login(request , user)

            # return JsonResponse({
            #     'message' : 'User Logged in Successfully'
            # } , status=201)


            '''

            ⭐) Returning Token in Login Response :-  To authenticate users, you need to return a token when they log in. This token can be used to authorize future requests. Here's an example of how you can return a token in the login response :-   
            
            # Return the CSRF token in the response. For simplicity, we are using a fixed token value.

            '''

            return JsonResponse({
                 'message' : 'User logged in successfully' , 'csrf_token' : 'abc123'
            })
        
        '''

        Input :- 

        {
           "username" : "Madhav P",
           "password" : 12345
        }
        
        Output :- 

        {
           "message": "User logged in successfully",
           "csrf_token": "abc123"
        }

        '''

        return JsonResponse({
            'error' : 'Invalid credentials'
        } ,status=400)
    
    return JsonResponse({
        'message' : 'Only POST method is allowed'
    }, status=405)



'''

Input :-   Path :- http://127.0.0.1:8000/login/

{
    "username" : "Madhav P",
    "password" : 12345
}


Output :- 


{
    "message": "User Logged in Successfully"
}

'''



@csrf_exempt
def user_logout(request):

    if request.method == "POST":

        logout(request)

        return JsonResponse({
            'message' : 'User logged out successfully'
        }, status=200)
    
    return JsonResponse({
        'message' : 'Only POST method is allowed'
    }, status=405)


'''

Input :-   Path :- http://127.0.0.1:8000/logout/


Output :- 

{
    "message": "User logged out successfully"
}

'''


# @login_required
def protected_view(request):
     return JsonResponse({
          'message' : 'This is Protected Route !'
     })