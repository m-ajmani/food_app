from django.shortcuts import render
from .models import food,review
from django.contrib.auth.decorators import login_required


def home(request):
	context = {
		'choices': food.objects.all()
	}
	return render(request, 'food/home.html', context)


def reviews(request):
	context = {
		'reviews': review.objects.all()
	}
	return render(request, 'food/reviews.html', context)

def login(request):
	return render(request, 'food/login.html')

def register(request):
	return render(request, 'food/register.html')

#In the views.py file of the users app, I used the following code to make the profile page unavailable until login is done. I tried to do the same here, but it was showing error.
#from django.contrib.auth.decorators import login_required
#@login_required
