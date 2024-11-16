from django.db import models
from django.contrib.auth.models import User 

# Create your models here.ss

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField( max_length=50)
    profile_img = models.ImageField(upload_to='User Profile', default="defualt.jpg")
    pending_cash = models.CharField( max_length=50)

    def __str__(self):
        return self.user.username

class Expence(models.Model):

    title = models.CharField( max_length=50)
    cost = models.IntegerField()
    started_date = models.DateField( auto_now=False, auto_now_add=True, null=True)
    last_date = models.DateField( auto_now=False, auto_now_add=False, null=True)
    remaing_students_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class GivenExpence(models.Model):

    expence = models.ForeignKey(Expence, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cost = models.IntegerField()
    status = models.CharField( max_length=150, null=True)
    date = models.DateField( auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.student.user.username + ' - ' + self.expence.title

