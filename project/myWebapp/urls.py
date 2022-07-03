from django.contrib import admin
from django.urls import path
from .views import home
from .views import display
from .views import update
from .views import delete

urlpatterns = [
    path('', home),
    path('all/', display),
    path('update/', update),
    path('delete/', delete),
    path('admin/', admin.site.urls),
]