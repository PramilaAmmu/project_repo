from django.shortcuts import render , redirect

from adminapp.models import CreateUser
from adminapp.serializers import CreateUserSerializer

from django.contrib import messages


from rest_framework.views import APIView
from datetime import datetime

# def CreateUserAPI1(request):
# 	try:
# 		return render(request,'create_user_page.html',{})
# 	except Exception:
# 		return redirect('/')


class CreateUserAPI(APIView):
	def get(self,request):
		try:
			if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status'):
				if request.session['role_type'] == 1:

					'''fetching all the user details '''
					output_data = {}
					user_qs = CreateUser.objects.all()
					serialized_user_var = CreateUserSerializer(user_qs,many=True)

					output_data['Status'] = "Success"
					output_data['Message'] = "Successfully Fetched the users"
					output_data['user_details'] = serialized_user_var.data

					return render(request,'create_user_page.html',output_data)

				else:
					return redirect('/login/')
			else:
				return redirect('/login/')
		except Exception:
			return redirect('/')


	def post(self,request):
		try:
			if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status'):

				if request.session['role_type'] == 1:

					output_data ={}
					input_data =  request.POST.dict()
					today_date  = datetime.now().strftime('%Y-%m-%d')

					'''Checking the user email-id is exist or not . if yes display the error mesg '''
					if CreateUser.objects.filter(email_id__iexact = input_data['email_id']).exists() == True:
						output_data['Status'] = "Failure"
						output_data['Message'] = "This email-id is already exists"
						messages.warning(request, output_data["Message"])
						return redirect('/create_user/') 

					insert_data = {}
					insert_data['name'] = input_data['name']
					insert_data['email_id'] = input_data['email_id']
					insert_data['role_type'] = input_data['role_type']
					insert_data['password'] = input_data['password']
					insert_data['added_by'] = request.session['user_name']
					insert_data['added_date'] = today_date

					'''inserting database into the databse '''
					serialized_var = CreateUserSerializer(data=insert_data)
					if serialized_var.is_valid(raise_exception = True):
						serialized_var.save()

						output_data['Status'] = "Success"
						output_data['Message'] = "Successfully Created the User"
						messages.success(request, output_data["Message"])
						return redirect('/create_user/')

				else:
					return redirect('/login/')

			else:
				return redirect('/login/')

		except Exception:
			return redirect('/login/')
