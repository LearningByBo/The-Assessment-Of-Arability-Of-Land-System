# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from System.models import Factor
from .forms import UploadFileForm
import sys
from django.core.context_processors import csrf


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render('', request))


def index_err_mess(request,err_mess):
    context = Context({err_mess: err_mess})
    context.update(csrf(request))
    return render_to_response('index.html',context)


def info_input(request):
    template = loader.get_template('info-input.html')
    return HttpResponse(template.render('', request))


def analyse(request):

    # may not exist
    if 'organic_matter' in request.POST and request.POST['organic_matter']:
        organic_matter = request.POST['organic_matter']
    else:
        organic_matter = -1

    if 'total_nitrogen' in request.POST and request.POST['total_nitrogen']:
        total_nitrogen = request.POST['total_nitrogen']
    else:
        total_nitrogen = -1

    if 'available_P' in request.POST and request.POST['available_P']:
        available_p = request.POST['available_P']
    else:
        available_p = -1

    if 'available_K' in request.POST and request.POST['available_K']:
        available_k = request.POST['available_K']
    else:
        available_k = -1

    if 'illumination_intensity' in request.POST and request.POST['illumination_intensity']:
        illumination_intensity = float(request.POST['illumination_intensity'])
    else:
        illumination_intensity = -1

    if 'illumination_time' in request.POST and request.POST['illumination_time']:
        illumination_time = float(request.POST['illumination_time'])
    else:
        illumination_time = -1

    if 'wind_speed' in request.POST and request.POST['wind_speed']:
        wind_speed = float(request.POST['wind_speed'])
    else:
        wind_speed = -1

    if 'cultivated_crops1' in request.POST and request.POST['cultivated_crops1']:
        cultivated_crops1 = request.POST['cultivated_crops1']
    else:
        cultivated_crops1 = ''

    if 'cultivation_cycle1' in request.POST and request.POST['cultivation_cycle1']:
        cultivation_cycle1 = float(request.POST['cultivation_cycle1'])
    else:
        cultivation_cycle1 = -1

    if 'cultivated_crops2' in request.POST and request.POST['cultivated_crops2']:
        cultivated_crops2 = request.POST['cultivated_crops2']
    else:
        cultivated_crops2 = 'N/A'

    if 'cultivation_cycle2' in request.POST and request.POST['cultivation_cycle2']:
        cultivation_cycle2 = float(request.POST['cultivation_cycle2'])
    else:
        cultivation_cycle2 = 'N/A'

    if 'cultivated_crops3' in request.POST and request.POST['cultivated_crops3']:
        cultivated_crops3 = request.POST['cultivated_crops3']
    else:
        cultivated_crops3 = 'N/A'

    if 'cultivation_cycle3' in request.POST and request.POST['cultivation_cycle3']:
        cultivation_cycle3 = float(request.POST['cultivation_cycle3'])
    else:
        cultivation_cycle3 = 'N/A'

    if 'chemical_fertilizer' in request.POST and request.POST['chemical_fertilizer']:
        chemical_fertilizer = float(request.POST['chemical_fertilizer'])
    else:
        chemical_fertilizer = -1

    if 'manure' in request.POST and request.POST['manure']:
        manure = float(request.POST['manure'])
    else:
        manure = -1

    # must exist
    if 'earth_type' in request.POST and request.POST['earth_type']:
        earth_type = request.POST['earth_type']

    if 'field_type' in request.POST and request.POST['field_type']:
        field_type = request.POST['field_type']

    if 'terrain' in request.POST and request.POST['terrain']:
        terrain = request.POST['terrain']

    if 'vegetation' in request.POST and request.POST['vegetation']:
        vegetation = request.POST['vegetation']

    if 'climate' in request.POST and request.POST['climate']:
        climate = request.POST['climate']

    if 'wind_direction' in request.POST and request.POST['wind_direction']:
        wind_direction = request.POST['wind_direction']

    if 'plant_diseases' in request.POST and request.POST['plant_diseases']:
        plant_diseases = request.POST['plant_diseases']

    context = get_context(earth_type,field_type,organic_matter,total_nitrogen,available_p,available_k,terrain,vegetation,climate,illumination_intensity,illumination_time,wind_direction,wind_speed,plant_diseases,cultivated_crops1,cultivation_cycle1,cultivated_crops2,cultivation_cycle2,cultivated_crops3,cultivation_cycle3,chemical_fertilizer,manure)
    if context == None:
        template = loader.get_template('info-input.html')
        context = Context({'mess': '请填写全部信息'})
    else:
        context.update({'source': '手动输入'})
        template = loader.get_template('analyse-detail.html')

    return HttpResponse(template.render(context, request))


