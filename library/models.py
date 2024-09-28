from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def obj_to_dict(self):

        return dict(
            id = self.id,
            name = self.name,
            author_name = self.author_name,
            publisher = self.publisher,
            quantity = self.quantity,
        )


class BookTracker(models.Model):
    student = models.ForeignKey('lms_backend.Student', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_timestamp = models.DateTimeField(auto_now=True)
    due_timestamp = models.DateTimeField()
    submit_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.student.name} | {self.book.name}'


    def obj_to_dict(self):
        return dict(
            id=self.id,
            student_id = self.student.id,
            student_name = self.student.name,
            book_id = self.LibBook.id,
            book_name= self.LibBook.name,
            issue_timestamp = self.issue_timestamp.strftime("%Y-%b-%d %H:%M"),
            due_timestamp = self.due_timestamp.strftime("%Y-%b-%d %H:%M"),
            submit_timestamp=self.submit_timestamp.strftime("%Y-%b-%d %H:%M") if self.submit_timestamp else None,
        )