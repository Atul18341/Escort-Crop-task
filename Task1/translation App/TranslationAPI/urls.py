from django.urls import path
from . import views
urlpatterns = [
   path('',views.Translation.as_view()),
]