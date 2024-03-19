from django.urls import path
from authapp import views


urlpatterns = [
    path("", views.Home, name="Home"),
    path("signup", views.signup, name="signup"),
    path("login", views.handlelogin, name="handlelogin"),
    path("logout", views.handlelogout, name="handlelogout"),
    path("contact", views.contact, name="contact"),
    path("join", views.enroll, name="enroll"),
    path("profile", views.profile, name="profile"),
    path("GALLERY", views.gallery_view, name="GALLERY"),
    path("attendance", views.attendance, name="attendance"),
    path("ABOUT", views.about_view, name="ABOUT"),
    path("SERVICE", views.service_view, name="SERVICE"),
]
