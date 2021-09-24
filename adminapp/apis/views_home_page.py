from django.shortcuts import render ,redirect

def home_page(request):
    try:
        return render(request,'main_page.html',{})

    except Exception:

        return redirect('/')




# def UploadImageAPI(request):
# 	try:
# 		return render(request,'upload_image_page.html',{})
# 	except Exception:
# 		return redirect('/')