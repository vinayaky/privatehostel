from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from home.models import Profile,onlyimages,Contact
from datetime import datetime
from django import forms
from django.contrib import messages


images=Profile

def index(request):
    us=request.user.is_anonymous
    data=images.objects.all()   
    if request.method=="GET":
        s=request.GET.get('search')
        if s!=None:
            data=images.objects.filter(name__icontains=s) 
    id={'uid':us,'Data':data}
    return render(request,'index.html',id)


def loginpage(request):
    us=request.user.is_anonymous
    id={'uid':us}

    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

  

    return render(request,'login.html')


def about(request):
    us=request.user.is_anonymous
    id={'uid':us}
    return render(request,'about.html',id)


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')



def Logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    us=request.user.is_anonymous
    id={'uid':us}
    return render(request,'upload.html',id)

def detail(request,pid,pid2):
    detail=onlyimages.objects.filter(name=pid)
    biodet=images.objects.filter(name=pid,uid=pid2)[0]
    
    us=request.user.is_anonymous
    print( 'single share: '+ pid)
    id={'uid':us,'detail':detail,'bio':biodet}
    return render(request,'detail.html',id)
   

def contactUs(request):
    us=request.user.is_anonymous
    id={'uid':us}  
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact =Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

        return redirect('home')


    return render(request,'contact.html',id)


def upload(request):
    us=request.user.is_anonymous
    userconf={'uid':us}
 
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        address= request.POST.get('address')
        singles='single sharing prize: ' + request.POST.get('singles')
        twos='double sharing prize: ' + request.POST.get('twos')
        threes='triple sharing prize: ' + request.POST.get('threes')
        fours='four sharing prize: ' + request.POST.get('fours')
        number=request.POST.get('number')
        uid=request.user.username
        occupancy='Occupancy Type: ' + request.POST.get('occupancy')
       
        image=None
        imag=request.FILES.getlist('image') 
        print(name,imag)
        for img in imag:
            image=img
            a= onlyimages(name=name,imagepname=uid,image=img)
            a.save()
            
        data=images(occupancy=occupancy,uid=uid,image=image,number=number,name=name,desc=desc,address=address,singles=singles,twos=twos,threes=threes,fours=fours)     
        data.save()    
        messages.success(request, "Profile details uploaded.")  
        return redirect('home')
    
    return render(request,'upload.html',userconf)

