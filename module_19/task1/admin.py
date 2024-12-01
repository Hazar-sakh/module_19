from django.contrib import admin
from .models import *

# Register your models here.
# name - Admin, password - 1212

admin.site.register(Player)
admin.site.register(Team)
