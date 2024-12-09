from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from.models import *
import razorpay
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG','oXUZ9Mf5zhjoZsTFLc7RpABO'))

def index(request):
    return render(request, 'index.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def check_adminlogin(request):
    if request.method=="POST":
        username=request.POSt.get("username")
        password=request.POT.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/admin_homepage/")
        else:
            return redirect("/adminlogin/")
        
def admin_homepage(request):
    book=tbl_book.objects.all()
    return render(request, "admin_homepage.html", {"book":book})

def savebook(request):
    if request.method == "POST":
        object=tbl_book()
        object.title=request.POST.get("title")
        object.author=request.POST.get("author")
        object.genre=request.POST.get("genre")
        object.price=request.POST.get("price")
        object.published_date=request.POST.get("published_date")
        object.save()
        return redirect("/admin_homepage/")
      
def editbook(request,id):
    edit=tbl_book.objects.get(id=id)
    return render(request,'editbook.html',{"edit":edit})

def updatebook(request,id):
    update=tbl_book.objects.get(id=id)
    update.title=request.POST.get("title")
    update.author=request.POST.get("author")
    update.genre=request.POST.get("genre")
    update.price=request.POST.get("price")
    update.published_date=request.POST.get("published_date")
    update.save()
    return redirect('/admin_homepage/')

def deletebook(request,id):
    delete=tbl_book.objects.get(id=id)
    delete.title=request.POST.get('title')
    delete.author=request.POST.get('author')
    delete.genre=request.POST.get('genre',)
    delete.price=request.POST.get('price')
    delete.published_date=request.POST.get('published_date')
    
    delete.delete()
    return redirect('/admin_homepage/')


def availablebooks(request):
    books = tbl_book.objects.all()  # Retrieve all book records from the database
    return render(request, "availablebooks.html", {'books': books})

def addtocart(request):
    return render(request, 'addtocart.html')
def addreview(request,id):
    try:
        if(request.session['user']):
            book=tbl_book.objects.get(id=id)
            return render(request, 'addreview.html', {'book':book})
    except:
        return redirect('/cuslogin/')
        
    
def loginpage(request):
    return render(request, 'loginpage.html')
    
def cusregistrations(request):
    return render(request, 'cusregistration.html')

def savecus(request):
    if request.method == "POST":
        object=customer_reg()
        object.name=request.POST.get("name")
        object.email=request.POST.get("email")
        object.number=request.POST.get("number")
        object.password=request.POST.get("password")
        object.save()
    return redirect("/cusregistration/")

def cuslogin(request):
    return render(request, 'cuslogin.html')


def cuslogin_check(request):
    name=request.POST.get("name")
    password=request.POST.get("password")
    if customer_reg.objects.filter(name=name, password=password).exists():
        cus=customer_reg.objects.get(name=name, password=password)
        request.session['user'] = cus.id
        return redirect('/')
    else:
        return HttpResponse('invalid date')
    
def save_reviews(request,id):
    if request.method == "POST":
        object=tbl_review()
        object.name=request.POST.get("name")
        object.email=request.POST.get("email")
        object.rating=request.POST.get("rating")
        object.review=request.POST.get("review")
        object.book_id=id
        object.save()
        return redirect("/")
    
def viewreviews(request,id): #
    b=tbl_book.objects.get(id=id)
    review=tbl_review.objects.filter(book=id)
    return render(request,'viewreviews.html' ,{"review":review,"b":b}) 

def addtocart(request,id):
    cart=tbl_cart()
    cart.book_id=id
    if not request.session.session_key:
        request.session.create()
    session_key=request.session.session_key
    cart.sessions_key=session_key
    cart.save() 
    return redirect('/cart/')

def cart(request):
    cartdata=tbl_cart.objects.filter(sessions_key=request.session.session_key) 
    total=sum(i.book.price for i in cartdata)
    return render(request, 'cart.html' , {'cartdata': cartdata,"total":total}) 

def cartdetete(request, id):
    cdelete = tbl_cart.objects.get(id=id)  # Get the cart item by ID
    cdelete.delete()  # Delete the cart item
    return redirect('cart')  # Redirect to the cart view

def checkout(request):
    cartdata=tbl_cart.objects.filter(sessions_key=request.session.session_key) 
    total=sum(i.book.price for i in cartdata)
    currency = 'INR'
    amount = int(total) * 100
    razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'savebill'
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url  
    return render(request, 'checkoutpage.html',context)

def savebill(request):
    if request.method == "POST":
        object = tbl_billing()
        cartdata = tbl_cart.objects.filter(sessions_key=request.session.session_key)
        total = sum(i.book.price for i in cartdata)
        object.full_name = request.POST.get("full_name")
        object.email = request.POST.get("email")
        object.address = request.POST.get("address")
        object.city = request.POST.get("city")
        object.state = request.POST.get("state")
        object.zip_code = request.POST.get("zipcode")
        object.save()

        razorpay_order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        # Verify the payment signature
        amount = int(total) * 100  # Amount in paise
        razorpay_client.payment.capture(payment_id, amount)

        # Send confirmation email
        subject = 'Payment Confirmation'
        message = f'Thank you for your purchase, {object.full_name}!\n\nYour payment was successful.\n\nOrder Details:\nFull Name: {object.full_name}\nEmail: {object.email}\nAddress: {object.address}\nCity: {object.city}\nState: {object.state}\nZip Code: {object.zip_code}\nTotal Amount: ₹{total}\n\nRegards,\nBookstall Team'
        recipient_list = [object.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        return redirect("/")

    return redirect("/")

def order(request):
    return render(request, 'order.html')
  
from django.shortcuts import render
from .models import tbl_billing

def billing_details(request):
    billing_data = tbl_billing.objects.all()  # Retrieve all billing details
    return render(request, 'billing_details.html', {'billing_data': billing_data})
