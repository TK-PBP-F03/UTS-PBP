from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from main.models import Book

# Create your views here.

def show_reviews(request):
  book = Book.objects.order_by("?")[:6]
  
  context = {'data': book}

  return render(request, "reviews.html", context)

def book_review(request, pk):
  try:
    book = get_object_or_404(Book, pk=pk)
    return render(request, "review.html", {"book": book})
  except Http404:
    return HttpResponse("berhasil")

