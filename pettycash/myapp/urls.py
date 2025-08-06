
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('submit/', submit_expense, name='submit_expense'),
    path('expenses/', expense_list, name='expense_list'),
    path('summary/', petty_cash_summary, name='petty_cash_summary'),

   
]