"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include

from students import views

from rest_framework.routers import DefaultRouter

from students.api import StudentsViewset
from bakugan_tournaments.api import TournamentViewset, GameViewset, ParticipantsViewset, ApplicationViewset

router = DefaultRouter()
router.register("students", StudentsViewset, basename="students")
router.register("tournaments", TournamentViewset, basename="tournaments")
router.register("games", GameViewset, basename="games")
router.register("participants", ParticipantsViewset, basename="participants_in_game")
router.register("applications", ApplicationViewset, basename="applications")

urlpatterns = [
    path('', views.ShowStudentsView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
