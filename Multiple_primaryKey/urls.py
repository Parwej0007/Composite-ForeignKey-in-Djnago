"""Multiple_primaryKey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from PkApp.views import OrgListCreate, OrgRetrieveUpdate, \
    SeqListCreate, SeqRetrieveUpdate, \
    OrgSubdomListCreate, OrgSubdomRetrieveUpdate, \
    AuthListCreate, AuthRetrieveUpdate


urlpatterns = [
    path('admin/', admin.site.urls),

    path('OrgList/', OrgListCreate.as_view()),
    path('OrgUpdate/<str:pk>/', OrgRetrieveUpdate.as_view()),

    path('SeqList/', SeqListCreate.as_view()),
    path('SeqUpdate/<str:org_code>/<str:seq_num>/<str:seq_type>/', SeqRetrieveUpdate.as_view()),

    path('OrgSubdomList/', OrgSubdomListCreate.as_view()),
    path('OrgSubdomUpdate/<str:org_code>/<str:org_dom>/<str:org_subdom>/', OrgSubdomRetrieveUpdate.as_view()),

    path('AuthList/', AuthListCreate.as_view()),
    path('AuthUpdate/<str:org_code>/<str:org_dom>/<str:org_subdom>/<int:org_seq>/', AuthRetrieveUpdate.as_view()),

    # path('UpdateStudent/<int:roll>/<str:branch>/', UpdateStudent.as_view()),
    # path('TeacherList/', ListCreateTeacher.as_view()),
    # path('UpdateTeacher/<int:pk>/', UpdateTeacher.as_view())
]
