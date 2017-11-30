from django.shortcuts import render, get_object_or_404
from django.http import Http404

from . forms import BookForm
from .models import Book


def book_home(request):
    book = request.GET.get('q', '')
    all_books = Book.objects.all()
    if book:
        all_books = all_books.filter(name__icontains=book)
    else:
        all_books = all_books.filter(user_name=request.user)
    return render(request, 'books/basefile.html', {'all_books': all_books})


def add_book(request):
    book_form = BookForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if book_form.is_valid():
            detail = book_form.save(commit=False)
            detail.user_name = request.user
            detail.save()
            return render(request, 'books/basefile.html')
    return render(request, 'books/add_book.html', {'book_form': book_form})


def book_remove(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except:
        raise Http404
    book.delete()
    all_books = Book.objects.all()
    books = all_books.filter(user_name=request.user.id)
    return render(request, 'books/book_list.html', {'books': books})


def books_list(request):
    all_books = Book.objects.all()
    books = all_books.filter(user_name=request.user.id)
    return render(request, 'books/book_list.html', {'books': books})


def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book_form = BookForm(request.POST or None, instance=book)

    if request.method == 'POST':
        if book_form.is_valid():
            details = book_form.save(commit=False)
            details.user_name = request.user
            details.save()
            return render(request, 'books/basefile.html')
    return render(request, 'books/edit_book.html', {'book_form': book_form})
