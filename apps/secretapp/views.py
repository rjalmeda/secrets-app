from django.shortcuts import render, redirect
from .models import Secret

# Create your views here.
def index(request):
	secrets= Secret.objects.all()
	context={
		"secrets":secrets
	}
	return render(request, 'secretapp/index.html', context)
def create(request):
	if request.method=="POST":
		Secret.objects.create(secret=request.POST['secret'])
		return redirect('/')
	else:
		return 	redirect('/')
def like(request):
	Secret.objects.likes
	pass