from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import products
# Create your views here.
def home(request):
    return render(request,'products/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] :
            pr = products()
            pr.title = request.POST['title']
            pr.body = request.POST['body']
            pr.url = request.POST['url']
            pr.icon = request.FILES['icon']
            pr.image = request.FILES['image']
            pr.pubdate = timezone.datetime.now()
            pr.hunter = request.user
            pr.save()
            return redirect('home')
        
        else:
            return render(request,'products/create.html',{'error':'all fields are required'})

    else:
        return render(request,'products/create.html')
