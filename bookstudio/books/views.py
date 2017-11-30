import pytesseract
from unidecode import unidecode
from PIL import Image as Img
from PIL import ImageEnhance, ImageFilter

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from . forms import BookForm, ImageForm
from .models import Book
from bookstudio.users.models import User
from django.core.mail import send_mail


def book_home(request):
    book = request.GET.get('q', '')
    all_books = Book.objects.all()
    if book:
        all_books = all_books.filter(name__icontains=book)
    else:
        all_books = all_books.filter(user_name=request.user)
    return render(request, 'books/basefile.html', {'all_books': all_books})


def book_mail(request, book_id):
    print(request.user.username)
    print(request.user.email)
    book = Book.objects.get(pk=book_id)
    user_details = User.objects.get(username=book.user_name)
    print(user_details.email)
    send_mail('Book buyer', 'The following user was intersted in your book' + ' name: '+ request.user.username + request.user.phone_number, 'bookstudio6@gmail.com' , [user_details.email], fail_silently=False, )


def book_search(request):
    image_form = ImageForm(request.FILES or None)
    if request.method == 'POST':
        image = request.FILES.get("file_name")
        with Img.open(image) as infile:
            text = pytesseract.image_to_string(infile)
            li = [s for s in text.splitlines() if s.strip()]
            li = li[:5]
        print(li)
        all_books = Book.objects.all()
        all_books = all_books.filter(name__icontains=li[0])
        return render(request, 'books/basefile.html', {'all_books': all_books})
    return render(request, 'books/search_book.html', {'book_form': image_form})


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
