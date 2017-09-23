from django.shortcuts import render
from .models import Grant


def grant_list(request):
	grants = Grant.objects.all()
	return render(request, 'app/grant_list.html', {'grants' : grants})




