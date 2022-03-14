from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    property_list = [
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Cork'},
        {'price':'€195,000','bedrooms':'2', 'address':'BLOSSOM & BERRY, Main Street, Lismore','county': 'Waterford'},
        {'price':'€285,000','bedrooms':'4', 'address':'Kilmore, Dring','county': 'Lomngford'},
        {'price':'€340,000','bedrooms':'4', 'address':'22 Mervue Crescent, Ballyvolane','county': 'Cork'},
        {'price':'€495,000','bedrooms':'4', 'address':'The Rectory, Banse Glebe, Kilmanagh','county': 'Kilkenny'},
        {'price':'€248,500','bedrooms':'4', 'address':'12 St MaryS Road, Kingscourt','county': 'Cavan'},
        {'price':'€365,000','bedrooms':'3', 'address': '60 Mill View, Ballinglanna, Glanmire','county': 'Cork'},
        {'price':'€295,000','bedrooms':'3', 'address':'3 The Alders, Cstlejane Woods, Glasmire','county': 'Cork'},
        {'price':'€425,000','bedrooms':'4', 'address':'29 Stonebridge, Kells, Meath','county': 'Meath'},
        {'price':'€485,000','bedrooms':'4', 'address':'Coolmona, Donoughmore','county': 'Cork'},
        {'price':'€295,000','bedrooms':'4', 'address':'Roayal Oak Road, Bagenalstown','county': 'Carlow'},
        {'price':'€400,000','bedrooms':'4', 'address':'75 The Wavering, Blainroe','county': 'Wicklow'},
        {'price':'€410,000','bedrooms':'3', 'address':'106 Carlton Court, Swords','county': 'Co. Dublin'},
        {'price':'€240,000','bedrooms':'3', 'address':'12 Chestnut Grove, Casstlepark, Mallow','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'5', 'address':'13 Woodlands, Abbeycartron','county': 'Co. Longford'},
        {'price':'€250,000','bedrooms':'4', 'address':'16 Francis Street, Rathealy, Fermoy','county': 'Co. Cork'},
    ]
    
    
    
    args = {
        'heading':'Property Listing' ,
        'property_list': property_list,
    }
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'property_list.html',args)