from django.urls import path
from . import views
urlpatterns = [
   path('',views.AccountLedgerView.as_view()),
]