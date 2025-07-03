'''

⭐) Create your views here.

myapp/views.py

'''


from django.http import HttpResponse          # 🌐 HttpRequest Docs :-  https://docs.djangoproject.com/en/5.2/ref/request-response/

def home(request):
    return HttpResponse('Hello , world')


'''

Django-Learning/myapp/views.py

⭐) Rendering Templates in Views 

'''

from django.shortcuts import render

def home(request):
    return render(request , 'home.html') 



'''

⭐) Creating JSON View  

⭐) Middleware allows you to manage requests before they reach your views. JSON responses are key for creating APIs.


⭐) The request.META dictionary contains all available HTTP headers. The key 'REMOTE_ADDR' in the request.META dictionary contains the IP address of the client.

Other useful keys in the request.META dictionary include :- 

1) 'HTTP_USER_AGENT':-  The client's user agent - the browser or the application that made the request.
2) 'HTTP_REFERER'   :-  The URL of the page that is linked to the current page.
3) 'HTTP_HOST'      :-  The hostname of the server (for example, www.example.com), etc.

Django-Learning/myapp/views.py

'''


from django.http import HttpResponse ,JsonResponse

def json_view(request):
    return JsonResponse({
        'message' : 'Hello , JSON !',
        'status' : 'Success',
        'code' : 200
    })


'''

⭐) Introduction to URL Parameters and Query Parameters :- 

⭐) Add URL Parameters :-  URL parameters are parts of the URL that can be used to pass information to views. Also Known as " path parameter "

'''

# def user_view(request , name):
#     return HttpResponse(f"Hello, {name}!")



'''

⭐) Utilize Query Parameters :-  Query parameters allow you to send additional information to your views using the URL. These come after the ? in a URL and are used to filter/search/pass data to the server.

'''

def search_view(request):
    query = request.GET.get('q' , '')
    category =request.GET.get('category', '')
    return HttpResponse(f'You searched for: {query} in category: {category}')      # Path :- http://127.0.0.1:8000/search/?q=python&category=programming


'''

⭐) Defining a Custom 404 View 

'''

from django.http import HttpResponse

def custom_404(request, exception):
    # return HttpResponse('<h1>Hey there, page not found</h1>', status=404)     # Path :- http://127.0.0.1:8000/g

    #  Modify the code to render a template when a 404 error occurs with the status code 404
    return render(request,'home.html',status=404)     # Path :- http://127.0.0.1:8000/g



'''

⭐) Managing Data with SQLite and Django ORM 

=> Connects to a SQLite database and retrieves data from it :- 

'''

from django.http import HttpResponse
import sqlite3

def get_items(request):

    # Create a new SQLite connection for each request
    connection = sqlite3.connect('db.sqlite3')
    items = []

    try:

        # Retrive items from the database
        raw_query = 'Select * from items'
        items = connection.execute(raw_query).fetchall()

    finally:

        # Close the connection to ensure it is not reused 
        connection.close()

    return HttpResponse(items)



'''

⭐)  Defining and Exporting Django Models  :-  The views include the logic for interacting with the database using the model.

'''

from django.http import HttpResponse

from .models import Song

# The add_and_get_items view creates a new Item, saves it, and then retrieves all items from the database.
def add_and_get_items(request):

    # song = Song(title='Song 1', artist='Artist 1')

    song = Song(artist='Krishnakumar Kunnath' , title = 'Lambi Judai')

    song.save()   # Save item to database

    songs = Song.objects.all()    # Retrieve all items   (Returns the query set)
    # output = ', '.join(item.name for item in items)

    songs_list = list(songs.values('title' , 'artist'))

    # songs_str = ', '.join([str(song) for song in songs])

    # return HttpResponse(f"Items : {output}")

    # return HttpResponse(songs_str)      

    return JsonResponse(songs_list, safe=False)



