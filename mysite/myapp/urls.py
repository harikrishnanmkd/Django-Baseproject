from django.urls import path 
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact, name="contact"),
    path("viewbook/",views.view_book, name="viewbook"),
    path("addbook/",views.add_book, name="addbook"),
    path("updatebook/<int:id>",views.update_book, name="updatebook"),
    path("deletebook/<int:id>",views.delete_book, name="deletebook")
]