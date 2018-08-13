# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if request.method == 'POST':
        return redirect('/results/')
    else:
        return render(request, "first_proj/index.html")

def results(request):
    if request.method == 'POST':
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        info = {
            "name" : request.POST['name'],
            "location" : request.POST['Dojo_Location'],
            "fav_lan" : request.POST.get('Favorite_language'),
            "comment" : request.POST.get('optional_comment')
        }
    
    return render(request, "first_proj/results.html", info)
