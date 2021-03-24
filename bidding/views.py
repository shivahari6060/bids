from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Sum
import datetime

# Create your views here.
def index(request):
    context={}
    return render(request, 'bidding/base.html', context)

def Supplier_add(request):
    form = SupplysideCreationForm()
    if request.method=='POST':
        form= SupplysideCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bidding:matchdemand')
    context={
        'form':form,
    }
    return render(request, 'bidding/supplier_add.html', context)


def Demand_add(request):
    form = DemandsideCreationForm()
    if request.method=='POST':
        form= DemandsideCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bidding:matchdemand')
    context={
        'form':form,
    }
    return render(request, 'bidding/demand_add.html', context)


def MatchDemand(request):
    supplies = Supplyside.objects.filter(active=False).order_by('-supply_create')[:7]
    demands = Demandside.objects.filter(active=False).order_by('-supply_create')[:7]
    matches = BidMatch.objects.all().order_by('-created')[:7]
    for supply in supplies:
        for demand in demands:
            if supply.commodity==demand.commodity:
                if supply.seed_type==demand.seed_type:
                    if supply.quantity==demand.quantity and supply.price==demand.price:
                        dttm = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        supid= supply.id
                        demid= demand.id
                        supply_id = "%02d" %supid
                        demand_id = "%02d" %demid
                        code = dttm + supply_id + demand_id
                        bidmatch= BidMatch.objects.create(
                            supply_id=supply.id,
                            demand_id=demand.id,
                            txn_code=code,
                            category=supply.category,
                            commodity= supply.commodity,
                            seed_type= supply.seed_type,
                            quantity= int(supply.quantity),
                            price=float(supply.price))
                        supply.active=True
                        supply.save()
                        demand.active=True
                        demand.save()
                        supplies = Supplyside.objects.filter(active=False).order_by('-supply_create')[:7]
                        demands = Demandside.objects.filter(active=False).order_by('-supply_create')[:7]
                    else:
                        supply.active=False
                        supply.save()
                        demand.active=False
                        demand.save()
                        supplies = Supplyside.objects.filter(active=False).order_by('-supply_create')[:7]
                        demands = Demandside.objects.filter(active=False).order_by('-supply_create')[:7]
                else:
                    pass
            else:
                pass
    # df = pd.DataFrame(list(Supplyside.objects.all().values()))
    # for commodity in Commodity.objects.all():
    #     supplies = Supplyside.objects.filter(commodity=commodity).aggregate(Sum('quantity'))
    context ={
        'supplies':supplies,
        'demands':demands,
        'matches':matches,
    }
    return render(request, 'bidding/match.html', context)



#the integration of the forms dropdowns.
# AJAX
def load_provinces(request):
    country_id = request.GET.get('country_id')
    provinces = Province.objects.filter(country_id=country_id).all()
    context={'provinces': provinces}
    return render(request, 'bidding/province_dropdown_options.html', context )
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_districts(request):
    province_id= request.GET.get('province_id')
    districts= District.objects.filter(province_id=province_id).all()
    context={'districts':districts}
    return render(request, 'bidding/district_dropdown_options.html', context)

def load_municipalities(request):
    district_id= request.GET.get('district_id')
    municipalities=  Municipality.objects.filter(district_id=district_id).all()
    context={'municipalities':municipalities}
    return render(request, 'bidding/municipality_dropdown_options.html', context)

def load_commodity(request):
    category_id = request.GET.get('category_id')
    commodities = Commodity.objects.filter(category_id=category_id).all()
    context={'commodities':commodities}
    return render(request, 'bidding/commodities_list.html', context)

def load_seedtype(request):
    commodity_id = request.GET.get('commodity_id')
    seeds = SeedType.objects.filter(commodity_id=commodity_id).all()
    context={'seeds':seeds}
    return render(request, 'bidding/seedtype_list.html', context)