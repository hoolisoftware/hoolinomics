from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name


class UnitCategory(models.Model):
    name = models.CharField(max_length=55)
    
    class Meta:
        verbose_name_plural = 'unit categories'

    def __str__(self):
        return self.name


class Unit(models.Model):
    currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE, default=3)
    category = models.ForeignKey(to=UnitCategory, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    value = models.IntegerField()
    description = models.TextField(null=True, blank=True)