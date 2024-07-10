"""
URL configuration for job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import include, path
from auth_job import views as user_views
from django.contrib.auth import views as authentication_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('dashboard')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("auth_job.urls")),
    path('register/', user_views.register, name='register'),
    # path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('login/', user_views.login_view, name='login')
]
