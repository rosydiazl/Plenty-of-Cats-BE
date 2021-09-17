from django.db import models
from django.contrib.auth import get_user_model

from .user import User
from .likes import Likes

# Create your models here.


class Profile(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  breed = models.CharField(
    max_length=100
    )
  bio = models.TextField(max_length=200)
  image = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='current_user'
  )
  liked_profiles = models.ManyToManyField(
      User,
      through=Likes,
      through_fields=('profile_id', 'user_id')
  )

  def __str__(self):
    # This must return a string
    return f"The cat user named '{self.name}' is {self.age} years old. Breed: {self.breed}. Their bio is {self.bio}"

  def as_dict(self):
    """Returns dictionary version of Profile models"""
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'breed': self.breed,
        'bio': self.bio,
        'image': self.image
    }
