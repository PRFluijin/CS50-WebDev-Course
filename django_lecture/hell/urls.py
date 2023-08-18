from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rob", views.rob, name="rob"),
    path("<str:name>", views.greet, name="greet")
]

