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
from django.http import JsonResponse
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

@csrf_exempt
def add_To_Do_3(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_To_Do_3 =  To_Do_3(task=data['task'] , completed  = data.get('completed', False))
        new_To_Do_3.save()

        return JsonResponse({
            'id' : new_To_Do_3.id , 'task': new_To_Do_3.task
        } , status=201)
    return JsonResponse({
        'message' : 'Invalid request'
    } , status=400)


'''

Output :-  added 4 json body content ... 

'''


def get_To_Dos_3(request):
    todos = To_Do_3.objects.all().values()
    return JsonResponse(list(todos) , safe=False)

 
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



def get_completed_3(request):
    todos = To_Do_3.objects.filter(completed = True).values()   # .values() :-  returns dicts instead of model objects → easier for JsonResponse.
    return JsonResponse(list(todos) , safe=False)


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

from django.shortcuts import get_object_or_404

def get_To_Dos_3(request,id): # Accept id from URL
        
    # Should retrieve incomplete tasks and completed tasks 
    # To_Dos_3 = To_Do_3.objects.all().values()
    # return JsonResponse(list(To_Dos_3),  safe=False)


    # Model we are using to understand this concept is :- To_Do_3 from models.py 

    # ⭐) Retrieving a Single Record by ID
    # try:
        # To_Dos_3 = To_Do_3.objects.get(id=id)

        To_Dos_3 = get_object_or_404(To_Do_3, id=id)   # There is also a shortcut method get_object_or_404() that simplifies this process. It retrieves the object if it exists, or raises a 404 error if not found. for this no need of try and except .

        return JsonResponse({
            'id' : To_Dos_3.id ,'task' : To_Dos_3.task , 'completed' : To_Dos_3.completed
        }, status=200)
    # except To_Do_3.DoesNotExist:
    #     return JsonResponse({
    #         'message' : 'To_Do_3 not found'
    #     },status=404)


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

# Retrieving a Single Record by ID

'''

Output :- http://127.0.0.1:8000/get_To_Dos_3/4/

{
    "id": 4,
    "task": "False",
    "completed": false
}

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


'''

⭐) The preload() view is used to insert some default data into your database, only if it doesn’t already exist.

'''

from .models import To_Do_preload_Example

@csrf_exempt
def preload(request):

    tasks = [
        ('Do the laundry', False, 'Home', 'Urgent'),
        ('Buy groceries', False, 'Shopping', 'Weekly'),
        ('Call mom', True, 'Personal', 'Family')
    ]

    
    for task_preload, completed_preload , category_preload , tag_preload in tasks:
        if not To_Do_preload_Example.objects.filter(task_preload=task_preload).exists():

            '''
                
            Left task is the field in your Todo model (i.e., models.CharField(...)).

            Right task is the variable from your for loop (for task, completed, ...).

            '''

            To_Do_preload_Example.objects.create(
                task_preload = task_preload,
                completed_preload = completed_preload,
                category_preload = category_preload,
                tag_preload = tag_preload
            )
        
        return JsonResponse({
            'message' : 'Preloaded Successfully !'
        })


'''

Output :-  path ;-http://localhost:8000/preload/

{
    "message": "Preloaded Successfully !"
}

'''


def get_todos_by_category_and_tag(request):
     category_preload = request.GET.get('category_preload')

     tag_preload = request.GET.get('tag_preload')

     if category_preload and tag_preload:
         ToDos_preload = To_Do_preload_Example.objects.filter(category_preload=category_preload , tag_preload=tag_preload)

         return JsonResponse({
             'ToDos_preload' : list(ToDos_preload.values())
         }, status=200)
     return JsonResponse({
         'message' : "Category and/or Tag not provided"
     }, status=400)


'''

Output :-    Path :-  http://localhost:8000/ToDos_preload/filter/?category_preload=Home&tag_preload=Urgent

{
    "ToDos_preload": [
        {
            "id": 1,
            "task_preload": "Do the laundry",
            "completed_preload": false,
            "category_preload": "Home",
            "tag_preload": "Urgent"
        }
    ]
}

'''



'''

⭐) Updating Records by ID :-  Using the data from To_Do_3 Model ! 

'''

from django.views.decorators.http import require_http_methods   # Blocks all other HTTP methods (like GET, POST, DELETE, etc.)

from .models import To_Do_Update


# Need to create a Update_add_data view ! not using preload for some data . 

@csrf_exempt
def Update_Example_add_Data(request):
    if request.method == "POST":

       try:
           data = json.loads(request.body)

           # Extract the data manually from request body
           task_Variable =  data.get('task')    # user sends 'task' in JSON
           completed_Variable =  data.get('completed')

           print("Extracted task :- ", task_Variable)    # Output :- Extracted task: Study Python
           print("Extracted completed :- ", completed_Variable)    # Output :- Extracted completed :-  True

           # Now create a To_Do_Update object using this data
           To_Do_Update_Variable = To_Do_Update(task_update=task_Variable, completed_update = completed_Variable)

           To_Do_Update_Variable.save()
           print("Saved to DB:", To_Do_Update_Variable.id)  # Output :- Saved to DB: 1

           return JsonResponse({
             'message' : "The Data for Update testing is Added Successfully. Now you can test for Update_To_Do", 'GET Data' : {
                'id' : To_Do_Update_Variable.id,
                'task': To_Do_Update_Variable.task_update,
                'completed' : To_Do_Update_Variable.completed_update
                }
            }, status=201)
    
       except Exception as e:
        return JsonResponse({
            'error' : str(e)
        } , status=400)
      
    return  JsonResponse({
        'error' : "Invalid Input"
    } , status=400)



'''

