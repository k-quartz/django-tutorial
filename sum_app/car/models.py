from django.db import models


# Create your models here.
class CarModel(models.Model):
    car_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50, blank=True)
    brand_name = models.CharField(max_length=50, blank=True)
    mfg_year = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"({self.brand_name} - {self.model_name})"

    class Meta:
        db_table = "car"
