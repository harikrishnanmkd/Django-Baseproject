from django.shortcuts import render
from.models import Book
# from django.http import HttpResponse

# def home(request):
#     data={
#        'Name':"Hari",
#         'Age':24,
#         'Place':"Mannarkkad"
#     }
#     return render(request,"home.html",data)
def home(request):
    data=["Python","Html","java","C++"]
    return render(request,"home.html",{'a':data})


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def view_book(request):
    data=Book.objects.all()
    return render(request,"viewbook.html",{'a':data})






