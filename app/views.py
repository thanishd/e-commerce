from django.http import JsonResponse
from django.shortcuts import render,redirect
from app.models import *
from django.http import HttpResponse
from app.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login Now..!")
            return redirect('/login')
    return render(request,'register.html',{'form':form})

def home(request):
    products=product.objects.filter(trending=1)
    return render(request,'index.html',{'hot':products})

def Cart(request):
    if request.user.is_authenticated:
        Cart=cart.objects.filter(user=request.user)
        return render(request,'Cart.html',{'Carts':Cart})
    else:
        return redirect("/")
    
def remove_fav(request,fid):
    item=favourite.objects.get(id=fid)
    item.delete()
    return redirect('/favviewpage')

def favviewpage(request):
    if request.user.is_authenticated:
        fav=favourite.objects.filter(user=request.user)
        return render(request,'fav.html',{'fav':fav})
    else:
        return redirect("/")

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=product.objects.get(id=product_id)
            if product_status:
                if favourite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favourite'}, status=200)
                else:
                    favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added to Favourite'}, status=200)     
        else:
            return JsonResponse({'status':'Login to Add Favourite'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=product.objects.get(id=product_id)
            if product_status:
                if cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity>=product_qty:
                        cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)
    
def remove_Cart(request,cid):
    Cartitem=cart.objects.get(id=cid)
    Cartitem.delete()
    return redirect('/Cart')


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")

def collection(request):
    Catagory=catagory.objects.filter(status=0)
    return render(request,'collection.html',{'datass':Catagory})

def collectionview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        Products=product.objects.filter(catagory__name=name)
        return render(request,'products/index.html',{'datas':Products,'catagory_name':name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collection')
    
def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            Products=product.objects.filter(name=pname,status=0).first()
            return render(request,'products/product_detail.html',{"products":Products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collection')
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collection')



# Create your views here.


# Create your views here.