'''

⭐) Integrating SQLite3 with Django ORM and Creating a Model :- Adding a new task via views.py


⭐) Note the use of @csrf_exempt to disable CSRF protection for this view. CSRF protection :- Is a security feature to prevent cross-site request forgery attacks. In a production environment, you should handle CSRF protection properly but in this course, we will disable it for simplicity.

'''

from django.views.decorators.csrf import csrf_exempt

from .models import ToDo

import json

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_todo = ToDo(task=data['task'])

        new_todo.save()

        return JsonResponse({
            'id' : new_todo.id,
            'task' : new_todo.task
        }, status=201)
    return JsonResponse({
        'message' : 'Invalid request'
    }, status=400)



'''

⭐) Creating Relationships Between Models ;:- create views to handle adding new categories and tasks with their corresponding categories.

'''

import json
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category , To_Do

@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_category = Category(name=data['name'])
        new_category.save()
        return JsonResponse({'id' : new_category.id , 'name' : new_category.name}, status=201)
    return JsonResponse({
        'message' : 'Invalid request'
    }, status=400)


'''

Input :-  

{
    "name": "Work"
}

Output :- 

{
  "id": 1,
  "name": "Work"
}

'''
    
@csrf_exempt
def add_todo_with_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # category = Category.objects.get(name=data['category'])
        category_variable = Category.objects.filter(name=data['category'])[0]  # Better use this ! 
        '''

        ⭐) Note :-  We are filtering the category by name and taking the first result instead of using get() as we earlier. This is because when we run the code several times, the add_category view will be called multiple times, and we may have multiple categories with the same name. In this case, the get() method will raise an exception, while the filter() method will return a queryset with all the categories with the same name, and we can take the first one.

        '''
        new_todo = To_Do(task=data['task'] , category=category_variable)  # this happens to be both the model field and variable name being the same.
        new_todo.save()
        return JsonResponse({'id' : new_todo.id , 'task' : new_todo.task, 'category' : new_todo.category.name} , status=201)
    return JsonResponse({
        'message' : 'Invalid request' 
    } , status=400)


'''

Input :- 

{
    "task": "Prepare presentation",
    "category": "Work"
}

Output :- 

{
  "id": 1,
  "task": "Prepare presentation",
  "category": "Work"
}

'''


'''

⭐) Validating Data with Django :- Handling validation errors within your views

'''

from .models import To_Do_2
from django.core.exceptions import ValidationError

@csrf_exempt
def add_To_Do_2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_todo = To_Do_2(task=data['task'])

        try:
            new_todo.full_clean()
            new_todo.save()
            return JsonResponse({
              'id' : new_todo.id , 'task' : To_Do_2.task
            } , status=201)
        except ValidationError as e:
            return JsonResponse({
                'message' : str(e)
            } , status=400)
    return JsonResponse({
        'message' : 'Invalid request'
    })


'''

Input :- 

{
  "task" : "Bu"
}

Output :- 

{
  "message": "{'task': ['Task must be at least 3 characters long']}"
}

'''


'''

⭐) Understanding Data Retrieval in Django ORM :- 

'''

from .models import To_Do_3
import json

# @csrf_exempt
# def add_To_Do_3(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         new_To_Do_3 =  To_Do_3(task=data['task'] , completed  = data.get('completed', False))
#         new_To_Do_3.save()

#         return JsonResponse({
#             'id' : new_To_Do_3.id , 'task': new_To_Do_3.task
#         } , status=201)
#     return JsonResponse({
#         'message' : 'Invalid request'
#     } , status=400)


'''

Output :-  added 4 json body content ... 

'''


# def get_To_Dos_3(request):
#     todos = To_Do_3.objects.all().values()
#     return JsonResponse(list(todos) , safe=False)

 
'''

Output :- 

[
    {
        "id": 1,
        "task": "Django Course",
        "completed": false
    },
    {
        "id": 2,
        "task": "Flask Course",
        "completed": true
    },
    {
        "id": 3,
        "task": "MERN Stack Course",
        "completed": true
    },
    {
        "id": 4,
        "task": "DBMS Course",
        "completed": false
    }
]

'''



