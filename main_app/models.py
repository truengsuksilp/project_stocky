from django.db.models import Model, OneToOneField, CASCADE, CharField, ForeignKey, TextField, DateTimeField, SlugField, DateField

from django.contrib.auth.models import User

# Create your models here.

# Extends user model as needed (e.g., location, bio)