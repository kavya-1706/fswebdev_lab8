from django.shortcuts import render
from .models import *
from jobproject.settings import BASE_DIR
# Create your views here.

def index(request):
    # jobs_data.objects.all().delete() #To Delete the data
    jobs = jobs_data.objects.all()
    return render(request, 'index.html', {'jobs':jobs, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        job = jobs_data()
        job.job_Name = request.POST.get("job_Name", False)
        job.job_Company = request.POST.get("job_Company", False)
        job.job_Location = request.POST.get("job_Location", False)
        job.job_Desc = request.POST.get("job_Desc", False)

        job.save()

    
    return render(request, 'upload.html')

