from django.db import models

# Create your models here.

class Property(models.Model):
    
    def __str__(self):
        return self.county, self.street_address, self.bedrooms
        
        
    #def __unicode__(self):
    #     return self.name
    PROPERTY_TYPE={
       ('BUNGALOW','BUNGALOW'),
       ('DETACHED','DETACHED'),
       ('SEMI-DETACHED','SEMI-DETACHED'),
       ('TERRACED','TERRACED'),
       ('APPARTMENT','APPARTMENT'),
       ('SITE','SITE'),
       ('PARKING SPACE','PARKING SPACE')
    }
    
   
    LISTING_TYPE={
       ('FOR SALE','FOR SALE'),
       ('FOR LEASE','FOR LEASE'),
    }
    
    
    BEDROOMS = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10+','10+'),
    }
    
    
    COUNTIES = {
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Derry', 'Derry'),
        ('Donegal', 'Donegal'),
        ('Down', 'Down'),
        ('Dublin', 'Dublin'),
        ('Fermanagh', 'Fermanagh'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Tyrone', 'Tyrone'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    }
    ############################################################################
    #   FIELDS
    ############################################################################
    
    #{'id':'1','price':'€345,000','bedrooms':'4', 'address':'11 West Avenue, Lios Rua, Ballyvolane','county': 'Cork'},
    
    
    property_type = models.CharField(
        max_length = 20,
        choices = PROPERTY_TYPE,
        default = 'BUNGALOW'
    ) 
    
    
    listing_type = models.CharField(
        max_length = 20,
        choices = LISTING_TYPE,
        default = 'FOR SALE'
    ) 
    
    
    price = models.CharField(
        max_length = 30,
        default = '0'
    )
    
    
    bedrooms = models.CharField(
        max_length = 5,
        choices = BEDROOMS,
        default = '1'
    ) 
    
    
    county = models.CharField(
        max_length = 12,
        choices = COUNTIES,
        default = 'Carlow'
    )
    
    
    street_address = models.CharField(
        max_length = 50,
        default = ''
    )
    
    
        
    latitude = models.CharField(
        max_length = 30,
        default = '53.423596'
    )
    
    
    longitude = models.CharField(
        max_length = 30,
        default = '-7.934211'
    )
    

    
    
