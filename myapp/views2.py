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
                  [Note :- request.POST is used for x-www-form-urlencoded or multipart/form-data (i.e. HTML forms or file uploads).]

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
                 'message' : 'User logged in successfully' , 
                #  'csrf_token' : 'abc123' , 
                 'csrf_token' : 'Token ImplementingPagination2025',  # For ⭐) Implementing Pagination
                 'username': user.username   # For ⭐) Data Validation and Error Handling 
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




'''

⭐) Data Validation and Error Handling  :- 

'''

from django.core.exceptions import ValidationError
from .models import To_Do_Validation   
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_To_Do_Validation(request):

    if request.method == "POST":

        data = json.loads(request.body)
        print("data :- ",data)       # Output :-  data :-  {'username': 'Madhav P Again for To_Do_Validation', 'task': 'Finish Django homework'}

        task = data.get("task")    
        print("task :- ",task)       # Output :-  task :-  Finish Django homework

        # Simulated header check
        token = request.headers.get("Authorization")
        print("Token :- ",token)     # Output :-  Token :-  Token abc123

        # if token != "Token abc123":
        #     return JsonResponse({"message": "Access Denied"}, status=403)

        if token != "Token ImplementingPagination2025":
            return JsonResponse({
                "message" : f'Access Denied its not Token("ImplementingPagination2025") != {token}'
            })

        username = data.get("username")    #  <- pass this in your request body
        print("Username :- ",username)        # Output :-  Username :-  Madhav P Again for To_Do_Validation

        if not username:
            return JsonResponse({"error": "Username is required"}, status=400)

        try:
            user = User.objects.get(username=username)
            print("user :- ",user)        # Output :- user :-  Madhav P Again for To_Do_Validatio

        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid user"}, status=400)

        if not task:
            return JsonResponse({"error": "Task is required"}, status=400)

        # new_todo = To_Do_Validation(task=task, user=request.user) 
        #
        print("user = request.user :- ",request.user) 

        new_todo = To_Do_Validation(task=task, user=user)    # ⭐) Implementing Pagination

        print("new_todo  :- ", new_todo)       # Output :- new_todo  :-  Finish Django homework
        
        try:
            new_todo.full_clean()
            new_todo.save()
            return JsonResponse({
                'message': 'To_Do added Successfully'
            }, status=201)
        except ValidationError as e:
            return JsonResponse({
                'error': e.message_dict
            }, status=400)
    
    return JsonResponse({
        'message': 'Invalid request'
    }, status=400)



'''

Path :-  http://127.0.0.1:8000/To_Do_Validation/

Input  :- 

{
  "username": "Madhav P Again for To_Do_Validation",
  "task": "Finish Django homework"
}


Output :-

{
    "message": "To_Do added Successfully"
}

'''




'''

⭐) Implementing Pagination  :- Pagination divides your content into separate pages, making it easier for users to navigate through large sets of data.

'''


from django.http import JsonResponse
from .models import To_Do_Validation

@csrf_exempt
def get_ToDos(request):
    if request.method == "GET":

        token = request.headers.get("Authorization")
        if token !="Token ImplementingPagination2025":
            return JsonResponse({
                "message" : "Access Denied"
            }, status=403)
        
        username = request.GET.get('username')    # <-  Pass it in the request 

        if not username:
            return JsonResponse({
                "error" : "Username is required"
            }, status=400)
        
        try : 

            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({
                'error' : "Invalid user"
            },status=400)
        
        
        # Pagination Logic 
        page = request.GET.get('page'  , 1)
        page = int(page) if page.isdigit() else 1
        # page = 1 if page < 1 else page
        page = max(1 , page)

        page_size = 3 
        start_index = (page - 1) * page_size
        end_index = start_index + page_size


        # ToDos_Pagination_Content = To_Do_Validation.objects.filter(user=request.user)[start_index:end_index]
        ToDos_Pagination_Content = To_Do_Validation.objects.filter(user=user)[start_index:end_index]

        return JsonResponse({
            'ToDos' : list(ToDos_Pagination_Content.values())     # Note that we use the values() method to serialize the tasks as dictionaries.
        })
    return JsonResponse({
        "message" : "Only GET allowed"
    }, status=405)



'''

Output :- 


Path :-   http://127.0.0.1:8000/get_ToDos_Pagination?username=Madhav%20P%20Again%20for%20Pagination%20Testing&page=1

{
    "ToDos": [
        {
            "id": 7,
            "task": "Django Task 1",
            "completed": false,
            "user_id": 3
        },
        {
            "id": 8,
            "task": "SQL Task 2",
            "completed": false,
            "user_id": 3
        },
        {
            "id": 9,
            "task": "MERN Task 3",
            "completed": false,
            "user_id": 3
        }
    ]
}


Path :- http://127.0.0.1:8000/get_ToDos_Pagination?username=Madhav%20P%20Again%20for%20Pagination%20Testing&page=2

{
    "ToDos": [
        {
            "id": 10,
            "task": "Flask Task 4",
            "completed": false,
            "user_id": 3
        },
        {
            "id": 11,
            "task": "AWS Task 6",
            "completed": false,
            "user_id": 3
        },
        {
            "id": 12,
            "task": "React Native Task 7",
            "completed": false,
            "user_id": 3
        }
    ]
}


Path :-  http://127.0.0.1:8000/get_ToDos_Pagination?username=Madhav%20P%20Again%20for%20Pagination%20Testing&page=3

{
    "ToDos": [
        {
            "id": 13,
            "task": "Python Task 8",
            "completed": false,
            "user_id": 3
        },
        {
            "id": 14,
            "task": "JavaScript Task 9",
            "completed": false,
            "user_id": 3
        }
    ]
}

'''