Input :- 

{
    "task":"Study Python",
    "completed":true
}

Output :- Path :-  http://localhost:8000/update_add_post_data/

{
    "message": "The Data for Update testing is Added Successfully. Now you can test for Update_To_Do",
    "GET Data": {
        "id": 1,
        "task": "Study Python",
        "completed": true
    }
}

'''

@csrf_exempt
@require_http_methods(['PUT'])   # PUT :- Replaces the entire resource. All fields must be sent, or they may reset.
def Update_To_Do(request ,  id):

    try:
        To_Do_Update_Variable = get_object_or_404(To_Do_Update, id=id)

        data = json.loads(request.body)

        print("Json Data is :- ",data)    # Output :-  Json Data is :-  {'task': 'Study Flask'}

        #  Only updating task_update (no force on completed_update)  (Wrong Way)
        To_Do_Update_Variable.task_update = data['task']

        print("Extracted Task from user is :-  ",To_Do_Update_Variable)   # Output :-  Extracted Task from user is :-   Study Flask

        To_Do_Update_Variable.save()

        return JsonResponse({
            'message' : "To Do of task content got  Updated"
        })
    except Exception as e:
        return JsonResponse({
            'error' : str(e)
        } , status=400)
    


'''

Input :- Path :- http://localhost:8000/To_Do_Update_Variable/1

{
    "task":"Study Flask"
}

Output :- 

{
    "message": "To Do of task content got  Updated"
}

'''


@csrf_exempt
def get_To_Dos_Update(request):
    Fetched_ALL_To_Do_Update = To_Do_Update.objects.all()

    # todos = Todo.objects.all().values('id', 'task', 'completed')
    # return JsonResponse(list(todos), safe=False)


    # List Comprehension Way :- manually construct a list of dictionaries
    return JsonResponse({
        'Fetched_ALL_To_Do_Update' : [
            {
                'id': Loop_Variable.id,
                'task' : Loop_Variable.task_update,
                'completed' : Loop_Variable.completed_update
            }  for Loop_Variable in Fetched_ALL_To_Do_Update
        ]
    })


'''

Output :-   Path :- http://localhost:8000/Fetched_ALL_To_Do_Update/

{
    "Fetched_ALL_To_Do_Update": [
        {
            "id": 1,
            "task": "Study Flask",
            "completed": true
        }
    ]
}

'''


from .models import To_Do_Patch

@csrf_exempt
def add_POST_Data_For_Patch(request):

    if request.method == "POST":
         
         try:
             data = json.loads(request.body)

             Extracted_course = data.get("course")

             Extracted_description = data.get('description')

             Extracted_course_completed = data.get('course_completed')

             print("Extracted Course Data :-  ",Extracted_course)

             print("Extracted Description Data :-  ",Extracted_description)

             print("Extracted Course Completed Data :-  ",Extracted_course_completed)

             To_Do_Patch_Object  = To_Do_Patch(course=Extracted_course, description=Extracted_description, course_completed = Extracted_course_completed)
         

             To_Do_Patch_Object.save()
             To_Do_Patch_Object.full_clean()

             print("Saved to DB:", To_Do_Patch_Object.id)  # Output :- Saved to DB: 1

             return JsonResponse({
                 'meesage' : "To_Do Patch Data Added Successful. Now Ready for Patch Testing",
                 "POST DAta" : [
                     {
                         'id' : To_Do_Patch_Object.id,
                         'course' : To_Do_Patch_Object.course,
                         'description':To_Do_Patch_Object.description,
                         'completed':To_Do_Patch_Object.course_completed,
                     }
                 ]
             },status=201)
         except Exception as e:
             return JsonResponse({
                 'error' : str(e)
             }, status=400)
         
    return JsonResponse({
        'message' : "Invalid Input"
    })
         


'''

Input :-   Path :- http://localhost:8000/add_POST_Data_For_Patch/

{
    "course":"Django For Beginners",
    "description": "○ Django is more feature-rich and follows the \"batteries-included\" philosophy.○ It includes built-in authentication, an admin panel, and ORM for database management.",
    "course_completed": true
}


OUtput :- 

{
    "meesage": "To_Do Patch Data Added Successful. Now Ready for Patch Testing",
    "POST DAta": [
        {
            "id": 6,
            "course": "Django For Beginners",
            "description": "○ Django is more feature-rich and follows the \"batteries-included\" philosophy.○ It includes built-in authentication, an admin panel, and ORM for database management.",
            "completed": true
        }
    ]
}

