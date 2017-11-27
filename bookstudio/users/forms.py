from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name')
    phone_number = forms.CharField(max_length=11, label='Mobile number')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()