def get_context(earth_type,field_type,organic_matter,total_nitrogen,available_p,available_k,terrain,vegetation,climate,illumination_intensity,illumination_time,wind_direction,wind_speed,plant_diseases,cultivated_crops1,cultivation_cycle1,cultivated_crops2,cultivation_cycle2,cultivated_crops3,cultivation_cycle3,chemical_fertilizer,manure):
    if organic_matter != -1:
        organic_matter = float(organic_matter)
        if organic_matter > 2.6:
            organic_matter_in = int(1)
        elif organic_matter > 2.5:
            organic_matter_in = int(2)
        elif organic_matter > 2.4:
            organic_matter_in = int(3)
        elif organic_matter > 2.3:
            organic_matter_in = int(4)
        elif organic_matter > 2.2:
            organic_matter_in = int(5)
        else:
            organic_matter_in = int(6)
    else:
        organic_matter_in = -1

    if total_nitrogen != -1:
        total_nitrogen = float(total_nitrogen)
        if total_nitrogen > 0.15:
            total_nitrogen_in = int(1)
        elif total_nitrogen > 0.14:
            total_nitrogen_in = int(2)
        elif total_nitrogen > 0.13:
            total_nitrogen_in = int(3)
        elif total_nitrogen > 0.12:
            total_nitrogen_in = int(4)
        elif total_nitrogen > 0.11:
            total_nitrogen_in = int(5)
        else:
            total_nitrogen_in = int(6)
    else:
        total_nitrogen_in = -1

    if available_p != -1:
        available_p = float(available_p)
        if available_p > 20.0:
            available_p_in = int(1)
        elif available_p > 18.0:
            available_p_in = int(2)
        elif available_p > 17.0:
            available_p_in = int(3)
        elif available_p > 16.0:
            available_p_in = int(4)
        elif available_p > 15.0:
            available_p_in = int(5)
        else:
            available_p_in = int(6)
    else:
        available_p_in = -1

    if available_k != -1:
        available_k = float(available_k)
        if available_k > 180.0:
            available_k_in = int(1)
        elif available_k > 170.0:
            available_k_in = int(2)
        elif available_k > 160.0:
            available_k_in = int(3)
        elif available_k > 150.0:
            available_k_in = int(4)
        elif available_k > 140.0:
            available_k_in = int(5)
        else:
            available_k_in = int(6)
    else:
        available_k_in = -1

    levellist = ['一', '二', '三', '四', '五', '六']

    if (organic_matter_in != -1) and (total_nitrogen_in != -1) and (available_p_in != -1) and (
        available_k_in != -1) and (
                illumination_intensity != -1) and (illumination_time != -1) and (wind_speed != -1) and (
                cultivated_crops1 != '') and (cultivation_cycle1 != -1) and (chemical_fertilizer != -1) and (
        manure != -1):
        answer = Factor.predict_data(organic_matter_in, total_nitrogen_in, available_p_in, available_k_in)
        index = int(answer[0])
        # print index
        level = levellist[index - 1]
        # print level
        evaluation = '一般'
        reason = '只耕种一种耕作物，不能很好地利用土地的资源，因为单一的耕作物对耕地中的微量元素的需求一成不变，故浪费了耕地中的另一部分的微量元素'
        if (cultivated_crops2 != 'N/A') and (cultivation_cycle2 != 'N/A'):
            evaluation = '良好'
            reason = '两种耕作物轮番耕种，能够较好的利用耕地的微量元素，轮番耕种可以对耕地中的大部分微量元素被充分的利用上'
            if (cultivated_crops3 != 'N/A') and (cultivation_cycle3 != 'N/A'):
                evaluation = '很好'
                reason = '耕种多种耕作物，充分利用耕地的每一种微量元素，可谓对耕地的利用达到最好的水平了'
        if field_type == u'水田' or field_type == u'望天田' or field_type == u'水浇田':
            change_for1 = '种植苗木花卉'
            possibility1 = '较高'
            condition1 = '地形：丘陵、平原、盆地 ； 气候：热带季风气候，亚热带季风气候，温带大陆性气候，温带季风气候'
            change_for2 = '种植莲藕、马蹄'
            possibility2 = '较高'
            condition2 = '地形：丘陵、平原、盆地 ； 气候：热带季风气候，亚热带季风气候'
        elif field_type == u'旱地':
            change_for1 = '種果樹'
            possibility1 = '较高'
            condition1 = '地形：山地、丘陵、平原、盆地 ； 气候：热带季风气候，亚热带季风气候，温带季风气候，温带大陆性气候'
            change_for2 = '養雞牛羊'
            possibility2 = '较高'
            condition2 = '地形：不限 ； 气候：热带季风气候，亚热带季风气候，温带季风气候，温带大陆性气候'
        else:
            change_for1 = '交错种植，由可以种植果树的同时种植蔬菜'
            possibility1 = '较高'
            condition1 = '地形：丘陵、平原、盆地 ； 气候：热带季风气候，亚热带季风气候，温带季风气候，温带大陆性气候'
            change_for2 = 'N/A'
            possibility2 = 'N/A'
            condition2 = 'N/A'
        lack = ''
        if organic_matter_in != 1:
            lack += '有机质'
        if total_nitrogen_in != 1:
            if len(lack) != 0:
                lack += ','
            lack += '全氮'
        if available_p_in != 1:
            if len(lack) != 0:
                lack += ','
            lack += '速效磷'
        if available_k_in != 1:
            if len(lack) != 0:
                lack += ','
            lack += '速效钾'
        if index == 1:
            lack = ''

        context = Context(
            {'lack': lack, 'condition2': condition2, 'possibility2': possibility2, 'change_for2': change_for2,
             'condition1': condition1, 'possibility1': possibility1, 'change_for1': change_for1, 'reason': reason,
             'evaluation': evaluation, 'level': level, 'land_capability': level + '级地',
             'earth_type': earth_type, 'field_type': field_type, 'organic_matter': organic_matter,
             'total_nitrogen': total_nitrogen, 'available_p': available_p, 'available_k': available_k,
             'terrain': terrain, 'vegetation': vegetation, 'climate': climate,
             'illumination_intensity': illumination_intensity, 'illumination_time': illumination_time,
             'wind_direction': wind_direction, 'wind_speed': wind_speed, 'plant_diseases': plant_diseases,
             'cultivated_crops1': cultivated_crops1, 'cultivation_cycle1': cultivation_cycle1,
             'cultivated_crops2': cultivated_crops2, 'cultivation_cycle2': cultivation_cycle2,
             'cultivated_crops3': cultivated_crops3, 'cultivation_cycle3': cultivation_cycle3,
             'chemical_fertilizer': chemical_fertilizer, 'manure': manure})
    else:
        context = None

    return context


