from django.test import TestCase
from django.utils import timezone

from books import models as md


class BookTest(TestCase):
    def setUp(self) -> None:
        self.user3 = md.User.objects.create(name="moot")
        self.nowTime = timezone.now()
        book = md.Book.objects.create(
            title="test",
            author="dasta",
        )
        md.BookRecord.objects.create(book=book, user=self.user3)

    def testBookProperties(self):
        book = md.Book.objects.get(id=1)
        self.assertEqual(book.title, "test")
        self.assertEqual(book.author, "dasta")
        self.assertEquals(book.creationDate.second, self.nowTime.second)
        self.assertEqual(book.isFreeToBorrow(), False)
        self.assertEqual(str(book), "test from dasta")

    def testBookRecord(self):
        br = md.BookRecord.objects.get(id=1)
        self.assertEqual(br.book.id, 1)
        self.assertEqual(br.user.name, "moot")

    def testReturnBook(self):
        book = md.Book.objects.get(id=1)
        now = timezone.now()
        book.returnBook()
        br = md.BookRecord.objects.get(id=1)
        self.assertEqual(br.returnTime.second, now.second)
        self.assertEqual(book.isFreeToBorrow(), True)
        self.assertEqual(br.book, book)

    def testCreateBookRecord(self):
        book = md.Book.objects.get(id=1)
        try:
            br2 = book.createBookRecord(user="author1")
        except Exception as e:
            self.assertEqual(str(e), "This book is occupied")
        book.returnBook()
        book.createBookRecord(user=self.user3)


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user1 = md.User.objects.create(name="mahmood")
        self.user2 = md.User.objects.create(name="alisha")
        return super().setUp()

    def testNameAndStr(self):
        self.assertEqual(str(self.user1), "mahmood")
        self.assertEqual(self.user2.name, "alisha")
