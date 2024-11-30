from django.contrib import admin
from .models import Buyer, Game

# Register your models here.
# name - Admin, password - 1212

admin.site.register(Buyer)
admin.site.register(Game)
