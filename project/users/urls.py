from django.urls import path
from .views import SignUpView, login_user, logout_user, register_user

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login_user/', login_user, name='login-user'),
    path('logout_user/', logout_user, name='logout-user'),
    path('register/', register_user, name='register'),
]
