from django.urls import path 
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact, name="contact"),
    path("viewbook/",views.view_book, name="viewbook"),
    path("addbook/",views.add_book, name="addbook"),
    path("updatebook/<int:id>",views.update_book, name="updatebook"),
    path("deletebook/<int:id>",views.delete_book, name="deletebook"),
    path("register/",views.register, name="register"),
    path("login/",views.login_form,name="login"),
    path("logout/",views.logout_form,name="logout"),
    path("viewcart/",views.view_cart,name="viewcart"),
    path("addcart/<int:book_id>",views.add_to_cart,name="addcart"),
    path("deletecart/<int:id>",views.delete_from_cart,name="deletecart"),
    path("clearcart",views.clear_cart,name="clearcart"),
    path("payment/<int:book_id>",views.buy_now,name="payment"),
    path("success",views.payment_success,name="success"),
    path('buy-all/',views.buy_all,name='buy-all')
  

    
    
    
    
    
    
    
]
