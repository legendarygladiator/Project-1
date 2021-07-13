from django.contrib.auth import login
from django.shortcuts import redirect,render, HttpResponse
# from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from ..forms import StudentSignUpForm
from django.contrib import messages
from PayTm import Checksum
from .models import Orders,Student,Myinfo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

MERCHANT_KEY = 'your_key';


def home(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact-us.html')

def signup(request):
    return render(request, 'home/signup.html')
    
def signupR(request):
    return render(request, 'home/signupR.html')

def training(request):
    return render(request, 'home/trainings.html')




 

   
# def thanks(request):
#     return render(request, 'home/Thanks.html') 


def handelsignupstudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username):
            messages.error(request, 'username already excist')
            return redirect('signup')
        else:
          
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            password1 = request.POST['password1']
            # check for error

            if len(username) > 10:
                messages.error(request, 'username must be under 10 charcter')
                return redirect('signup')
            if password != password1:
                messages.error(request, 'your password did not match, please try again')
                return redirect('signup')
            if not username.isalnum():
                messages.error(request, 'username should be contain letters, number')
                return redirect('signup')

            # create the user
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_student = True 
            myuser.save()
            login(request, myuser)
            messages.success(request, 'Your account successfully created')
            return redirect('/details')

    else:
        return HttpResponse('404 - page not found')




    
def handelsignuprecruiter(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        # check for error

        if len(username) > 10:
            messages.error(request, 'username must be under 10 charcter')
            return redirect('signupR')
        if password != password1:
            messages.error(request, 'your password did not match, please try again')
            return redirect('signupR')
        if not username.isalnum():
            messages.error(request, 'username should be contain letters, number')
            return redirect('signupR')

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_employer = True
        myuser.save()
        messages.success(request, 'Your account successfully created')
        login(request,myuser)
        return redirect('/main')

    else:
        return HttpResponse('404 - page not found')


def handellogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword= request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)


        if user is not None and user.is_student:
            login(request, user)
            
            messages.success(request, 'Successfully logged in')
            return redirect('/')
            
           
        else:
            messages.success(request, 'Sorry no detail found, please try again letter')
            # thank = True
            return redirect('/')

    return HttpResponse('404 - page not found')


def handel_emp_login(request):
    if request.method == 'POST':
        loginusername = request.POST['empusername']
        loginpassword= request.POST['emppassword']
        user = authenticate(username=loginusername, password=loginpassword)

            
        if user is not None and user.is_employer:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('/main')    
        else:
            messages.success(request, 'Sorry no detail found, please try again letter')
        return redirect('home')

    return HttpResponse('404 - page not found')



def handellogout(request):

    logout(request)
    # messages.success(request, 'Sussessfully logged out')
    return redirect('home')


def checkout(request):
   

    if request.method == 'POST':

        amount = request.POST['amount']
        name = request.POST['name']
        
        email = request.POST['email']
        phone = request.POST['phone']
        image = request.FILES['image']


        if len(name)<2 or len(email)<6 or len(phone)<10 :
            messages.error(request, 'Please correct your details')
            return render(request, 'home/checkout.html')
        else:
            order = Orders(amount=amount, name=name,   email=email, phone=phone, 
                           image=image)
            order.save()
            print(order.order_id)
            messages.success(request, 'Thanks for participate here !')






        param_dict = {
            'MID': 'your_id',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'home/paytm.html', {'param_dict': param_dict})

    return render(request, 'home/checkout.html')


    
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i =='CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('unsuccessful' + response_dict['RESPMSG'])

    return render(request, 'home/paymentstatus.html', {'response': response_dict})

@login_required(login_url='/signup')
def studentdetail(request):
    user = request.user

    if request.method == 'POST':
        myuser= user.username 
        fname =user.first_name
        lname = user.last_name
        email = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']
        skills = request.POST['skills']
        qualify = request.POST['qualify']
        country =request.POST['country']
        city   = request.POST['city']
        state  = request.POST['state']
        Iname   = request.POST['Iname']
        zipcode  = request.POST['zip']
        dob  =  request.POST['dob']


        job = Student(users=myuser,institution = Iname,qualification=qualify, state=state,city=city,country=country,last_name=lname, DOB=dob, zipcode=zipcode, first_name=fname, skills=skills , email=email, contact=contact, 
                           address=address)
        job.save()
        return redirect("/")

    return render(request,"home/student.html")


@login_required(login_url='/signup')
def apply_data(request,post_id):

    user=request.user

       



 
    mydata = Student.objects.filter(users=user)[0]
    print(mydata)
     
    myuser= mydata.users 
    fname =mydata.first_name
    lname = mydata.last_name
    email = mydata.email
    address = mydata.address
    contact = mydata.contact
    skills = mydata.skills
    qualify = mydata.qualification
    country =mydata.country
    city   = mydata.city
    state  = mydata.state
    Iname   = mydata.institution
    zipcode  = mydata.zipcode
    dob  =  mydata.DOB
    job_id = post_id   
    data = Myinfo(users=myuser,institution = Iname,qualification=qualify, state=state,city=city,country=country,last_name=lname, DOB=dob, zipcode=zipcode, first_name=fname, skills=skills , email=email, contact=contact, 
                           address=address,job_id=job_id)
    # data = Myinfo(user1=user,job_id=job_id)
    data.save()
    return redirect('/main/fresherjobs/')