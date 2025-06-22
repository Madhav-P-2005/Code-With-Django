# from django.contrib import admin
# from django.urls import path
# from myapp import views 

# urlpatterns = [
#     path('', views.home , name='home'),
# ]


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
    path('user/<str:name>/' , views.user_view , name='user_view'),


    # With this, when a user navigates to http://127.0.0.1:3000/search/?q=python, they will see the message You searched for: python, since the query parameter q=python is passed to the view.
    path('search/', views.search_view , name='search_view')
]