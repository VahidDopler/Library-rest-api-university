from django.contrib import admin

from .models import Book, Cage, Author

admin.site.register(Book)
admin.site.register(Cage)
admin.site.register(Author)
# Register your models here.
