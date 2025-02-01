from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("login/password/", views.verify_code, name="verify_code"),
    path("logout/", views.logout_user, name="logout"),
]
