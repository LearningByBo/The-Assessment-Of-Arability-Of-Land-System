from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from System.models import Factor


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    # Factor.generate_DesicionTree()
    return HttpResponse(template.render('', request))


def infoinput(request):
    template = loader.get_template('info-input.html')
    return HttpResponse(template.render('', request))


def analyse(request):
    # 1, prehandle the input data
    # 2, gennerate the Decesion Tree and predict the data
    # 3, display the prediction

    if 'name' in request.POST and request.POST['name']:
        name = request.POST['name']
    else:
        name = ''
    if 'organic_matter' in request.POST and request.POST['organic_matter']:
        organic_matter = float(request.POST['organic_matter'])
        if organic_matter > 2.6:
            organic_matter = int(1)
        elif organic_matter > 2.5:
            organic_matter = int(2)
        elif organic_matter > 2.4:
            organic_matter = int(3)
        elif organic_matter > 2.3:
            organic_matter = int(4)
        elif organic_matter > 2.2:
            organic_matter = int(5)
        else:
            organic_matter = int(6)
    else:
        organic_matter = 0

    if 'total_nitrogen' in request.POST and request.POST['total_nitrogen']:
        total_nitrogen = float(request.POST['total_nitrogen'])
        if total_nitrogen > 0.15:
            total_nitrogen = int(1)
        elif total_nitrogen > 0.14:
            total_nitrogen = int(2)
        elif total_nitrogen > 0.13:
            total_nitrogen = int(3)
        elif total_nitrogen > 0.12:
            total_nitrogen = int(4)
        elif total_nitrogen > 0.11:
            total_nitrogen = int(5)
        else:
            total_nitrogen = int(6)
    else:
        total_nitrogen = 0

    if 'available_P' in request.POST and request.POST['available_P']:
        available_p = float(request.POST['available_P'])
        if available_p > 20.0:
            available_p = int(1)
        elif available_p > 18.0:
            available_p = int(2)
        elif available_p > 17.0:
            available_p = int(3)
        elif available_p > 16.0:
            available_p = int(4)
        elif available_p > 15.0:
            available_p = int(5)
        else:
            available_p = int(6)
    else:
        available_p = 0

    if 'available_K' in request.POST and request.POST['available_K']:
        available_k = float(request.POST['available_K'])
        if available_k > 180.0:
            available_k = int(1)
        elif available_k > 170.0:
            available_k = int(2)
        elif available_k > 160.0:
            available_k = int(3)
        elif available_k > 150.0:
            available_k = int(4)
        elif available_k > 140.0:
            available_k = int(5)
        else:
            available_k = int(6)
    else:
        available_k = 0

    if (name != '') and (organic_matter != 0) and (total_nitrogen != 0) and (available_p != 0) and (available_k != 0):
        template = loader.get_template('analyse-detail.html')
        answer = Factor.predict_data(organic_matter,total_nitrogen,available_k,available_p)
        print answer
    else:
        print name
        print organic_matter
        print total_nitrogen
        print available_k
        print available_p
        template = loader.get_template('info-input.html')


    return HttpResponse(template.render('', request))
