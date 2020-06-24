from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import products
# Create your views here.
def home(request):
    product=products.objects
    return render(request,'products/home.html',{'product':product})

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
            return redirect('/products/' + str(pr.id))
        
        else:
            return render(request,'products/create.html',{'error':'all fields are required'})

    else:
        return render(request,'products/create.html')



def detail(request,product_id):
    pr = get_object_or_404(products , pk=product_id)
    return render(request,'products/detail.html',{'product':pr})        

@login_required
def upvote(request,product_id):
    if request.method == 'POST':
        pr = get_object_or_404(products , pk=product_id)
        pr.votes_total+=1
        pr.save()
        return redirect('/products/' + str(pr.id))