# def get_completed_3(request):
#     todos = To_Do_3.objects.filter(completed = True).values()   # .values() :-  returns dicts instead of model objects → easier for JsonResponse.
#     return JsonResponse(list(todos) , safe=False)


'''

Output :- 

[
    {
        "id": 2,
        "task": "Flask Course",
        "completed": true
    },
    {
        "id": 3,
        "task": "MERN Stack Course",
        "completed": true
    }
]

'''


# Method Two :- 

@csrf_exempt
def add_To_Do_3(request):

    if request.method == "POST":
        try :
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'message'  : "Invalid JSON."
            }, status=400)
        

        To_Dos_3 = data if isinstance(data,list) else data.get('To_Do_3', [])    # isinstance(data, list)  →  Checks if the data variable is a list (like [{...}, {...}]).

        # This is is used when you're adding multiple to-dos at once
        if To_Dos_3:
            for todo in To_Dos_3:
                title = todo.get('title' , ' ').strip()
                description = todo.get('description' , '').strip()
                completed = todo.get('completed' , False)

                if not title or not description:
                    return JsonResponse({
                        'message' : "Title and description are required."
                    }, status=400)
                
                new_To_Do_3 = To_Do_3(
                    title = title,
                    description = description,
                    completed = completed
                )
                
            try:   
                new_To_Do_3.full_clean()
                new_To_Do_3.save()
            except ValidationError as e:
                return JsonResponse({
                    'meeage' : str(e)
                }, status=400)
            

            return JsonResponse({
                'message' : "Todos Created Succesfully ! "
            } , status=201)
        else:
            return JsonResponse({
                'nessage' : "No todos provided."
            }, status=400)
    return JsonResponse({
        'message' : "Only POST method is allowed."
    } , status=405)


'''

Input :- 

[
  {"title": "Learn Django", "description": "Study models", "completed": false},
  {"title": "Learn Flask", "description": "Learn about MVC", "completed": true},
  {"title": "Learn DBMS", "description": "Learn about DML and DDL", "completed": true},
  {"title": "Learn MERN", "description": "Study about MongoDB", "completed": true}
]

Output :-

{
    "message": "Todos Created Succesfully ! "
}

'''

def get_To_Dos_3(request):
    # Should retrieve incomplete tasks and completed tasks 
    To_Dos_3 = To_Do_3.objects.all().values()
    return JsonResponse(list(To_Dos_3),  safe=False)
    # or 
    # return JsonResponse(list(To_Dos_3) , safe=True)


'''

Output :- 

[

 {
        "id": 1,
        "title": "Learn Django",
        "description": "Study models",
        "completed": false
    },
    {
        "id": 2,
        "title": "Learn Flask",
        "description": "Learn about MVC",
        "completed": true
    },
    {
        "id": 3,
        "title": "Learn DBMS",
        "description": "Learn about DML and DDL",
        "completed": true
    },
    {
        "id": 4,
        "title": "Learn MERN",
        "description": "Study about MongoDB",
        "completed": true
    }

]


'''

from django.db.models import Q

'''

Note :-  Q objects allow you to perform more advanced queries by combining multiple conditions. To check if something is contained in a field, you can use the __icontains lookup with the field name: field_name__icontains.


Syntax :- objects = Todo.objects.filter((Q(A) | Q(B)) & Q(C))

Example :- 

from django.db.models import Q

todos = Todo.objects.filter(
    (Q(title__icontains="Clean") | Q(title__icontains="Wash")) & Q(completed=True)
).values()


'''

def get_filtered_To_Do_3(request):
    To_Dos_3 = To_Do_3.objects.filter(Q(completed=True) | Q(title__icontains="Clean")).values()
    return JsonResponse(list(To_Dos_3) , safe=False)


'''

Output :- 

Filtered todos: [{'id': 2, 'task': 'Pay bills', 'completed': True}, {'id': 3, 'task': 'Clean house', 'completed': True}, {'id': 4, 'task': 'Clean the balcony', 'completed': False}]

'''