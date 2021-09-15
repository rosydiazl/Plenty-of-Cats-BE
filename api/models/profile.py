from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  RUSSIANBLUE = 'RB'
  PERSIANCAT = 'PC'
  RAGDOLL = 'RD'
  SPHYNXCAT = 'SC'
  BENGALCAT = 'BC'
  BIRMAN = 'BM'
  SIBERIANCAT = 'SC'
  BOMBAYCAT = 'BC'
  KORAT = 'K'
  THAICAT = 'TC'
  BREED_CHOICES = [
    (RUSSIANBLUE, 'Russian Blue'),
    (PERSIANCAT, 'Persian Cat'),
    (RAGDOLL, 'Ragdoll'),
    (SPHYNXCAT, 'Sphynx Cat'),
    (BENGALCAT, 'Belgal Cat'),
    (BIRMAN, 'Birman'),
    (SIBERIANCAT, 'Siberian Cat'),
    (BOMBAYCAT, 'Bombay Cat'),
    (KORAT, 'Korat'),
    (THAICAT, 'Thai Cat'),
  ]
  breed = models.CharField(
    max_length=2,
    choices=BREED_CHOICES,
    default=RUSSIANBLUE
    )
  bio = models.TextField(max_length=200)
  images = models.ImageField(upload_to='images/')
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
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
        'bio': self.bio
    }
