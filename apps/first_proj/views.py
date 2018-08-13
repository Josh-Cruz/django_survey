# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if request.method == 'POST':
        return redirect('/results')
    else:
        return render(request, "/first_proj/index.html")

def results(request):
    if request.method == 'POST':
        request.session['count'] += 0
        info = {
            "name" : request.POST['name'],
            "location" : request.POST['Dojo_Location'],
            "fav_lan" : request.POST['Favorite_language'],
            "comment" : request.POST['optional_comment']
        }
    return render(request, "first_proj/results.html", info)
