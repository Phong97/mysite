from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Student)