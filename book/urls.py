"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import IndexView, BookListAPIView, ChapterListAPIView, CharacterListAPIView, SidekickListAPIView, ItemListAPIView
from app.views import BookDetailAPIView, ChapterDetailAPIView, CharacterDetailAPIView, SidekickDetailAPIView, ItemDetailAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^book/$', BookListAPIView.as_view(), name="book_list_api_view"),
    url(r'^book/(?P<pk>\d+)/$', BookDetailAPIView.as_view(), name="book_detail_api_view"),
    url(r'^chapter/$', ChapterListAPIView.as_view(), name="chapter_list_api_view"),
    url(r'^chapter/(?P<pk>\d+)/$', ChapterDetailAPIView.as_view(), name="chapter_detail_api_view"),
    url(r'^character/$', CharacterListAPIView.as_view(), name="character_list_api_view"),
    url(r'^character/(?P<pk>\d+)/$', CharacterDetailAPIView.as_view(), name="character_detail_api_view"),
    url(r'^sidekick/$', SidekickListAPIView.as_view(), name="sidekick_list_api_view"),
    url(r'^sidekick/(?P<pk>\d+)/$', SidekickDetailAPIView.as_view(), name="sidekick_detail_api_view"),
    url(r'^item/$', ItemListAPIView.as_view(), name="item_list_api_view"),
    url(r'^item/(?P<pk>\d+)/$', ItemDetailAPIView.as_view(), name="item_detail_api_view")
]
