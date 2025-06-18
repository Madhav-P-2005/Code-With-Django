# from django.contrib import admin
# from django.urls import path
# from myapp import views 

# urlpatterns = [
#     path('', views.home , name='home'),
# ]


'''

✅ This works — BUT it's only fine for small projects or beginners.

🔁 ✅ BETTER (Scalable) Approach: Use include()
This is the recommended and scalable approach used by all pro Django developers :- 

'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('myapp.urls')),
]