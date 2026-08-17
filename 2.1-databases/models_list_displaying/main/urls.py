from django.contrib import admin
from django.urls import path
from books.views import books_view, book_list_by_date


urlpatterns = [
    path('', books_view, name='book_list'),
    path('<int:year>-<int:month>-<int:day>/', book_list_by_date, name='book_list_by_date'),
    path('admin/', admin.site.urls),
]