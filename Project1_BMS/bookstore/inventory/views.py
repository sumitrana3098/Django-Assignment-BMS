from django.shortcuts import get_object_or_404, redirect, render
from inventory.forms import BookForm
from inventory.models import Book

# Create your views here.
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'inventory/add_book.html', {'form': form})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'inventory/update_book.html', {'form': form})

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})


    # books = Book.objects.all()
    # return render(request, 'inventory/book_list.html', {'books': books})
