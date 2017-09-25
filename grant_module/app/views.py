from django.shortcuts import render
from .models import Grant
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json


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

    resp = requests.get('https://storage.scrapinghub.com/items/239574/?format=json', auth=('cfdcde65f04b417ebfc8d6ea60952966', ''))
    grants = resp.json()

    for grant in grants:
        if not Grant.objects.filter(title=grant['title']):
            Grant.objects.create(title=grant['title'], date=grant['date'],
                      link=grant['link'])

    return redirect('grant_list')


