from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from menus.models import menu


# Create your views here.
def index(request):
    datetime.now().date() #오늘 날짜 가져오기
    today = str(datetime.now().date()) # 형식 변환하기
    menus = menu.objects.all()
    context = {"today":today, 'menus':menus}
    return render(request, 'menus/index.html', context=context)

def detail(request, pk):
    food = menu.objects.all().get(id=pk)
    context={'menu':food}
    return render(request, 'menus/detail.html', context=context)