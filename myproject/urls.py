from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path('', views.home , name='home'),
]


'''

 This works — BUT it's only fine for small projects or beginners.

 BETTER (Scalable) Approach :-  Use include()
This is the recommended and scalable approach used by all pro Django developers :- 

'''

from django.contrib import admin
from django.urls import path, include


'''

⭐) Updating URL Patterns 

Djano-Learning/myproject/urls.py 

'''

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , include('myapp.urls')),

    path('json/' , views.json_view, name='json_view'),     # Path :- http://127.0.0.1:8000/json/

    # This code sets up a URL pattern that captures the user's name and passes it to the user_view.
    # path('user/<str:name>/' , views.user_view , name='user_view'),


    # With this, when a user navigates to http://127.0.0.1:3000/search/?q=python, they will see the message You searched for: python, since the query parameter q=python is passed to the view.
    path('search/', views.search_view , name='search_view'),


    # URL Configuration :-  The URL /get-items/ is mapped to the get_items view and can be accessed to see the items.
    path('get-items/' , views.get_items , name = 'get-items'),      # Path :-  http://127.0.0.1:8000/get-items/

    
    # The urls.py file contains the URL patterns that map to the views. This is how we direct web requests to the correct view function.
    path('add-and-get/', views.add_and_get_items)     # Path :-  http://127.0.0.1:8000/add-and-get/
]


'''

⭐) Configuring Django to Use the Custom View

'''

# handler404 = 'myapp.views.custom_404'