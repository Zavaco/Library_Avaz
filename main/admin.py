from django.contrib import admin
from .models import Book
from .models import LibAdmin, LibUser,OrderLog
# Register your models here.


admin.site.register(Book)
admin.site.register(LibUser)
admin.site.register(OrderLog)


@admin.register(LibAdmin)
class Avaz(admin.ModelAdmin):
    list_display = ['customer', 'book', 'take_date', 'give_date']
