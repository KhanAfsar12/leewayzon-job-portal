from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse

from django.conf import settings
from .forms import ApplicationForm, EducationFormSet, ExperienceFormSet, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Application, Education, Experience, Job
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
                return render(request, 'login.html')
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
                messages.warning(request, f"You may need to create an account")
                return redirect('register')
            if user_record.is_staff==1 and user_record.is_superuser==0:
                return HttpResponse("You can login through admin panel")
        except Exception as e:
            return redirect('register')
        
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
        application_form = ApplicationForm(request.POST, request.FILES)
        education_formset = EducationFormSet(request.POST, queryset=Education.objects.none())
        experience_formset = ExperienceFormSet(request.POST, queryset=Experience.objects.none())
        if application_form.is_valid() and education_formset.is_valid() and experience_formset.is_valid():

            existing = Application.objects.filter(
                user = request.user,
                job_id = job_id,
            )
            if existing.exists():
                messages.warning(request, "You have already submitted the application for this job.")
                return redirect('dashboard')
            
            application = application_form.save(commit=False)
            application.user_id = request.user.id
            application.job_id = job_id
            application.save()

            for form in education_formset:
                education = form.save(commit=False)
                education.user = request.user
                education.save()


            for form in experience_formset:
                experience = form.save(commit=False)
                experience.user = request.user
                experience.save()
            messages.success(request, "Your Application has been submitted successfully")
            return redirect('dashboard')
    else:
        application_form = ApplicationForm()
        education_formset = EducationFormSet(queryset=Education.objects.none())
        experience_formset = ExperienceFormSet(queryset=Experience.objects.none())

        form = {
            'application_form': application_form,
            'education_formset': education_formset,
            'experience_formset': experience_formset
        }
    return render(request, 'application_form.html', {'form':form})


# For download bio data of particular user
def UserDataView(request, user_id):
    user = get_object_or_404(User, id=user_id)
    applications = Application.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    educations = Education.objects.filter(user=user)
    print(applications, experiences, educations)

    context = {
        'user': user,
        'applications': applications,
        'experiences': experiences,
        'educations': educations
    }
    return render(request, 'user_data.html', context)



def custom_action_view(request):
    # Perform your custom action logic
    return HttpResponse("Custom action performed!")