from django.db import models
from django.contrib.auth import get_user_model


class Likes(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  breed = models.CharField(
      max_length=100
  )
  bio = models.TextField(max_length=200)
  profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='current_owner'
  )



  def __str__(self):
        return self.created
