from django.shortcuts import render
from .models import Book
from datetime import datetime



def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books,
    }
    return render(request, template, context)


def book_list_by_date(request, year, month, day):
    """Отображение книг за конкретную дату с навигацией по соседним датам"""
    target_date = datetime(year, month, day).date()

    # Книги за указанную дату
    books = Book.objects.filter(pub_date=target_date)

    # Находим ближайшую предыдущую дату, у которой есть книги
    prev_date = Book.objects.filter(
        pub_date__lt=target_date
    ).order_by('-pub_date').values_list('pub_date', flat=True).first()

    # Находим ближайшую следующую дату, у которой есть книги
    next_date = Book.objects.filter(
        pub_date__gt=target_date
    ).order_by('pub_date').values_list('pub_date', flat=True).first()

    template = 'books/book_list_by_date.html'
    context = {
        'books': books,
        'current_date': target_date,
        'prev_date': prev_date,
        'next_date': next_date,
        'has_books': books.exists(),
    }
    return render(request, template, context)