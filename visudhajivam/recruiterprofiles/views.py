from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from.models import Mypostjob
from home.models import User,Myinfo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/signupR')
def orgnize(request):
     if request.method == 'POST':
        user = request.user
        position = request.POST['position']
        company = request.POST['company']
        experience = request.POST['exp']
        package = request.POST['package']
        location = request.POST['location']
        skill = request.POST['skill']
        desc = request.POST['desc']
       

        post = Mypostjob(user=user,position=position,company=company,experience=experience,package=package,location=location,
        skill=skill,desc=desc)
        post.save()

        return redirect('/main/fresherjobs')


     return render(request, 'recruiterprofiles/post_internship.html')



def fresherjob(request):
    mypost = Mypostjob.objects.all()
   
    return render(request,'recruiterprofiles/fresherjob.html',{'mypost':mypost})   


def job_details(request,post_id):
    mypost1 = Mypostjob.objects.filter(post_id=post_id)[0]
    print(mypost1)
   
    return render(request,'recruiterprofiles/job_details.html',{'mypost1':mypost1})      




@login_required(login_url='/signupR')
def myjob(request):
    jobs = Mypostjob.objects.filter(user=request.user)
    

    return render(request,'recruiterprofiles/myjob.html',{'jobs':jobs})



    



@login_required(login_url='/signupR')
def view_applies(request,post_id):
    info = Myinfo.objects.filter(job_id=post_id)
    
    
   
    return render(request,'recruiterprofiles/main.html',{'info':info})



