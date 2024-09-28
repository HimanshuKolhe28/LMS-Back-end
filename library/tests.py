from django.test import TestCase

# Create your tests here.

data = [
    {
        "student_id":1,
        "student_name": "Himanshu kolhe",
        "book_issued": [
            {
                "book_id": 1,
                "book_name": "Python",
                "Issue_date": "",
                "due_date": "",
            },
            {
                "book_id": 2,
                "book_name": "Python",
                "Issue_date": "",
                "due_date": "",
            },
        ]   
    },
    {
        "student_id":2,
        "student_name": "Mayur Fegde",
        "book_issued": [
            {
                "book_id": 1,
                "book_name": "Python advance",
                "Issue_date": "",
                "due_date": "",
            },
            {
                "book_id": 2,
                "book_name": "Python Basic",
                "Issue_date": "",
                "due_date": "",
            },
        ]   
    }
]


from django.db import models

# Create your models here.


class Employee (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    position = models.CharField(max_length=50)

    def __str__(self):    
        return f'{self.name}'

    def obj_to_dict(self):
        return dict (
            name = self.name,
            email = self.email,
            phone = self.phone,
            position = self.position
        )



