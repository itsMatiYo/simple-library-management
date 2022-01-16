from django import forms

from books.models import BookRecord


class CreateBookRecordForm(forms.ModelForm):
    class Meta:
        model = BookRecord
        fields = [
            "book",
            "user",
        ]

    def clean_book(self):
        book = self.cleaned_data.get("book")
        if book.isFreeToBorrow():
            return book
        else:
            self.add_error("book", "Book is occupied.")


class FileForm(forms.Form):
    file = forms.FileField(required=True)

