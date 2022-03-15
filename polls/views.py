from django.shortcuts import render, get_object_or_404, get_list_or_404
from polls.models import Store, Gu

def index(request):
    return render(request, 'polls/index.html')


def detail_sunhan(request, x):
    store = get_object_or_404(Store,idx=x)
    context = {'store': store}
    return render(request, 'polls/detail_sun.html', context)

def where(request):
    sunhan = Store.objects.all().order_by('addr1')
    gu = Gu.objects.all().order_by('num')
    context = {'sun': sunhan, 'gu': gu}
    return render(request, 'polls/where.html', context)

def where_detail(request,x):
    gu = Gu.objects.all().order_by('num')
    sunhan = get_list_or_404(Store, zipcode=x)
    context = {'sun': sunhan, 'gu': gu}
    return render(request, 'polls/where.html', context)

def analy(request):
    return render(request, 'polls/analy.html')

def aboutus(request):
    return render(request,'polls/aboutus.html')

def aboutusdetail(request):
    return render(request,'polls/aboutusdetail.html')
