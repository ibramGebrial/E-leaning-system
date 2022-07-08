from django.urls import path
from . import views


urlpatterns = [
    path('profile/<str:pk>/', views.profiles, name="profiles"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.message, name="message"),
    path('send-message/<str:pk>/', views.sendMessage, name="send-message"),
]
