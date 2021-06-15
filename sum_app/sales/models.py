from django.db import models
from django.utils import timezone

from sum_app.car.models import CarModel


# Create your models here.
class SalesModel(models.Model):
    sales_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(CarModel, on_delete=models.SET_DEFAULT, default=0)
    sales_year = models.IntegerField(default=timezone.now().year())
    sales_value = models.FloatField(default=0.0)

    class Meta:
        db_table = "sales"
