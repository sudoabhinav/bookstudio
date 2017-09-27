from django.shortcuts import render, get_object_or_404

from . forms import BookForm
from .models import Book


def book_home(request):
    return render(request, 'books/basefile.html')


def add_book(request):
    book_form = BookForm(request.POST or None)
    if request.method == 'POST':
        if book_form.is_valid():
            detail = book_form.save(commit=False)
            detail.user_name = request.user
            detail.save()
            return render(request, 'books/basefile.html')
    return render(request, 'books/add_book.html', {'book_form': book_form})


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
