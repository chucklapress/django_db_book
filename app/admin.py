from django.contrib import admin
from app.models import Book, Chapter, Character, Sidekick

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Sidekick)
