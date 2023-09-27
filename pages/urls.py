from django.urls import path
from .views import HomePageView, AboutPageView, QuiltPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("quilt/", QuiltPageView.as_view(), name="quilt"),
    path("", HomePageView.as_view(), name="home"),
]
