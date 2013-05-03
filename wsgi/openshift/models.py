from django.db import models

# A Model for an Inventory
class Inventories(models.Model):
    institution = models.CharField(max_length=100)
    publicationdate = models.CharField(max_length=10)
    stationarycombustion = models.CharField(max_length=100)
    mobilecombustion = models.CharField(max_length=100)
    processemissions = models.CharField(max_length=100)
    fugitiveemissions = models.CharField(max_length=100)
    scope1 = models.CharField(max_length=100)
    purchasedelectricity = models.CharField(max_length=100)
    purchasedheating = models.CharField(max_length=100)
    purchasedcooling = models.CharField(max_length=100)
    purchasedsteam = models.CharField(max_length=100)
    scope2 = models.CharField(max_length=100)
    commuting = models.CharField(max_length=100)
    airtravel = models.CharField(max_length=100)
    solidwaste = models.CharField(max_length=100)
    wastewater = models.CharField(max_length=100)
    paperemissions = models.CharField(max_length=100)
    scope2td = models.CharField(max_length=100)
    scope3 = models.CharField(max_length=100)
    carbonoffsets = models.CharField(max_length=100)
    totalrecs = models.CharField(max_length=100)
    landsequestration = models.CharField(max_length=100)
    compostsequestration = models.CharField(max_length=100)
    gsf = models.CharField(max_length=100)
    residentialspace = models.CharField(max_length=100)
    studentfte = models.CharField(max_length=100)

    def __unicode__(self):
        return self.institution+", "+self.publicationdate