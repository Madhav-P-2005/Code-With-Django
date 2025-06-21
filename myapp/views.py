'''

⭐) Create your views here.

myapp/views.py

'''


# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hello , world')


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


from django.http import JsonResponse

def json_view(request):
    return JsonResponse({
        'message' : 'Hello , JSON !',
        'status' : 'Success',
        'code' : 200
    })