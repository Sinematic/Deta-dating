from django.db import models

# Create your models here.


class Users(models.Model):
    id
    firstname=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    age=models.CharField()
    bio=models.CharField(maw_length=100)
    pictures=models.CharField() #pictures ??..
    orientation=models.CharField()
    expectations=models.CharField(max_length=100)

    class Meta:
        ordering=['firstname','age']

    def __str__(self):
        return self.firstname+" "+self.age


