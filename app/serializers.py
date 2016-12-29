from rest_framework import serializers
from app.models import Book, Chapter, Character, Sidekick, Item




class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        depth = 3
        fields = ('id','title','author')

class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        depth = 3
        fields = ('id','title','book')

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        depth = 3
        fields = ('id','name','appears')

class SidekickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sidekick
        depth = 3
        fields = ('id','name','helps')

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        depth = 4
        fields = ('id','The_One_Ring', 'Gandalf','Silmarils')
