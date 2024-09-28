
from django.urls import path
from library.views import create_student, read_student, update_student, book_create, \
     read_book, issue_book, read_booktracker, \
     get_book,submit_book,book_submited, book_details, create_libraryid, create_subject, read_subject, \
     update_department, update_student_subjects,student_detail

urlpatterns = [
     path('create_student',create_student),
     path('read_student',read_student),
     path('update_student/<int:pk>',update_student),
     path('book_create',book_create),
     path('read_book',read_book),
     path('issue_book',issue_book),
     path('read_booktracker', read_booktracker),
     
     path('get_book',get_book),
     path('submit_book/<int:pk>',submit_book),
     path('book_submited/<int:pk>',book_submited),
     path('book_details', book_details),
     path('create_libraryid',create_libraryid),
     path('create_subject',create_subject), 
     path('read_subject',read_subject),
     path('update_department',update_department),
     path('update_student_subjects/<int:pk>', update_student_subjects),
     path('student_detail/<int:pk>',student_detail),
    
]   
