from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage),
    path('login', views.login_user),
    path('signup', views.signup_user),
    path('logout', views.logout_user),

]