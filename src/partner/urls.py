from django.urls import path, re_path, include
from . import views

app_name = "partner"

urlpatterns = [
    # Partner urls
    re_path(r'^$', views.signup, name="signup"),
]