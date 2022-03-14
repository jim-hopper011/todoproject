from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Series
from . forms import SeriesForm
# Create your views here.
def index(request):
    serie= Series.objects.all()
    context= {'series':serie}
    return render(request, 'index.html', context)

def details(request, series_id):
    series= Series.objects.get(id=series_id)
    return render(request, 'details.html', {'series':series})

def add_series(request):
    if request.method == 'POST':
        name= request.POST.get('sname')
        desc = request.POST.get('sdes')
        img = request.FILES['simg']
        series= Series(sname=name, sdes=desc, simg=img)
        series.save()
        return redirect('/')
    return render(request, 'add.html')

def update(request, id):
    series= Series.objects.get(id=id)
    form= SeriesForm(request.POST or None, request.FILES, instance=series)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'series':series})
def delete(request, id):
    if request.method == 'POST':
        series= Series.objects.get(id=id)
        series.delete()
        return redirect('/')
    return render(request, 'delete.html')