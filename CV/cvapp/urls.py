from django.urls import path, include
from .views  import authView, home,view_cv

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),
    path("view_cv/<int:cv_id>", view_cv, name="view_cv"),
]
