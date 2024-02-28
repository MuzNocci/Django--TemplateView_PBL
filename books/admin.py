from django.contrib import admin
from books import models



@admin.register(models.Books)
class AuthorAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('title',), }
