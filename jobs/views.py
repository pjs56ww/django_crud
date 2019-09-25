from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
fake = Faker()

def insert(request):
    return render(request, 'jobs/insert.html')

# GIF_API = f'https://api.giphy.com/v1/gifs/search?api_key=yffLcxywQ73zcI0YssOgH5IvPpi9qCU1&q={ p_j }&limit=1&offset=0&rating=G&lang=en'


def past_job(request):
    jobs = Job.objects.all()
    name = request.POST.get('Name')
    image = request.FILES.get('image')
    if jobs.filter(Name=name):

        job = Job.objects.get(Name=name)
    else:
        pastjob = fake.job()
        job = Job()
        job.profile_image = image
        job.Name = name
        job.past_job = pastjob
        job.save()


# https://api.giphy.com/v1/gifs/search?api_key=yffLcxywQ73zcI0YssOgH5IvPpi9qCU1&q=??&limit=1&offset=0&rating=G&lang=en

    context = {'job': job}
    return render(request, 'jobs/past_job.html', context)

def delete(request):
    job = Job.objects.all()
    if request.method == 'POST':
        job.delete()

        return redirect('jobs:insert')
    else:
        return redirect('jobs:insert')

