# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
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

    # may not exist
    if 'organic_matter' in request.POST and request.POST['organic_matter']:
        organic_matter = float(request.POST['organic_matter'])
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

    if 'total_nitrogen' in request.POST and request.POST['total_nitrogen']:
        total_nitrogen = float(request.POST['total_nitrogen'])
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

    if 'available_P' in request.POST and request.POST['available_P']:
        available_p = float(request.POST['available_P'])
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

    if 'available_K' in request.POST and request.POST['available_K']:
        available_k = float(request.POST['available_K'])
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

    levellist = ['一', '二', '三', '四', '五', '六']

    if (organic_matter_in != -1) and (total_nitrogen_in != -1) and (available_p_in != -1) and (available_k_in != -1) and (
        illumination_intensity != -1) and (illumination_time != -1) and (wind_speed != -1) and (
        cultivated_crops1 != '') and (cultivation_cycle1 != -1) and (chemical_fertilizer != -1) and (manure != -1):
        answer = Factor.predict_data(organic_matter_in, total_nitrogen_in, available_p_in, available_k_in)
        index = int(answer[0])
        level = levellist[index - 1]
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

        template = loader.get_template('analyse-detail.html')
        context = Context(
            {'lack': lack, 'condition2': condition2, 'possibility2': possibility2, 'change_for2': change_for2,
             'condition1': condition1, 'possibility1': possibility1, 'change_for1': change_for1, 'reason': reason,
             'evaluation': evaluation, 'level': level, 'source': '手动输入', 'land_capability': level + '级地',
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
        template = loader.get_template('info-input.html')
        context = Context({'mess': '请填写全部信息'})

    return HttpResponse(template.render(context, request))
