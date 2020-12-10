from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, LibAdminForm, BookForm, CreateUserForm
from .models import LibUser, LibAdmin
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import Book

app_name = 'main'


def main(request):
    return render(request, 'main/index.html')


class UserFormView(generic.FormView):
    form_class = UserForm
    template_name = 'main/create_user.html'

    def form_valid(self, form):
        form.save()

        return super(UserFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('userlist')


def success(request):
    return render(request, "main/user_list.html")


def lib_user(request):
    form = LibAdminForm()

    if request.method == 'POST':
        form = LibAdminForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data.get('book')
            # book = Book.objects.filter(id=book.id).update(book_status=False)
            book.book_status = False
            book.save()
            form.save()
            return redirect('/orderlist')
    context = {
        'form': form
    }
    return render(request, 'main/lib_user.html', context)


def user_list(request):
    customer = LibUser.objects.all()
    return render(request, 'main/user_list.html', {'customer': customer})


class UserUpdateView(UpdateView):
    model = LibUser
    fields = '__all__'
    widgets = {
        'user_name': forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        'email': forms.EmailInput(
            attrs={'class': 'form-control'}),
        'password': forms.TextInput(
            attrs={'class': 'form-control'}),

        'user_image': forms.ClearableFileInput(
            attrs={'class': 'form-control'})

    }

    def get_success_url(self):
        return reverse('userlist')


class UserDeleteView(DeleteView):
    model = LibUser
    fields = '__all__'

    def get_success_url(self):
        return reverse('userlist')


def book_list(request):
    book_info = Book.objects.all()
    return render(request, 'main/book_list.html', {'book_info': book_info})


def book_update(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/booklist/')
    context = {
        'form': form
    }

    return render(request, 'main/book_update.html/', context)


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('booklist')


class BookDeleteView(DeleteView):
    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('booklist')


def search(request):
    queryset_list = Book.objects.all()
    if 'book_title' in request.GET:
        book_title = request.GET['book_title']
        if book_title:
            queryset_list = queryset_list.filter(book_title__icontains=book_title)

    context = {
        'result': queryset_list,
        'values': request.GET
    }

    return render(request, "main/search.html", context)


def search_user(request):
    queryset_list = LibUser.objects.all()
    if 'user_name' in request.GET:
        user_name = request.GET['user_name']
        if user_name:
            queryset_list = queryset_list.filter(user_name__icontains=user_name)

    context = {
        'result': queryset_list,
        'values': request.GET
    }

    return render(request, "main/user_search.html", context)


def order_list(request):
    order = LibAdmin.objects.all()
    return render(request, 'main/order_list.html', {'order': order})


class OrderUpdateView(UpdateView):
    model = LibAdmin
    fields = '__all__'

    def get_success_url(self):
        return reverse('order_list')


def delete_order(request, pk):
    order = LibAdmin.objects.get(id=pk)
    context = {'order': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/orderlist/')
    return render(request, 'main/order_delete.html', context)


def history(request):
    order = LibAdmin.objects.filter(returned=True)
    return render(request, 'main/history.html', {'order': order})


class BookDetailView(DetailView):
    model = Book
    template_name = 'main/book_read.html'
    context_object_name = 'book'


class UserDetailView(DetailView):
    model = LibUser
    template_name = 'main/customer_read.html'
    context_object_name = 'customer'


class OrderDetailView(DetailView):
    model = LibAdmin
    template_name = 'main/order_read.html'
    context_object_name = 'order'


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'The account was created successfully !')
            redirect('login')
    context = {
        'form': form
    }
    return render(request, 'permit/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

        context = {}
    return render(request, 'permit/login.html', context)