'''
            
@csrf_exempt  
def Update_Patch(request , course):

    if request.method == 'PATCH':

        try:
            
            # Step 1: Find the object by course
            Update_Patch_Variable = get_object_or_404(To_Do_Patch , course=course)

            # Step 2: Load incoming data
            data = json.loads(request.body)

            # Step 3: Update only fields provided in PATCH
            if 'course' in data:
                Update_Patch_Variable.course = data['course']

            if 'description' in data:
                Update_Patch_Variable.description = data['description']
            
            if 'completed' in data:
                Update_Patch_Variable.course_completed = data['course_completed']

            # Step 4: Save the updated object
            Update_Patch_Variable.save()

            # Step 5: Return response (with return!)
            return JsonResponse({
            'message' : "POST DATA Got Updated Using PATCH",
            "Patch DATA (Partically Updated)":
                    [
                        {
                            "id" : Update_Patch_Variable.id,
                            "course":Update_Patch_Variable.course,
                            "description":Update_Patch_Variable.description,
                            "course_completed":Update_Patch_Variable.course_completed
                        }
                    ]
            }, status=201)
        except Exception as e:
            return JsonResponse({
                "error" : str(e)
            }, status=400)
    return JsonResponse({
        "error"  : "Invalid Input -  PATCH Only"
    })



'''

Input :-  Path :- http://localhost:8000/Update_Patch/Django For Beginners/

{
    "description": " 1) Django is more feature-rich and follows the \"batteries-included\" philosophy. 2) It includes built-in authentication, an admin panel, and ORM for database management. 3) Great for large-scale projects or when you need an all-in-one solution."
}


Output :- 

{
    "message": "POST DATA Got Updated Using PATCH",
    "Patch DATA (Partically Updated)": [
        {
            "id": 7,
            "course": "Django For Beginners",
            "description": " 1) Django is more feature-rich and follows the \"batteries-included\" philosophy. 2) It includes built-in authentication, an admin panel, and ORM for database management. 3) Great for large-scale projects or when you need an all-in-one solution.",
            "course_completed": true
        }
    ]
}


'''



def get_Patch_Data(request):

    try:

         Fetched_Patch_Data_Object = To_Do_Patch.objects.all()

         return JsonResponse({
             'message' : "Retrieval of Patch DATA successfull",
             " Fetched_Patch_Data_Object ":[
            {
                "id" : Loop_DATA.id,
                "course" : Loop_DATA.course,
                "description": Loop_DATA.description,
                "course_completed":Loop_DATA.course_completed

            }
            for Loop_DATA in Fetched_Patch_Data_Object
           ]
         } ,status=201)
    except Exception as e:
        return JsonResponse({
            'error' : str(e)
        }, status=400)
    


'''

Output :-   Path :- 

{
    "message": "Retrieval of Patch DATA successfull",
    " Fetched_Patch_Data_Object ": [
        {
            "id": 7,
            "course": "Django For Beginners",
            "description": " 1) Django is more feature-rich and follows the \"batteries-included\" philosophy. 2) It includes built-in authentication, an admin panel, and ORM for database management. 3) Great for large-scale projects or when you need an all-in-one solution.",
            "course_completed": true
        }
    ]
}

'''


'''

⭐) Deleting Records by ID  :- Using  To_Do_3 Model 

Added Data :- From :- POST for add_To_Do for DELETE TESTING  . Path :-   http://127.0.0.1:8000/add_To_Do_3/

Input :-   

{
        "id": 1,
        "task": "MERN Course",
        "completed": true
}


{
        "id": 2,
        "task": "MERN Course",
        "completed": true
}


{
        "id": 3,
        "task": "MERN Course",
        "completed": true
}


Output from  :- GET for To_Do_3 ( get_To_Dos_3 ) For DELETE Checking !    Path :-  http://127.0.0.1:8000/get_To_Dos_3/


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
        "task": "MERN Course",
        "completed": true
    }
]

'''


from .models import To_Do_3

@csrf_exempt
def Delete_To_Do(request, id):

    if request.method == "DELETE":

        try:

             To_Do_Object = get_object_or_404(To_Do_3 , id=id)  # Alternative :- To_Do_3.objects.get(id=id)

             To_Do_Object.delete()
             return JsonResponse({
                 'message' : "To_Do_Object Got Deleted  !"
             })
        except : 
            return JsonResponse({
                'message' : "To_Do_Object Not Found"
            } , status=404)
    return JsonResponse({
        'message' : "Invalid Request"
    } , status=400)



'''

Path :-  http://127.0.0.1:8000/Delete_To_Do/1

Output :- 

{
    "message": "To_Do_Object Got Deleted  !"
}


Checking Output from :- GET for To_Do_3 ( get_To_Dos_3 ) For DELETE Checking !    Path :-  http://127.0.0.1:8000/get_To_Dos_3/


[
    {
        "id": 2,
        "task": "Flask Course",
        "completed": true
    },
    {
        "id": 3,
        "task": "MERN Course",
        "completed": true
    }
]

'''