from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import user,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def HomePage(request):
    return render(request,'HomePage.html')

def RegisterPage(request):
    # if request.method=='post':
    #     full_name=request.post['full_name ']
    #     identyfy=request.post['identyfy ']
    #     age=request.post['age ']
    #     country=request.post['country']
    #     email=request.post['email']
    #     cnt_num=request.post['cnt_num']
    #     tuberculosi=request.post['tuberculosi']
    #     person=request.post['person']
    #     Organisational=request.post['Organisational']
    #     narrative=request.post['narrative']
    #     training=request.post['training'] 

    #     user=user.objects.crea
# else:
    return render(request,'RegisterPage.html')

def Submission(request):
    return render(request,'Submission.html')

def Forgotpassword(request):
    return render(request,'forgotpassword.html')

def Consent(request): 
    return render(request,'Consent.html')

def Pre_and_post(request): 
    return render(request,'Pre_and_post.html')   