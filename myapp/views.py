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