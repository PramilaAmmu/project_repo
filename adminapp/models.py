from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class CreateUser(models.Model):
	user_id  = models.AutoField(primary_key =True)
	name = models.CharField(max_length=100 ,blank=True)
	email_id = models.CharField(max_length = 100 , blank=True)
	password = models.CharField(max_length = 50,blank=True)
	role_type  = models.IntegerField(default=1) #by default user is admin: 1-admin,2-uploader,3-Viewonly
	added_by = models.CharField(max_length=100, default=None)
	added_date = models.DateField()

    
	def __str__(self):
		return str(self.user_id)



class images(models.Model):
	image_id = models.AutoField(primary_key =True)
	image_title = models.CharField(max_length=100)
	image = CloudinaryField('image')
	user_id = models.ForeignKey(CreateUser,on_delete=models.CASCADE ,default=1)

	def __str__(self):
		return str(self.image_id)


class uploadedFileDetails(models.Model):
    file_details_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    user_id = models.IntegerField(default=1)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateField()
    

    def __str__(self):
        return str(self.file_details_id)