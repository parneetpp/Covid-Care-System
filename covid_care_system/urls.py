"""covid_care_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    # path('update/', Table, name='update'),
    path('world/', world, name='world'),
    path('india/', india, name='india'),
    path('test/', test, name='test'),
    path('signup/', signuppage, name='signuppage'),
    path('login/', loginpage, name='loginpage'),
    path('logout/', Logout, name='logout'),
    path('home/', Home, name='p_home'),
    path('profile/', profile, name='profile'),
    path('makeappointments/', MakeAppointments, name='makeappointments'),
    path('viewappointments/', viewappointments, name='viewappointments'),
    path('patientdeleteappointments<int:pid>', patient_delete_appointment, name='patientdeleteappointments')
]
