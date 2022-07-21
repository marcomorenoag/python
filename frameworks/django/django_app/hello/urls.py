from django.urls import path
from .views import *
from .models import LogMessage

home_list_view = HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", hello_there, name="hello_there"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("log/", log_message, name="log"),
]
