from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.user)
# receiver then sender , sender will get executed 
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
        print('profile created')


post_save.connect(create_profile,sender=User)


def update_profile(sender,instance,created,**kwargs):
    if created==False:
        instance.profile.save()
        print('profile Updated')


post_save.connect(update_profile,sender=User)
    

