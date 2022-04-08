from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Property

# Create your views here.

def index(request):
    
    property_list = [
        {'id':'1','price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Cork'},
        {'id':'2','price':'€195,000','bedrooms':'2', 'address':'BLOSSOM & BERRY, Main Street, Lismore','county': 'Waterford'},
        {'id':'3','price':'€285,000','bedrooms':'4', 'address':'Kilmore, Dring','county': 'Longford'},
        {'id':'4','price':'€340,000','bedrooms':'4', 'address':'22 Mervue Crescent, Ballyvolane','county': 'Cork'},
        {'id':'5','price':'€495,000','bedrooms':'4', 'address':'The Rectory, Banse Glebe, Kilmanagh','county': 'Kilkenny'},
        {'id':'6','price':'€248,500','bedrooms':'4', 'address':'12 St MaryS Road, Kingscourt','county': 'Cavan'},
        {'id':'7','price':'€365,000','bedrooms':'3', 'address': '60 Mill View, Ballinglanna, Glanmire','county': 'Cork'},
        {'id':'8','price':'€295,000','bedrooms':'3', 'address':'3 The Alders, Cstlejane Woods, Glasmire','county': 'Cork'},
        {'id':'9','price':'€425,000','bedrooms':'4', 'address':'29 Stonebridge, Kells, Meath','county': 'Meath'},
        {'id':'10','price':'€485,000','bedrooms':'4', 'address':'Coolmona, Donoughmore','county': 'Cork'},
        {'id':'11','price':'€295,000','bedrooms':'4', 'address':'Roayal Oak Road, Bagenalstown','county': 'Carlow'},
        {'id':'12','price':'€400,000','bedrooms':'4', 'address':'75 The Wavering, Blainroe','county': 'Wicklow'},
        {'id':'13','price':'€410,000','bedrooms':'3', 'address':'106 Carlton Court, Swords','county': 'Dublin'},
        {'id':'14','price':'€240,000','bedrooms':'3', 'address':'12 Chestnut Grove, Casstlepark, Mallow','county': 'Cork'},
        {'id':'15','price':'€345,000','bedrooms':'5', 'address':'13 Woodlands, Abbeycartron','county': 'Longford'},
        {'id':'16','price':'€250,000','bedrooms':'4', 'address':'16 Francis Street, Rathealy, Fermoy','county': 'Cork'},
        {'id':'17','price':'€265,000','bedrooms':'4', 'address':'21 West Avenue, Lios Rua, Ballyvolane','county': 'Kerry'},
        {'id':'18','price':'€105,000','bedrooms':'2', 'address':'Main Street, Lismore','county': 'Wicklow'},
        {'id':'19','price':'€205,000','bedrooms':'4', 'address':'Lismore, Bring','county': 'Leitrim'},
        {'id':'20','price':'€300,000','bedrooms':'4', 'address':'103 Mervue, Ballyvolane','county': 'Limerick'},
        {'id':'21','price':'€405,000','bedrooms':'4', 'address':'Banse Glebe, Kilmanagh','county': 'Carlow'},
        {'id':'22','price':'€348,500','bedrooms':'4', 'address':'39 St MaryS Road, Kingscourt','county': 'Meath'},
        {'id':'23','price':'€260,000','bedrooms':'3', 'address': '12 Mill View, Ballinglanna, Glanmire','county': 'WestMeath'},
        {'id':'24','price':'€240,000','bedrooms':'3', 'address':'17 The Alders, Cstlejane Woods, Glasmire','county': 'Roscommon'},
        {'id':'25','price':'€600,000','bedrooms':'4', 'address':'35 Stonebridge, Kells, Meath','county': 'Donegal'},
        {'id':'26','price':'€415,000','bedrooms':'4', 'address':'Donoughmore','county': 'Sligo'},
        {'id':'27','price':'€245,000','bedrooms':'4', 'address':'Bagenalstown','county': 'Galway'},
        {'id':'28','price':'€300,000','bedrooms':'4', 'address':'51 The Wavering, Blainroe','county': 'Galway'},
        {'id':'29','price':'€320,000','bedrooms':'3', 'address':'19 Carlton Court, Swords','county': 'Laois'},
        {'id':'30','price':'€290,000','bedrooms':'3', 'address':'33 Chestnut Grove, Casstlepark, Mallow','county': 'Laois'},
        {'id':'31','price':'€275,000','bedrooms':'5', 'address':'40 Woodlands, Abbeycartron','county': 'Tipperary'},
        {'id':'32','price':'€270,000','bedrooms':'4', 'address':'4 Francis Street, Rathealy, Fermoy','county': 'Cork'},
    ]
    
    
    property_list_db = Property.objects.all()
    
    p = Paginator(property_list_db,6)
    
    page = request.GET.get('page')
    property_page = p.get_page(page)
    
    
    args = {
        'heading':'Property Listing' ,
        'property_list': property_list,
        'property_page': property_page
    }
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'property_list.html',args)