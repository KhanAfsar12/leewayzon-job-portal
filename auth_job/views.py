from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse

from django.conf import settings
from .forms import ApplicationForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Application, Job
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages




# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print(username, email)
        
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.warning(request, f"User {username} already exists. Please login")
                print("/////////////////////////////")
                return redirect('login')
            else:
                form.save()
                messages.success(request, f"Welcome {username}, Your Account Is Created Successfully")
                return render(request, 'login.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        if not (username and password):
            return HttpResponse("User credentials are required!")

        try:
            user_record = User.objects.filter(username=username).first()
            if not user_record:
                return HttpResponse("User not found")
            if user_record.is_staff==1 and user_record.is_superuser==0:
                return HttpResponse("You can login through admin panel")
        except Exception as e:
            return render(request, "signup.html")
        
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            request.session.set_expiry(settings.SESSION_COOKIE_AGE) 
            request.session['user_id'] = user.id
            print(request.session['user_id'])
            # return render(request, 'dashboard.html', {"user": user})
            # return redirect('dashboard')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return HttpResponse("Invalid email or password")

    return render(request, 'login.html')




def jobsView(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs':jobs})



def description(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    request.session['job_id'] = job_id
    return render(request, 'job_desc.html', {'job':job})



def apply(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return render(request, 'login.html')
    return render(request, 'apply_job.html')



@login_required
def application_view(request):
    if 'job_id' in request.session:
        job_id = request.session['job_id']
    else:
        job_id = None

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            existing = Application.objects.filter(
                user = request.user,
                job_id = job_id,
                # email = form.cleaned_data['email']     if user want to send application of another person through their account.
            )
            if existing.exists():
                messages.warning(request, "You have already submitted the application for this job.")
                return redirect('dashboard')
            
            application = form.save(commit=False)
            application.user_id = request.user.id
            application.job_id = job_id
            application.save()
            messages.success(request, "Your Application has been submitted successfully")
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form':form})