def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # get the data from the uploaded_file
            data = handle_uploaded_file(request.FILES['uploadfile'])
            if data == []:
                template = loader.get_template('index.html')
                return HttpResponseRedirect('/index/upload_file_message_missing/',)
            # verify the data
            if not verify_upload_file_data(data):
                template = loader.get_template('index.html')
                return HttpResponseRedirect('/index/upload_file_message_verify_fail/', )
            else:
                illumination_intensity = float(data[9])
                illumination_time = float(data[10])
                wind_speed = float(str(data[11].encode('utf-8')).split(',')[1].strip())
                cultivated_crops1 = str(data[13].encode('utf-8')).split(',')[0].strip()
                cultivation_cycle1 = float(str(data[13].encode('utf-8')).split(',')[1].strip())
                if data[14].split(',').__len__() == 2:
                    cultivated_crops2 = str(data[14].encode('utf-8')).split(',')[0].strip()
                    cultivation_cycle2 = str(data[14].encode('utf-8')).split(',')[1].strip()
                    if not is_float(cultivation_cycle2):
                        cultivation_cycle2 = 'N/A'
                else:
                    cultivated_crops2 = 'N/A'
                    cultivation_cycle2 = 'N/A'
                if data[15].split(',').__len__() == 2:
                    cultivated_crops3 = str(data[15].encode('utf-8')).split(',')[0].strip()
                    cultivation_cycle3 = str(data[15].encode('utf-8')).split(',')[1].strip()
                    if not is_float(cultivation_cycle3):
                        cultivation_cycle3 = 'N/A'
                else:
                    cultivated_crops3 = 'N/A'
                    cultivation_cycle3 = 'N/A'
                chemical_fertilizer = float(data[16])
                manure = float(data[17])
                context = get_context(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],illumination_intensity,illumination_time,str(data[11].encode('utf-8')).split(',')[0].strip(),wind_speed,data[12],cultivated_crops1,cultivation_cycle1,cultivated_crops2,cultivation_cycle2,cultivated_crops3,cultivation_cycle3,chemical_fertilizer,manure)
                if context == None:
                    template = loader.get_template('index.html')
                    return HttpResponseRedirect('/index/upload_file_message_verify_fail/', )
                else:
                    context.update({'source': '文件上传'})
                    return render_to_response('analyse-detail.html',context)


