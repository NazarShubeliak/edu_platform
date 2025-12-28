from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LibraryItem

# Create your views here.
@login_required
def library_list(request):
    books = LibraryItem.objects.all().order_by("title")

    grouped_books = {}
    for book in books:
        first_latter = book.title[0].upper()
        grouped_books.setdefault(first_latter, []).append(book)

    return render(request, "library/library_list.html", {"grouped_books": grouped_books})

@login_required
def upload_book(request):
    if request.user.role not in ["admin", "teacher"]:
        return redirect("home")

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        file = request.FILES.get("file")

        LibraryItem.objects.create(
            title=title,
            author=author,
            file=file,
            uploaded_by=request.user
        )
        return redirect("library_list")

    return render(request, "library/upload_book.html")

@login_required
def delete_book(request, pk):
    if request.user.role not in ["admin", "teacher"]:
        return redirect("home")

    book = get_object_or_404(LibraryItem, pk=pk)
    if request.user == book.uploaded_by or request.user == "admin":
        book.delete()
    return redirect("library_list")
