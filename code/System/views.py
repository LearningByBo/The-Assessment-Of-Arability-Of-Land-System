from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from System.models import Factor

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    factor = Factor()
    factor.generate_DesicionTree()
    return HttpResponse(template.render('', request))