from django import forms
from django.forms import ModelForm
from . models import Book 


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'pages', 'price', 'description')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Book name'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['publisher'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Publisher'})
        self.fields['pages'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pages'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Price'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        return cleaned_data
