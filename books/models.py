from django.db import models
from django.utils import timezone


class BookRecord(models.Model):
    related_name = "bookRecords"
    book = models.ForeignKey(
        "books.Book", related_name=related_name, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "books.User", related_name=related_name, on_delete=models.CASCADE
    )
    borrowingTime = models.DateTimeField(auto_now_add=True)
    returnTime = models.DateTimeField(blank=True, null=True)

    def setReturnTime(self):
        self.returnTime = timezone.now()
        self.save()

    class Meta:
        ordering = [
            "-borrowingTime",
        ]

    def __str__(self) -> str:
        return super().__str__()


class User(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    title = models.CharField(max_length=512)
    # author = models.ForeignKey(Author, blank=True)
    author = models.CharField(max_length=400, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)

    def createBookRecord(self, user):
        if self.isFreeToBorrow():
            BookRecord.objects.create(book=self, user=user)
        else:
            raise Exception("This book is occupied")

    def returnBook(self):
        if self.bookRecords.filter(returnTime=None).exists():
            br = self.bookRecords.get(returnTime=None)
            br.setReturnTime()
        else:
            raise Exception("This book is not occupied")

    def isFreeToBorrow(self) -> bool:
        try:
            return not (self.bookRecords.filter(returnTime=None).exists())
        except:
            return True

    def __str__(self) -> str:
        if self.author:
            return f"{self.title} from {self.author}"
        else:
            return f"{self.title}"
