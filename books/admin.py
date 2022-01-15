from django.contrib import admin
from django.views.generic.edit import UpdateView

from books import models

admin.site.register(models.Book)
admin.site.register(models.BookRecord)
