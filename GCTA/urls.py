from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('HomePage', views.HomePage , name='HomePage'),
    path('Login', views.Login , name='Login'),
    path('Register', views.Register , name='Register'),
    path('RegisterPage', views.RegisterPage , name='RegisterPage'),
    path('Submission', views.Submission , name='Submission'),
    path('Forgotpassword', views.Forgotpassword , name='Forgotpassword'),
    path('Pre_and_post', views.Pre_and_post , name='Pre_and_post'),
    path('Consentpage', views.Consentpage , name='Consentpage'),
    path('Consent', views.Consent , name='Consent'),
    
]

