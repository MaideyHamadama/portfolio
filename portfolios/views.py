from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from Portfolio.settings import EMAIL_HOST_USER
import re,os
from .models import FilesAdmin
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    info = ""
    error = False
    files = FilesAdmin.objects.all()
    for post in files:
        file = post
    context = {
        'info' : info,
        'error' : error,
        'file' : file
    }
    return render(request, 'portfolios/index.html', context)

#Create view for sending mail
def mail(request):
    if request.method == 'POST':
        Name = request.POST.get('name', '')
        Email = request.POST['email']
        Tel = request.POST['tel']
        Message = request.POST['message']
        Message = "Name: " + Name + " \nMessage: " + Message + "\nEmail: " + Email + "\nTel: " + Tel
        if Message and Email:
            #Email validator
            if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
                info = "Email is not valid. Check email please"
                error_mail = True
                context = {
                'error' : error_mail,
                'info_mail' : info
                }
                return render(request, 'portfolios/index.html', context)
            if not re.match(r"^6[2,5,6,7,8,9]\d{7}", Tel):
                info = "Telephone number invalid. Check Telephone please"
                error_tel = True
                context = {
                'error' : error_tel,
                'info_tel' : info
                }
                return render(request, 'portfolios/index.html', context)   
            #Sending email after email and tel verification
            try:
                send_mail('Portfolio Contact Message', Message, Email, [EMAIL_HOST_USER], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Make sure all fields are entered and valid')
    return render(request, 'portfolios/index.html')

#Create view for download files
def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404