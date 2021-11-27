from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('HomePage', views.HomePage , name='HomePage'),
    path('RegisterPage', views.RegisterPage , name='RegisterPage'),
    path('Submission', views.Submission , name='Submission'),
    path('Forgotpassword', views.Forgotpassword , name='Forgotpassword'),
    path('Consent', views.Consent , name='Consent'),
    path('Pre_and_post', views.Pre_and_post , name='Pre_and_post'),
]

