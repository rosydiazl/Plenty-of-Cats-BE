from django.db import models


class Likes(models.Model):
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created
