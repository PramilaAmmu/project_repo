from django.shortcuts import render ,redirect
from adminapp.models import CreateUser
from adminapp.serializers import CreateUserSerializer

from django.contrib import messages


def login_function(request):
    if request.method == 'GET':
       
        ''' if u already logged in and again try to login into account session details will be deleted'''
        if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status'):
            del request.session["user_id"]
            del request.session["role_type"]
            del request.session["login_status"]
            return render(request, 'login_page.html', {})

        return render(request, 'login_page.html', {})


    if request.method == "POST":
        try:
            output_data = {}
            input_data = request.POST.dict()

            ''' checking if the email-id is present or not ''' 
            if CreateUser.objects.filter(email_id__iexact = input_data['email_id']).exists() == True:

                ''' fetching the details from the CreateUser table for particular email-id '''
                user_details_qs = CreateUser.objects.filter(email_id__iexact = input_data['email_id']).values('name','password','user_id','role_type')
                for items in user_details_qs:
                    user_details = {}
                    user_details['password'] = items['password']
                    user_details['role_type'] = items['role_type']
                    user_details['user_id'] = items['user_id']
                    user_details['name'] = items['name']

                '''checking if the passwords are matching '''
                if user_details['password'] != input_data['password']:
                    ''' password are wrong, display error message in the login page '''
                    output_data['Status'] = "Failure"
                    output_data['Message'] = "Invalid Password"
                    messages.warning(request, output_data["Message"])
                    return redirect('/login/')

                else:
                    # if password is matched logged in to the dashboard
                    request.session['login_status'] = 'loggedin'
                    request.session['user_id'] = user_details['user_id']
                    request.session['role_type'] = user_details['role_type']
                    request.session['user_name'] = user_details['name']

                    output_data['Status'] = "Success"
                    output_data['Message'] = "You successfully logged in"
                    return redirect('/dashboard/')

            else:
                ''' if the email-id is wrong, display error message in the login page '''
                output_data['Status'] = "Failure"
                output_data['Message'] = "Entered Wrong Email-id"
                messages.warning(request, output_data["Message"])
                return redirect('/login/')

        except Exception:
            return redirect('/login/')


def logout_function(request):
    output_data={}
    if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status') & request.session.has_key('user_name'):
        del request.session["user_id"]
        del request.session["role_type"]
        del request.session["login_status"]
        del request.session['user_name']

        request.session.flush()

        output_data["Status"]="Success"
        output_data["Message"]="Successfully logedout"

        return redirect('/') 

    return redirect('/')




def userDashboard(request):
    if request.session.has_key('user_id') & request.session.has_key('role_type') & request.session.has_key('login_status'):
        try:
            output_data={}
            user_id  = request.session['user_id']

            user_qs = CreateUser.objects.get(user_id = user_id )
            serialized_user_var = CreateUserSerializer(user_qs)

            output_data['user_details'] = serialized_user_var.data

            return render(request, 'dashboard.html',output_data)

        except Exception:
            return redirect('/login/')
        
    else:
        return redirect('/login/')
