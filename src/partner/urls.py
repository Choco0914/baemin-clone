from django.urls import path, re_path, include
from . import views

app_name = "partner"

urlpatterns = [
    # Partner urls
    re_path(r'^$', views.index, name="index"),
    re_path(r'^login/$', views.login, name="login"),
    re_path(r'^signup/$', views.signup, name="signup"),
    re_path(r'^logout/$', views.logout_view, name="logout"),
]