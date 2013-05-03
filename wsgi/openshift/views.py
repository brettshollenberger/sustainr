import os
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import os.path
from models import Inventories
from django.views.decorators.csrf import csrf_exempt
from forms import CollegeSelect

#Checks whether or not all entries for a given attribute return zero based on user selection.
def NoneCheck(collegelist, attribute):
    attrlist = []
    for coll in collegelist:
        try:
            attr = int(getattr(coll, attribute))
            attrlist.append(attr)
        except:
            attr = getattr(coll, attribute)
            attrlist.append(attr)
            #Attribute returns list of figures
            #attribute = True
            #return attribute
    try:
        if sum(attr for attr in attrlist) == 0:
            attribute = False
    except:
        attribute = attrlist
    return attribute
    #Attribute returns False

@csrf_exempt
def home(request, college1=None, college2=None):
    if request.method == 'POST':
        form = CollegeSelect(request.POST)
        if form.is_valid():
            homepage = True
            cd = form.cleaned_data
            college1 = cd['college1']
            college2 = cd['college2']
            if college1 == college2:
                return render_to_response('sustainr.htm', locals())
            scope1val = cd['scope1']
            scope2val = cd['scope2']
            scope3val = cd['scope3']
            offsetsval = cd['offsets']
            builtspaceval = cd['builtspace']
            studentfteval = cd['studentfte']
            college1queryset = Inventories.objects.filter(institution=college1)
            college2queryset = Inventories.objects.filter(institution=college2)
            collegelist = []
            for college in college1queryset:
                collegelist.append(college)
            for college in college2queryset:
                collegelist.append(college)
            stationarycombustion = NoneCheck(collegelist, 'stationarycombustion')
            mobilecombustion = NoneCheck(collegelist, 'mobilecombustion')
            processemissions = NoneCheck(collegelist, 'processemissions')
            fugitiveemissions = NoneCheck(collegelist, 'fugitiveemissions')
            scope1 = NoneCheck(collegelist, 'scope1')
            purchasedelectricity = NoneCheck(collegelist, 'purchasedelectricity')
            purchasedheating = NoneCheck(collegelist, 'purchasedheating')
            purchasedcooling = NoneCheck(collegelist, 'purchasedcooling')
            purchasedsteam = NoneCheck(collegelist, 'purchasedsteam')
            scope2 = NoneCheck(collegelist, 'scope2')
            commuting = NoneCheck(collegelist, 'commuting')
            airtravel = NoneCheck(collegelist, 'airtravel')
            solidwaste = NoneCheck(collegelist, 'solidwaste')
            wastewater = NoneCheck(collegelist, 'wastewater')
            paperemissions = NoneCheck(collegelist, 'paperemissions')
            scope2td = NoneCheck(collegelist, 'scope2td')
            scope3 = NoneCheck(collegelist, 'scope3')
            carbonoffsets = NoneCheck(collegelist, 'carbonoffsets')
            totalrecs = NoneCheck(collegelist, 'totalrecs')
            landsequestration = NoneCheck(collegelist, 'landsequestration')
            compostsequestration = NoneCheck(collegelist, 'compostsequestration')
            gsf = NoneCheck(collegelist, 'gsf')
            residentialspace = NoneCheck(collegelist, 'residentialspace')
            studentfte = NoneCheck(collegelist, 'studentfte')
            if scope1val and scope2val and scope3val and offsetsval and builtspaceval and studentfteval == False:
                if college1 == college2: 
                    scope1, scope2, scope3, carbonoffsets, totalrecs, landsequestration, compostsequestration, gsf, residentialspace, studentfte = False
                else: 
                    scope1, scope2, scope3, carbonoffsets, totalrecs, landsequestration, compostsequestration, gsf, residentialspace, studentfte = True
            if scope1val or scope2val or scope3val or offsetsval or builtspaceval or studentfteval:
                if not scope1val:
                    scope1 = False
                if not scope2val:
                    scope2 = False
                if not scope3val:
                    scope3 = False
                if not offsetsval:
                    carbonoffsets = False
                    totalrecs = False
                    landsequestration = False
                    compostsequestration = False
                if not builtspaceval:
                    gsf = False
                    residentialspace = False
                if not studentfteval:
                    studentfte = False
            return render_to_response('sustainr.htm', locals())
        else:
            homepage = True
            error = 'colleges'
            return render_to_response('sustainr.htm', locals())
    form = CollegeSelect()
    return render_to_response('sustainr.htm', {'form': form, 'homepage': True})

def about(request):
    return render_to_response('about.htm', {'about': True})
