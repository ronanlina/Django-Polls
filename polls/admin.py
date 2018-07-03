from django.contrib import admin
from .models import Question

# Register your models here.
# Models that can be used for CRUD applications
# on admin.

admin.site.register(Question)
