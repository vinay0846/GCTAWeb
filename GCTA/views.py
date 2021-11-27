from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.session.has_key('username'):
        # username = request.session['username']
        return redirect('HomePage')
    else:
      return render(request,'index.html')

def Login(request):
    if request.method == 'GET':
        UserId = request.GET['userid']
        request.session['username'] = UserId
        return HttpResponse('success')

def HomePage(request):
        # username = request.session['username']
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