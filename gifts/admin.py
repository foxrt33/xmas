from django.contrib import admin
from gifts.models import Person
from gifts.models import Exception
from gifts.models import Gift

# Register your models here.

admin.site.register(Person)
admin.site.register(Exception)
admin.site.register(Gift)
