from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Book

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        # Start with all books
        queryset = super().get_queryset()
        
        # Implement search by title or author
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(author__icontains=search_query)
        
        return queryset


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date', 'genre']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_date', 'genre']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
