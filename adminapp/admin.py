from django.contrib import admin
from adminapp.models import CreateUser ,images ,uploadedFileDetails

class CreateUserAdmin(admin.ModelAdmin):
	list_display = ['user_id','name','role_type','email_id','password','added_by','added_date']

admin.site.register(CreateUser,CreateUserAdmin)



class imagesAdmin(admin.ModelAdmin):
	list_display = ['image_id','image_title','image','user_id']

admin.site.register(images,imagesAdmin)


class uploadedFileDetailsAdmin(admin.ModelAdmin):
	list_display = ['file_details_id','name','education','city','email_id','user_id','added_by','added_date']

admin.site.register(uploadedFileDetails,uploadedFileDetailsAdmin)