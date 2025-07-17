from django.contrib.auth.models import AbstractUser
from django.db import models

# Option 1: Inherit the Abstract user, gives us the ability to add fields on top of the ones from django
# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         null=True,
#         blank=True,
#     )

# Option 2: This won't create a table, we can't add fields, we can define methods
# class CustomCustomUser(CustomUser):
#     class Meta:
#         proxy = True
#
#     def get_points(self):
#         return self.points

