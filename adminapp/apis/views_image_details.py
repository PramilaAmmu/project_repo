from django.shortcuts import render , redirect
from adminapp.models import images
from adminapp.serializers import imagesSerializer
from django.contrib import messages
from rest_framework.views import APIView

class UploadImageAPI(APIView):
	def get(self,request):
		try:
			if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status'):
				# if the user role is not viewonly then fetch the details 
				if request.session['role_type'] != 3:
					output_data = {}
					user_id = request.session["user_id"]

					'''fetching all images details added by the logged in user '''
					image_qs =images.objects.filter(user_id = user_id )
					image_details_lst = []
					for picks in image_qs:
						images_details = {}
						images_details['image_id'] = picks.image_id
						images_details['image'] = picks.image
						images_details['image_title'] = picks.image_title

						image_details_lst.append(images_details)

					output_data['Status'] = "Success"
					output_data['Message'] = "Successfully Fetched the images"
					output_data['image_details'] = image_details_lst

					return render(request,'upload_image_page.html',output_data)

				else:
					return redirect('/login/')
			else:
				return redirect('/login/')
		except Exception:
			return redirect('/')


	def post(self,request):
		try:
			if request.session.has_key("user_id") & request.session.has_key('role_type') & request.session.has_key('login_status'):
				# if the user role is not viewonly then fetch the details 
				if request.session['role_type'] != 3:
					output_data ={}
					user_id = request.session["user_id"]
					input_data =  request.POST.dict()
					input_data['image']=request.FILES['image']

					insert_data ={}
					insert_data['image_title']= input_data['title']
					insert_data['image']= input_data['image']
					insert_data['user_id']= user_id

					serialized_var =imagesSerializer(data=insert_data)
					if serialized_var.is_valid(raise_exception = True):
						serialized_var.save()

						output_data['Status'] = "Success"
						output_data['Message'] = "Image Uploaded Successfully"
						messages.success(request, output_data["Message"])
						return redirect('/upload_image/')
				else:
					return redirect('/login/')

			else:
				return redirect('/login/')

		except Exception:
			return redirect('/login/')
