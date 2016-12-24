from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from app.models import Book, Chapter, Character, Sidekick, Item
from app.serializers import BookSerializer, ChapterSerializer, CharacterSerializer, SidekickSerializer, ItemSerializer

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterListAPIView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class CharacterListAPIView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class SidekickListAPIView(generics.ListCreateAPIView):
    queryset = Sidekick.objects.all()
    serializer_class = SidekickSerializer

class SidekickDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sidekick.objects.all()
    serializer_class = SidekickSerializer

class ItemListAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
