from django.db import models

# Create your models here.
class Warship(models.Model): 
   name = models.CharField(max_length=250, blank=True)
   leadership = models.DecimalField(max_digits=2, decimal_places=0, default='10')
   power = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   attackBonus = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   hp = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   armour = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   shield = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   load = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   speed = models.DecimalField(max_digits=4, decimal_places=0, default='100')
   damage = models.DecimalField(max_digits=4, decimal_places=0, default='100')

   class Meta:
        verbose_name_plural = "Warship"

   def __str__(self):
        return self.name