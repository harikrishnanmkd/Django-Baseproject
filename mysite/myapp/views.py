from django.shortcuts import render,redirect,get_object_or_404

from .forms import BookForm,UserRegistrationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from.models import Book,Cart
import stripe
from django.conf import settings
from django.urls import reverse


stripe.api_key=settings.STRIPE_SECRET_KEY



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
@login_required
def view_book(request):
    data=Book.objects.all()
    return render(request,"viewbook.html",{'a':data})
@login_required
def add_book(request):
    data=BookForm(request.POST or None,request.FILES or None)
    if data.is_valid():
        data.save()
        return redirect('viewbook')
    return render(request,"addbook.html",{'ab':data})
@login_required
def update_book(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES or None,instance=book)
    if form.is_valid():
        form.save()
        return redirect('viewbook')
    return render(request,"updatebook.html",{'ab':form})
@login_required
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


def login_form(request):
    form=UserLoginForm(request,data=request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.get_user()
        login(request,user)
        return redirect('viewbook')
    return render(request,'login.html',{"form":form})

def logout_form(request):
    logout(request)
    return redirect("home")

@login_required
def view_cart(request):
    cart_item=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cart_item:
        total_price+= item.book.price*item.quantity
    return render(request,'viewcart.html',{"cart":cart_item,"total_price":total_price})

    
def add_to_cart(request,book_id):
    book=Book.objects.get(id=book_id)
    cart_item, created=Cart.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect("viewcart")

def delete_from_cart(request,id):
    cart_item=Cart.objects.get(id=id,user=request.user)
    if request.method=="POST":
        if cart_item.quantity>1:
            cart_item.quantity-=1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('viewcart')
    
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect('viewcart')


def buy_now(request, book_id):
    cart_item = get_object_or_404(Cart, user=request.user, id=book_id)
    book = cart_item.book
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': book.title,
                },
                'unit_amount': int(float(book.price) * 100),
            },
            'quantity': cart_item.quantity,
        }],
        mode="payment",

        # ✅ send cart_id
        success_url=request.build_absolute_uri(reverse('success')) + f"?cart_id={cart_item.id}",

        cancel_url=request.build_absolute_uri(reverse('viewcart')),
    )
    return redirect(session.url)



def buy_all(request):
    cart_items = Cart.objects.filter(user=request.user)

    line_items = []

    for item in cart_items:
        book = item.book

        line_items.append({
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': book.title,
                },
                'unit_amount': int(float(book.price) * 100),
            },
            'quantity': item.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',

        # ✅ send flag
        success_url=request.build_absolute_uri(reverse('success')) + "?buy_all=1",

        cancel_url=request.build_absolute_uri(reverse('viewcart')),
    )

    return redirect(session.url)

def payment_success(request):

    cart_id = request.GET.get("cart_id")
    buy_all = request.GET.get("buy_all")

    if cart_id:
        # delete only that purchased item
        Cart.objects.filter(id=cart_id, user=request.user).delete()

    elif buy_all:
        # delete entire cart
        Cart.objects.filter(user=request.user).delete()

    return render(request, "success.html")

def payment_cancel(request):
    return render(request,"viewcart.html")

    
    
    


    






