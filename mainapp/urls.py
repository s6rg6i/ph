from django.urls import path

from mainapp.views import HelloWorldView, hello_world

urlpatterns = [
    path("", hello_world),
    path("class/", HelloWorldView.as_view()),
]