def handle_uploaded_file(f):
    # upload the file to the server
    with open(sys.path[0] + '\\static\\file\\' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    data = []
    with open(sys.path[0] + '\\static\\file\\' + f.name, 'rb+') as reader:
        for line in reader.readlines():
            # verify the data is digital & some data must be set
            # print line.split(':')[1].strip('\r\n').strip().decode("utf-8")
            if line.split(':').__len__() == 2:
                data.append(line.split(':')[1].strip('\r\n').strip().decode("utf-8"))
    if data.__len__() != 18:
        data = []
    # print data
    return data


def verify_upload_file_data(data):
    # print data
    earth_type = data[0]
    if not is_earth_type(earth_type):
        return False
    field_type = data[1]
    if not is_field_type(field_type):
        return False
    organic_matter = data[2]
    if not is_float(organic_matter):
        return False
    total_nitrogen = data[3]
    if not is_float(total_nitrogen):
        return False
    available_p = data[4]
    if not is_float(available_p):
        return False
    available_k = data[5]
    if not is_float(available_k):
        return False
    terrain = data[6]
    if not is_terrain(terrain):
        return False
    vegetation = data[7]
    if not is_vegetation(vegetation):
        return False
    climate = data[8]
    if not is_climate(climate):
        return False
    illumination_intensity = data[9]
    if not is_float(illumination_intensity):
        return False
    illumination_time = data[10]
    if not is_float(illumination_time):
        return False
    if str(data[11].encode('utf-8')).split(',').__len__() != 2:
        return False
    wind_direction = str(data[11].encode('utf-8')).split(',')[0].strip()
    # print 'wind'
    # print is_wind_direction(wind_direction)
    if not is_wind_direction(wind_direction):
        return False
    wind_speed = str(data[11].encode('utf-8')).split(',')[1].strip()
    if not is_float(wind_speed):
        return False
    plant_diseases = data[12]
    if not is_plant_diseases(plant_diseases):
        return False
    if str(data[13].encode('utf-8')).split(',').__len__() != 2:
        return False
    cultivated_crops1 = str(data[13].encode('utf-8')).split(',')[0].strip()
    cultivation_cycle1 = str(data[13].encode('utf-8')).split(',')[1].strip()
    if not is_float(cultivation_cycle1):
        return False
    chemical_fertilizer = data[16]
    if not is_float(chemical_fertilizer):
        return False
    manure = data[17]
    if not is_float(manure):
        return False

    return True


# verify the data is float
def is_float(str_float):
    if str(str_float).split('.').__len__() == 2:
        return str(str_float).split('.')[0].isdigit() and str(str_float).split('.')[1].isdigit()
    else:
        return str(str_float).isdigit()


# verify the data is in the set
def is_earth_type(s):
    earth_type = [u'砖红壤',u'赤红壤',u'红壤',u'黄壤',u'黄棕壤',u'棕壤',u'暗棕壤',u'寒棕壤',u'褐土',u'黑钙土',u'栗钙土',u'棕钙土',u'黑垆土',u'荒漠土',u'草甸土',u'漠土']
    return earth_type.__contains__(s)


def is_field_type(s):
    field_type = [u'水田',u'望天田',u'菜地',u'旱地',u'水浇田']
    return field_type.__contains__(s)


def is_terrain(s):
    terrain = [u'高原',u'山地',u'丘陵',u'平原',u'盆地']
    return terrain.__contains__(s)


def is_vegetation(s):
    vegetation = [u'草原',u'荒漠',u'热带雨林',u'常绿阔叶林',u'落叶阔叶林',u'针叶林']
    return vegetation.__contains__(s)


def is_climate(s):
    climate = [u'热带季风气候',u'亚热带季风气候',u'温带季风气候',u'温带大陆性气候',u'高原山地气候']
    return climate.__contains__(s)


def is_wind_direction(s):
    wind_direction = ['北风','东北风','东风','东南风','南风','西南风','西风','西北风']
    return wind_direction.__contains__(s)


def is_plant_diseases(s):
    plant_diseases = [u'无',u'少',u'一般',u'多']
    return plant_diseases.__contains__(s)