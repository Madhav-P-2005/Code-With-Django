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
    path('add-and-get/', views.add_and_get_items),     # Path :-  http://127.0.0.1:8000/add-and-get/


    path('add-todo/' , views.add_todo, name='add_todo'),


    path('add-category/', views.add_category, name='add_category'),    # Path :- http://127.0.0.1:8000/add-category/
    path('add-todo-with-category/', views.add_todo_with_category, name='add_todo_with_category'),   # Path :-  http://127.0.0.1:8000/add-todo-with-category/


    path('add_To_Do_2',views.add_To_Do_2 , name='add_To_Do_2'),      # Path :-  


    # path('add_To_Do_3/', views.add_To_Do_3, name='add_To_Do_3'),                  # Path :-  http://127.0.0.1:8000/add_To_Do_3/,

    # path('get_To_Dos_3/', views.get_To_Dos_3, name='get_To_Dos_3'),                  # Path :- http://127.0.0.1:8000/get_To_Dos_3/,

    #  Retrieving a Single Record by ID
    # path('get_To_Dos_3/<int:id>/', views.get_To_Dos_3, name='get_To_Dos_3'),                  # Path :- http://127.0.0.1:8000/get_To_Dos_3/4/

    # path('get_completed_3/', views.get_completed_3, name='get_completed_3'),               # Path :- http://127.0.0.1:8000/get_completed_3/

    # path('get_filtered_To_Do_3/' , views.get_filtered_To_Do_3, name='get_filtered_To_Do_3'),

    path('preload/' , views.preload ,name = 'preload'),  # Path :- http://localhost:8000/preload/

    path('ToDos_preload/filter/' , views.get_todos_by_category_and_tag, name="get_todos_by_category_and_tag"),    # Path :- http://localhost:8000/ToDos_preload/filter/?category_preload=Home&tag_preload=Urgent
]


'''

⭐) Configuring Django to Use the Custom View

'''

# handler404 = 'myapp.views.custom_404'