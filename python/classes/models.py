from django.db import models




class Users(models.Model):
#id .....primary key..
    firstname=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    age=models.CharField()
    bio=models.CharField(maw_length=100)
    pictures=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)) #pictures options..
    orientation=models.CharField()
    expectations=models.CharField(max_length=100)

    class Meta:
        ordering=['firstname','age']

    def __str__(self):
        return self.firstname+" "+self.age


