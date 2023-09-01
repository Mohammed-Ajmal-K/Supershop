from django.shortcuts import render,redirect
from superapp.models import categorydb,productdb
from webapp.models import registrationdb,contactdb,cartdb,checkoutdb
from django.contrib import messages


# Create your views here.
def home_pg(req):
    data=categorydb.objects.all()
    return render(req,"Home.html",{'data':data})
def about_us(req):
    return render(req,"About.html")
def contact_us(req):
    return render(req,"Contact.html")
def cat_pg(req):
    data=categorydb.objects.all()
    return render(req,"Category.html",{'data':data})
def prod_pg(req,cat_name):
    prod=productdb.objects.filter(Category=cat_name)
    return render(req,"product.html",{'prod':prod})
def cart_pg(req):
    data=cartdb.objects.filter(Username=req.session['username'])
    return render(req,"cart.html",{"data":data})

def cartsave(request):
    if request.method == "POST":
        unm=request.POST.get("uname")
        pname=request.POST.get("proname")
        ppri=request.POST.get("price")
        pqty=request.POST.get('qty')
        ttl=request.POST.get('total')
        obj=cartdb(Username=unm, ProductName=pname, Quantity=pqty, Price=ppri, Totalprice=ttl)
        obj.save()
        messages.success(request,"Saved Successfully")
    return redirect(cart_pg)

def deletecart(request,cartid):
    cart = cartdb.objects.filter(id=cartid)
    cart.delete()
    messages.success(request, "Deleted Successfully")
    return redirect(cart_pg)

def singleproduct(request,dataid):
    data= productdb.objects.get(id=dataid)
    return render(request,"single_product.html",{"data":data})

def regpage(request):
    return render(request,"reg_page.html")

def savereg(request):
    if request.method=="POST":
        una=request.POST.get("uname")
        ema=request.POST.get("email")
        pas=request.POST.get("password")
        img=request.FILES["image"]

        obj=registrationdb(Uname=una, Email=ema, Password=pas, Image=img)
        obj.save()
        return redirect(regpage)

def Userlogin(request):
    if request.method=="POST":
        usname=request.POST.get("username")
        passw=request.POST.get("password1")
        if registrationdb.objects.filter(Uname=usname, Password=passw).exists():
            request.session['Uname']=usname
            request.session['Password']=passw
            messages.success(request,"Login Successfully")
            return redirect(home_pg)
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect(regpage)
    return redirect(regpage)

def Userlogout(request):
    del request.session['Uname']
    del request.session['Password']
    return redirect(regpage)

def savecontact(request):
    if request.method=="POST":
        na=request.POST.get("name")
        mob=request.POST.get("mobile")
        ema=request.POST.get("email")
        sub=request.POST.get("subject")
        mes=request.POST.get("message")

        obj=contactdb(Name=na, Mobile=mob, Email=ema, Subject=sub, Message=mes)
        obj.save()
        return redirect(contact_us)


def checkout(request):
    return render(request,"Checkout.html")

def checkoutsave(request):
        if request.method == "POST":
            con = request.POST.get("country")
            fna = request.POST.get("fname")
            lna = request.POST.get("lname")
            addr = request.POST.get('address')
            sta = request.POST.get('state')
            zi = request.POST.get('zip')
            ema = request.POST.get('email')
            pho = request.POST.get('phone')
            obj = checkoutdb(Country=con, Fname=fna, Lname=lna, Address=addr, State=sta, Zip=zi, Email=ema, Phone=pho)
            obj.save()
            messages.success(request, "Saved Successfully")
        return redirect(cart_pg)