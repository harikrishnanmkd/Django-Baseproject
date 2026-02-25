from django.shortcuts import render,redirect

from .forms import BookForm,UserRegistrationForm
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

def add_book(request):
    data=BookForm(request.POST or None,request.FILES or None)
    if data.is_valid():
        data.save()
        return redirect('viewbook')
    return render(request,"addbook.html",{'ab':data})

def update_book(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES or None,instance=book)
    if form.is_valid():
        form.save()
        return redirect('viewbook')
    return render(request,"updatebook.html",{'ab':form})

def delete_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=="POST":
        book.delete()
        return redirect('viewbook')
    # return render(request,"deletebook.html",{'ab':book})
    
def register(request):
    form=UserRegistrationForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        form.save()
        return redirect("viewbook")
    return render(request,'register.html',{"form":form})

    

    
    


    






