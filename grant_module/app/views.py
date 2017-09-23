from django.shortcuts import render
from .models import Grant
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def grant_list(request):

    grant_list = Grant.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(grant_list, 15)

    try:
        grants = paginator.page(page)
    except PageNotAnInteger:
        grants = paginator.page(1)
    except EmptyPage:
        grants = paginator.page(paginator.num_pages)

    return render(request, 'app/grant_list.html', { 'grants': grants })


@login_required
def crawler(request):

    data = [
       ['project', 'default'],
       ['spider', 'rfbr'],
           ]

    requests.post('http://localhost:6800/schedule.json', data=data)

    data[1][1] = 'rscf'
    requests.post('http://localhost:6800/schedule.json', data=data)

    data[1][1] = 'tp'
    requests.post('http://localhost:6800/schedule.json', data=data)

    return redirect('grant_list')


