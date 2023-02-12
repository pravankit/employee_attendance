from django.db import models
from django.core.validators import MaxValueValidator
class Service(models.Model):
    E_id= models.IntegerField(primary_key=True,validators=[MaxValueValidator(9999999999)])
    Name=models.CharField(max_length=50)
    January= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    February= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    March= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    April= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    May= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    June= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    July= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    August= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    September= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    October= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    November= models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    December= models.PositiveIntegerField(validators=[MaxValueValidator(31)])

class Employee_details(models.Model):
    Month_number=models.PositiveIntegerField(validators=[MaxValueValidator(13)])
    Month = models.CharField(max_length=50)
    Ramesh  = models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    Anju = models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    Manju = models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    Umesh = models.PositiveIntegerField(validators=[MaxValueValidator(31)])
    Neha = models.PositiveIntegerField(validators=[MaxValueValidator(31)])

