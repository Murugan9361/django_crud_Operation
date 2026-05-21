from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name="login"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_page,name="logout"),
]
