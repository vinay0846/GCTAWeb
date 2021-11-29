from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import Registration

# Create your views here.
def index(request):
    if request.session.has_key('username'):
        # username = request.session['username']
        return redirect('HomePage')
    else:
      return render(request,'index.html')

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        UserId = request.POST['userid']
        request.session['username'] = UserId
        return HttpResponse('success')

def HomePage(request):
        # username = request.session['username']
    return render(request,'HomePage.html')

def RegisterPage(request):
    return render(request,'RegisterPage.html')

@csrf_exempt
def Register(request):
    if request.method == 'POST':
                
        fld_full_name = request.POST['txtfull_name']
        fld_i_identify_as_id = "1"
        fld_i_identify_as_name =request.POST['txtidentyfy']
        fld_age = request.POST['txtage']
        fld_country_of_residence = request.POST['txtcountry']
        fld_email = request.POST['txtemail']
        fld_telephone_number = request.POST['txtcnt_num']
        fld_tuberculosis_id = "1"
        fld_tuberculosis_name = request.POST['txttuberculosi']
        fld_am_person_id= "1"
        fld_am_person_name = request.POST['txtperson']
        fld_organizational_affiliations = request.POST['txtOrganisational']
        fld_working_with_TB_HIV = request.POST['txtnarrative']
        fld_part_of_this_training = request.POST['txttraining']
        fld_logged_in_user_id =''
        fld_data_source ='W'
        fld_form_start_time =''
        fld_form_end_time =''
        sql = "call sp_registration("+"'"+fld_full_name+"'"+","+"'"+fld_i_identify_as_id+"'"+","+"'"+fld_i_identify_as_name+"'"+","+"'"+fld_age+"'"+","+"'"+fld_country_of_residence+"'"+","+"'"+fld_email+"'"+","+"'"+fld_telephone_number+"'"+","+"'"+fld_tuberculosis_id+"'"+","+"'"+fld_tuberculosis_name+"'"+","+"'"+fld_am_person_id+"'"+","+"'"+fld_am_person_name+"'"+","+"'"+fld_organizational_affiliations+"'"+","+"'"+fld_working_with_TB_HIV+"'"+","+"'"+fld_part_of_this_training+"'"+","+"'"+fld_logged_in_user_id+"'"+","+"'"+fld_data_source+"'"+","+"'"+fld_form_start_time+"'"+","+"'"+fld_form_end_time+"'"+")"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        if result == 1:
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")

def Submission(request):
    return render(request,'Submission.html')

def Forgotpassword(request):
    return render(request,'forgotpassword.html')

def Consentpage(request): 
    return render(request,'Consent.html')

@csrf_exempt
def Consent(request):
    if request.method == 'POST':
        name = request.POST['name']
        mynameid="1"
        myname=request.POST['myname']
        experienceid="1"
        experience=request.POST['experience']
        photographsid="1"
        photographs=request.POST['photographs']
        videosid="1"
        videos=request.POST['videos']
        date=request.POST['date']
        address=request.POST['address']
        cnt_num=request.POST['cnt_num']
        email=request.POST['email']
        fld_logged_in_user_id =''
        fld_data_source ='W'
        fld_form_start_time =''
        fld_form_end_time =''
        sql = "call sp_consent_form("+"'"+name+"'"+","+"'"+mynameid+"'"+","+"'"+myname+"'"+","+"'"+experienceid+"'"+","+"'"+experience+"'"+","+"'"+photographsid+"'"+","+"'"+photographs+"'"+","+"'"+videosid+"'"+","+"'"+videos+"'"+","+"'"+date+"'"+","+"'"+address+"'"+","+"'"+cnt_num+"'"+","+"'"+email+"'"+","+"'"+fld_logged_in_user_id+"'"+","+"'"+fld_data_source+"'"+","+"'"+fld_form_start_time+"'"+","+"'"+fld_form_end_time+"'"+")"
        cursor = connection.cursor()
        connection.commit()
        result = cursor.execute(sql)
        if result == 1:
            return HttpResponse("success")
        else:
            return HttpResponse("something wentwrong!!")

def Pre_and_post(request): 
    return render(request,'Pre_and_post.html')   