"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('',views.index,name='index'),
    path('todo/<int:id>', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('video/', views.video, name='video'),
    path('Resetvideo/', views.Resetvideo, name='Resetvideo'),
    path('completed/', views.completed, name='completed'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('completed/<int:id>', views.completed_by_id, name='completed_by_id'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


