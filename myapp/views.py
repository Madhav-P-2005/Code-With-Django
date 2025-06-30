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