from Tools.demo.mcast import sender
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Book(models.Model):
    book_title = models.CharField(max_length=100, null=True)
    published_date = models.DateField(null=True, blank=True)
    book_status = models.BooleanField(null=True, default=True)
    author_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class LibUser(models.Model):
    user_name = models.CharField(null=True, max_length=100)
    user_status = models.BooleanField(default=True)
    user_image = models.ImageField(upload_to='customer', null=True, blank=True)
    book_info = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class LibAdmin(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(LibUser, on_delete=models.CASCADE, null=True, blank=True)
    take_date = models.DateField(null=True, blank=True)
    give_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    returned = models.BooleanField(null=True)

    def __str__(self):
        return self.customer.user_name

    class Meta:
        verbose_name = 'Library_Admin'
        verbose_name_plural = 'Library_Admins'


class OrderLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(LibUser, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.book.book_title


@receiver(post_save, sender=LibAdmin)
def order_log(sender, instance, **kwargs):
    OrderLog.objects.create(book=instance.book, customer=instance.customer)
