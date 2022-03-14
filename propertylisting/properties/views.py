from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    property_list = [
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€195,000','bedrooms':'2', 'address':'BLOSSOM & BERRY, Main Street, Lismore','county': 'Co. Waterford'},
        {'price':'€285,000','bedrooms':'4', 'address':'Kilmore, Dring','county': 'Co. Lomngford'},
        {'price':'€340,000','bedrooms':'4', 'address':'22 Mervue Crescent, Ballyvolane','county': 'Co. Cork'},
        {'price':'€495,000','bedrooms':'4', 'address':'The Rectory, Banse Glebe, Kilmanagh','county': 'Co. Kilkenny'},
        {'price':'€230,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
        {'price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Co. Cork'},
    ]
    
    
    
    args = {
        'heading':'Property Listing' ,
        'property_list': property_list,
    }
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'property_list.html',args)