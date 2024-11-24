from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.models import *
# Create your views here.

def index(request):
    res=tbl_event.objects.all()
    return render(request,"index_1.html",{"res":res})

def full_view_event(request,id):
    res=tbl_event.objects.get(id=id)
    return render(request,"full_view.html",{"obj":res})

def admin_login(request):
    res=tbl_event.objects.all()
    return render(request,"admin_login.html",{"res":res})

def admin_login_data(request):
    if(request.method == "POST"):
        user=request.POST["username"]
        pas=request.POST["pas"]
        print(user,pas)
        if user == "admin" and pas == "admin":
            request.session['admin']=user
            return HttpResponseRedirect("/admin_login_success")
        else:
            return HttpResponseRedirect("/admin_login")
    else:
        return HttpResponseRedirect("/")
    

def admin_login_success(request):
    if(request.session.has_key('admin')):
        return render(request,"admin_layout_1.html")
    else:
        return HttpResponseRedirect("/admin_login")
    
def admin_logout(request):
    if(request.session.has_key('admin')):
        del request.session['admin']
        return HttpResponseRedirect("/admin_login")
    else:
        return HttpResponseRedirect("/admin_login")
    
def post_event(request):
    if request.session.has_key('admin'):
        return render(request,"post_event.html")
    else:
        return HttpResponseRedirect("/admin_login")
    
def post_event_data(request):
    if request.method == "POST":
        id=request.POST["id"]
        name=request.POST["event_name"]
        date=request.POST["event_date"]
        des=request.POST["description"]
        img=request.FILES["img"]
        venue=request.POST["venue"]
        time=request.POST["time"]
        guest_pic=request.FILES["guest_pic"]
        guest_name=request.POST["guest_name"]
        if id == "null":
            res=tbl_event()
        else:
            res=tbl_event.objects.get(id=id)
        res.event_name=name
        res.event_date=date
        res.description=des
        res.image=img
        res.venue=venue
        res.event_time=time
        res.guest_profile=guest_pic
        res.guest_name=guest_name
        res.save()
        if id == "null":
            print("data saved")
            return HttpResponseRedirect("/post_event")
        else:
            print("data updated")
            return HttpResponseRedirect("/view_event")
        
    

def view_event(request):
    if request.session.has_key('admin'):
        res=tbl_event.objects.all()
        return render(request,"view_events.html",{"res":res})
    else:
        return HttpResponseRedirect("/")
    
def event_delete(request,id):
    res=tbl_event.objects.get(id=id)
    res.delete()
    return HttpResponseRedirect("/view_event")

def admin_view_feedback(request):
    res=tbl_feedback.objects.all()
    return render(request,"view_feedback.html",{"res":res})


# ******************************user**************************************

def user_register(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST["name"]
        college=request.POST["college"]
        course=request.POST["course"]
        department=request.POST["department"]
        phone_number=request.POST["phone_number"]
        email=request.POST["email"]
        regno=request.POST["regno"]
        Password=request.POST["Password"]
        obj=tbl_event.objects.get(id=id)
        res=tbl_student()
        res.name=name
        res.college=college
        res.course=course
        res.department=department
        res.phone_number=phone_number
        res.email=email
        res.regno=regno
        res.ref_event=obj
        res.password=Password
        res.save()
        return HttpResponseRedirect("/")
    
def login_check(request):
    if request.method == "POST":
        user=request.POST["username"]
        pas=request.POST["pas"]
        if tbl_student.objects.filter(email=user,password=pas).exists():
            print("test1")
            request.session['user']=user
            return HttpResponseRedirect("/user_login_success")
        else:
            return HttpResponseRedirect("/")
        
def user_login_success(request):
    if request.session.has_key('user'):
        return render(request,"user_layout.html")
    else:
        return HttpResponseRedirect("/")
    
def student_register(request,id):
    res=tbl_event.objects.get(id=id)
    return render(request,"register.html",{"res":res})

def user_logout(request):
    if request.session.has_key('user'):
        del request.session['user']
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
    
def feeback_menu(request):
    if request.session.has_key('user'):
        user=request.session['user']
        res=tbl_student.objects.filter(email=user)
        return render(request,"menu_feedback.html",{"res":res})
    else:
        return HttpResponseRedirect("/")
    
def feeback_data(request,id):
    if request.session.has_key('user'):
        res=tbl_student.objects.get(id=id)
        return render(request,"rate_us.html",{"res":res})
    else:
        return HttpResponseRedirect("/")
    
def rating_data(request):
    if request.method == "POST":
        id=request.POST["id"]
        des=request.POST["description"]
        star=request.POST["star"]
        print(id,star,des)
        obj=tbl_student.objects.get(id=id)
        obj_1=tbl_event.objects.get(id=obj.ref_event.id)
        res=tbl_feedback()
        res.star=star
        res.description=des
        res.ref_student=obj
        res.ref_event=obj_1
        res.save()
        return HttpResponseRedirect("/user_login_success")

