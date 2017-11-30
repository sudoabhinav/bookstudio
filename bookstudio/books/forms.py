from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from . models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'pages', 'price', 'description', 'file_name')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Book name'})
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.fields['publisher'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Publisher'})
        self.fields['pages'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pages'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Price'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
        self.fields['file_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Book Image'})

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        name = cleaned_data.get("name", "")
        author = cleaned_data.get("author", "")
        price = cleaned_data.get("price", "")
        if not name:
            raise forms.ValidationError("name is required")
        elif not author:
            raise forms.ValidationError("author name is required")
        elif not price:
            raise forms.ValidationError("price is required")
        else:
            return cleaned_data
