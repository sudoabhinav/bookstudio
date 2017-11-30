from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_home, name="book_home"),
    url(r'^search/$', views.book_search, name="book_search"),
    url(r'^buy/(?P<book_id>[0-9]*)/$', views.book_mail, name="book_mail"),
    url(r'^add/$', views.add_book, name="book_add"),
    url(r'^books_list/$', views.books_list, name="books_list"),
    url(r'^(?P<book_id>[0-9]+)/book_edit/$', views.book_edit, name="book_edit"),
    url(r'^(?P<book_id>[0-9]+)/book_remove/$', views.book_remove, name="book_remove")
]
