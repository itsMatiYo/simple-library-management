from urllib.parse import unquote

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from books.forms import CreateBookRecordForm, FileForm
from books.models import Book, BookRecord, User


# ! Book Views
class BookCreate(CreateView):
    model = Book
    template_name = "books/create.html"
    fields = ["title", "author"]


class BookList(ListView):
    queryset = Book.objects.all()
    template_name = "books/list.html"
    context_object_name = "books"


class BookDetail(DetailView):
    model = Book
    template_name = "books/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookRecords"] = self.get_object().bookRecords.all()
        return context


class BookUpdate(UpdateView):
    model = Book
    template_name = "books/update.html"
    fields = ["title", "author"]


class BookDelete(DeleteView):
    model = Book
    template_name = "books/delete.html"
    success_url = reverse_lazy("bookList")


# ! User Views
class UserkCreate(CreateView):
    model = User
    template_name = "users/create.html"
    fields = [
        "name",
    ]


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "users/list.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = User
    template_name = "users/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = self.get_object().bookRecords.all()
        return context


class UserUpdate(UpdateView):
    model = User
    template_name = "users/update.html"
    fields = [
        "name",
    ]


class UserDelete(DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("userList")


# ! Book Record
class BookRecordCreate(CreateView):
    template_name = "bookrs/create.html"
    model = BookRecord
    form_class = CreateBookRecordForm
    success_url = reverse_lazy("bookRecordList")


class BookRecordList(ListView):
    queryset = BookRecord.objects.all()
    template_name = "bookrs/list.html"
    context_object_name = "bookRecords"


class BookRecordDetail(DetailView):
    queryset = BookRecord.objects.all()
    template_name = "bookrs/detail.html"
    context_object_name = "bookRecord"


class BookRecordReturn(View):
    template_name = "bookrs/return.html"
    model = BookRecord

    def get(self, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=self.kwargs["pk"])
        context = {}
        context["obj"] = obj
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=self.kwargs["pk"])
        obj.setReturnTime()
        return redirect("bookRecordDetail", obj.pk)


class BookRecordDelete(DeleteView):
    model = BookRecord
    template_name = "bookrs/delete.html"
    context_object_name = "bookRecord"
    success_url = reverse_lazy("bookRecordList")


# ! File Views
class BookFileUpload(View):
    template_name = "createFile/form.html"

    def get(self, *args, **kwargs):
        form = FileForm()
        context = {"form": form}
        context["type"] = "books.txt"
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = FileForm(self.request.POST, self.request.FILES)
        context = {"form": form}
        if form.is_valid():
            titles = self.request.FILES.get("file").readlines()
            for title in titles:
                title = title.decode("utf-8")
                if title.strip():
                    Book.objects.create(title=title)
            return redirect("bookList")
        return render(self.request, self.template_name, context)


class UserFileUpload(View):
    template_name = "createFile/form.html"

    def get(self, *args, **kwargs):
        form = FileForm()
        context = {"form": form}
        context["type"] = "users.txt"

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = FileForm(self.request.POST, self.request.FILES)
        context = {"form": form}
        if form.is_valid():
            names = self.request.FILES.get("file").readlines()
            for name in names:
                name = name.decode("utf-8")
                if name:
                    User.objects.create(name=name)
            return redirect("userList")
        return render(self.request, self.template_name, context)
