from django.db import models

# Create your models here.

class Property(models.Model):
        
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
        
    ############################################################################
    #   FIELDS
    ############################################################################
    property_type = models.CharField(
        max_length = 20,
        choices = PROPERTY_TYPE,
        default = 'BUNGALOW'
    ) 