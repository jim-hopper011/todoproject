from django.http import HttpResponse
from django.shortcuts import render

from . models import poto, team
# Create your views here.
def d1(request):
    ino= poto.objects.all()
    tm= team.objects.all()
    return render(request, 'index.html', {'data':ino, 'team':tm})


# def add(request):
#     a = int(request.GET['n1'])
#     b = int(request.GET['n2'])
#     addre = a + b
#     subre = a - b
#     mulre = a * b
#     divre = a / b
#     return render(request, 'result.html', {'addresult':addre, 'subresult':subre, 'mulresult':mulre, 'divresult':divre})
