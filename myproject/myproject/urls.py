"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/<int:id>/', views.usersData.as_view()),
    path('bookmark/', views.bookmarkData.as_view()),
    path('scene_percentage/', views.scene_percentageData.as_view()),
    path('scene_percentage/<int:user_id>/', views.readScene_Percentage_By_user_idData.as_view()),
    path('understood/', views.understoodData.as_view()),
    path('not_understood/', views.not_understoodData.as_view()),
    path('scene/', views.sceneData.as_view()),
    path('scene/<int:lvl>/', views.readScene_By_LevelData.as_view()),
    path('recommendation/', views.recommendationData.as_view()),
    path('words/', views.wordData.as_view()),
    path('words/<int:scene_id>/', views.readWord_By_Scene_idData.as_view()),
]
