from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_home, name="book_home"),
    url(r'^add/$', views.add_book, name="book_add"),
    url(r'^books_list/$', views.books_list, name="books_list"),
    url(r'^(?P<book_id>[0-9]+)/book_edit/$', views.book_edit, name="book_edit")
]
