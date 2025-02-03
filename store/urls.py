from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("login/password/", views.verify_code, name="verify_code"),
    path("logout/", views.logout_user, name="logout"),
    path("page/terms/", views.terms, name="terms"),
    path("page/privacy/", views.privacy, name="privacy"),
    # register new users
    path("register/", views.register_user, name="register"),
]
