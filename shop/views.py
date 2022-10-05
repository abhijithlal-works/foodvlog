from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None

    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:

         prodt=products.objects.all().filter(available=True)


    cat=categ.objects.all()

# <!-- paginator ################################################################################################ -->

    page=request.GET.get('page',1)

    paginator = Paginator(prodt,4)
    try:
        page= paginator.page(page)
    except PageNotAnInteger:
        page= paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{"pr":page, 'ct':cat})


    # paginator=Paginator(prodt,6)
    # try:
    #     page= paginator.page('page','1')
    # except PageNotAnInteger:
    #     page=paginator.page(1)
    #
    #
    # except(EmptyPage):
    #     page=paginator.page(paginator.num_pages)
    # return render(request,'index.html',{"pr":page, 'ct':cat})

# <!-- end paginator ################################################################################################ -->



def prodDetail(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)

    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)| Q(desc__contains=query))


    return render(request,'search.html', {"qr":query, "pr":prod})

