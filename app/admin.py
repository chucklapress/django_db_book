from django.contrib import admin
from app.models import Book, Chapter, Character, Sidekick, Item

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Sidekick)
admin.site.register(Item)
