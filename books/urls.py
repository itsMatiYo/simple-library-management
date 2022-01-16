from django.urls import path

from books.views import (
    BookCreate,
    BookDelete,
    BookDetail,
    BookFileUpload,
    BookList,
    BookRecordCreate,
    BookRecordDelete,
    BookRecordDetail,
    BookRecordList,
    BookRecordReturn,
    BookUpdate,
    UserDelete,
    UserDetail,
    UserFileUpload,
    UserkCreate,
    UserList,
    UserUpdate,
)

urlpatterns = [
    # books urls
    path("books/create/", BookCreate.as_view(), name="bookCreate"),
    path("books/", BookList.as_view(), name="bookList"),
    path("books/<int:pk>/", BookDetail.as_view(), name="bookDetail"),
    path("books/<int:pk>/edit/", BookUpdate.as_view(), name="bookEdit"),
    path("books/<int:pk>/delete/", BookDelete.as_view(), name="bookDelete"),
    # users urls
    path("users/create/", UserkCreate.as_view(), name="userCreate"),
    path("users/", UserList.as_view(), name="userList"),
    path("users/<int:pk>/", UserDetail.as_view(), name="userDetail"),
    path("users/<int:pk>/edit/", UserUpdate.as_view(), name="userEdit"),
    path("users/<int:pk>/delete/", UserDelete.as_view(), name="userDelete"),
    # bookrecord
    path(
        "bookrecord/<int:pk>/return/",
        BookRecordReturn.as_view(),
        name="bookRecordReturn",
    ),
    path("bookrecord/create/", BookRecordCreate.as_view(), name="bookRecordCreate"),
    path("bookrecord/", BookRecordList.as_view(), name="bookRecordList"),
    path("bookrecord/<int:pk>/", BookRecordDetail.as_view(), name="bookRecordDetail"),
    path(
        "bookrecord/<int:pk>/delete/",
        BookRecordDelete.as_view(),
        name="bookRecordDelete",
    ),
    # files
    path("books/file/", BookFileUpload.as_view(), name="bookFileUpload"),
    path("users/file/", UserFileUpload.as_view(), name="userFileUpload"),
]
