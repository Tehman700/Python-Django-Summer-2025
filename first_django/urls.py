from django.contrib import admin
from django.urls import path, include



# URL ROUTING FILES
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
