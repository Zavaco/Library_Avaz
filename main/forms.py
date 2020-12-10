from django import forms
from .models import LibUser, LibAdmin, Book
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = LibUser
        fields = [
            'user_name',
            'email',
            'user_image',
            'password',
        ]
        widgets = {
            'user_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Your Name',
                    'id': 'validationCustom01'
                }
            ),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your E-mail',
                                             'id': 'validationCustomUsername'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'validationCustom02',
                                               'placeholder': 'Your password'}),

            'user_image': forms.ClearableFileInput(attrs={'class': 'form-control'})

        }


class LibAdminForm(ModelForm):
    class Meta:
        model = LibAdmin
        fields = '__all__'

        widgets = {
            "take_date": DateInput(),

            "give_date": DateInput(),

        }

    def __init__(self, *args, **kwargs):
        super(LibAdminForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['book'].queryset = Book.objects.filter(book_status=True)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
