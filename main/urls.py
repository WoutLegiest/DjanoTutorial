from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # Ervoor zorgen dat zowel register en register/ werkt
    url(r'^register', views.register, name="register"),
    url(r'^login', views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("<single_slug>", views.single_slug, name="single_slug"),
]