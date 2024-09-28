import json
import csv


from library.models import  Book, BookTracker
from django.http import JsonResponse
from django.db.models.functions import Lower
 

from datetime import datetime, timedelta

# create (student)


def create_student(request,pk= None):
    if request.method == "POST":
        params = json.loads (request.body)


        instance = Student.objects.create (
        name=params.get('name'),
        branch=params.get('branch'),
        year=params.get('year'),
        batch=params.get('batch'),
        roll_no=params.get('roll_no'),
        phone=params.get('phone'),
        email=params.get('email')
        )

        return JsonResponse({
            "message": "New Student is created",
            "data": instance.obj_to_dict()

        })


# read (student)

def read_student (request,pk= None):
    if request.method == "GET":
        params= request.GET
        response = []
        branch = params.get('branch')

        qeryset = Student.objects.order_by("id")

        if branch:
            qeryset = qeryset.filter(branch=branch)
        
        if pk:
            qeryset = qeryset.filter(id=pk)

        for instance in qeryset:
            response.append(instance.obj_to_dict())
    
        return JsonResponse({
            "message": "success",
            "data": response
        })


# Update (Student)

def update_student (request,pk = None):
    if request.method == "PATCH":
        params= json.loads(request.body)


        name=params.get('name')
        branch=params.get('branch')
        year=params.get('year')
        batch=params.get('batch')
        roll_no=params.get('roll_no')
        phone=params.get('phone')

        email=params.get('email')

        instance = Student.objects.get(id=pk)

        if name:
            instance.name = name

        if branch:
            instance.branch = branch
        instance.save(

        )
        return JsonResponse({
            "message": "success",
            "data": instance.obj_to_dict()
        })
     

def book_create (request,pk =None):

    if request.method == "POST":

        params  = json.loads(request.body)


        book_name = params.get('name')
        author_name = params.get('author_name')
        
        publisher = params.get('publisher')
        quantity = params.get('quantity')


        instance = LibBook.objects.create(
            name = book_name,
            author_name = author_name,
            publisher = publisher,
            quantity = quantity)

            
        return JsonResponse({

            "message": "Successfully done",
            "data": instance.obj_to_dict()
            })



def read_book (request,pk= None):
    if request.method == "GET":
        params= request.GET
        response = []
        branch = params.get('name')

        qeryset = BookTracker.objects.all()

        if branch:
            qeryset = qeryset.filter(name=name)
        
        if pk:
            qeryset = qeryset.filter(id=pk)

        for instance in qeryset:
            response.append(instance.obj_to_dict())
    
        return JsonResponse({
            "message": "success",
            "data": response
        })




# create BookTracker
def issue_book(request,pk= None):
    if request.method == "POST":
        params = json.loads (request.body)
        student_id = params.get('student_id')
        book_id = params.get('book_id')

        stud_obj = Student.objects.get(id=student_id)
        book_obj = LibBook.objects.get(id=book_id)
        
        issue_timestamp = datetime.today()
        due_timestamp = issue_timestamp + timedelta(days=7)
        print("due_timestamp", due_timestamp)
        instance = BookTracker.objects.create(
            student=stud_obj,
            LibBook=book_obj,
            issue_timestamp=issue_timestamp,
            due_timestamp = due_timestamp,
            is_submited=False
            

        )

        return JsonResponse({

            "message": "New issue book  is created",
            "data": instance.obj_to_dict(),

        })


# read booktracker

def read_booktracker(request,pk=None):
    if request.method=="GET":
        params= request.GET
        response = []

        
        student_id = params.get('student_id')
        book_id = params.get ('book_id')

        queryset = BookTracker.objects.order_by(Lower("student__id").desc())

        # if student_id:

        #     print("Name Filter Applying", student_id)
        #     queryset = queryset.filter(student_id=student_id)

        # if book_id:
        #     print("Book ID Filter Applying", book_id)
        #     queryset = queryset.filter(LibBook__id=book_id)
        print(queryset)

        if pk:
            print("Pk filter applying", pk)
            queryset = queryset.filter(id=pk)

        for instance in queryset:

            response.append(instance.obj_to_dict())
    
        return JsonResponse({
            "message": "successfully read",
            "data": response
        })
''
'''
def get_book_issued_from_student(request):

    student_queryset = Student.objects.all()
    book_tracker_queryset = BookTracker.objects.all()

    response = []
    for student in student_queryset:
        
        book_issued = []
        for book_issue in book_tracker_queryset.filter(student=student):
            book_issued.append(dict(
                id=book_issue.id,
                book_id=book_issue.LibBook.id,
                book_name=book_issue.LibBook.name,
            ))
        response.append(dict(
            student_id=student.id,
            student_name=student.name,
            book_issued=book_issued,
        ))

    return JsonResponse(dict(
        status=True,
        data=response
    ))

'''
def get_book(request):
    student_queryset = Student.objects.all()
    response=[]
 
        
    for student in student_queryset:
        book_issued = []
        for book_issue in BookTracker.objects.filter(student=student):
            book_issued.append(dict(
                id=book_issue.id,
                book_id=book_issue.LibBook.id,
                book_name=book_issue.LibBook.name,
                issue_timestamp=book_issue.issue_timestamp,
                due_timestamp=book_issue.due_timestamp,
                is_submited=book_issue.is_submited,
                submit_timestamp=book_issue.submit_timestamp,
                
            ))
        response.append(dict(
            student_id= student.id,
            student_name= student.name,
            no_of_book_issued=len(book_issued),
            #no_of_book_issued_new=BookTracker.objects.filter(student=student).count(),
            book_issued= book_issued, 
        ))

    return JsonResponse(dict(
        status=True,
        data= response
    ))



def submit_book(request, pk=None): 
    instance = BookTracker.objects.get(id=pk)
    instance.is_submited = True
    instance.submit_timestamp = datetime.now()
    instance.save()

    return JsonResponse(dict(
        status=True,
        data=instance.obj_to_dict()
    ))



def book_submited(request, pk=None):
    instance = BookTracker.objects.get(id=pk)
    instance.is_submited = True
    instance.submit_timestamp = datetime.now()
    instance.save()

    return JsonResponse(dict(
        status=True,
        data=instance.obj_to_dict()
    ))



def book_details(request):
    
    bookQuerySet = LibBook.objects.all()
    bookTrackerQuerySet = BookTracker.objects.all()
    responsse = []
    for book_instance in bookQuerySet:
        responsse.append(dict(
            book_id=book_instance.id,
            book_name=book_instance.name,
            data=[{
                    "student_id": book_tracker.student.id, 
                    "student_name": book_tracker.student.name,
                    "branch": book_tracker.student.branch
                } for book_tracker in bookTrackerQuerySet.filter(LibBook=book_instance)]
    

        ))

    return JsonResponse(dict(
        status=True,
        data=responsse,
    ))


def book_details (request):
    bookQuerySet = BookTracker.objects.all()
  #  bookTrackerQuerySet = BookTracker.objects.all()
    response = []
    for book_instance in bookQuerySet:
        response.append(dict(
            book_id = book_instance.id,
            book_name = book_instance.name,
            data=[{
                "student_id": book_tracker.student.id,
                "student_name" : book_tracker.student.name,
                "branch": book_tracker.student.branch
            }
            for book_tracker in bookTrackerQuerySet.filter(LibBook=book_instance)]
        ))

    return JsonResponse(dict(
        status - True,
        data = response,  
    ))



def create_libraryid(request,pk= None):
    if request.method == "POST":
        params = json.loads (request.body)


        instance = Student.objects.create (
        name=params.get('Student_name'),
        branch=params.get('branch'),
        year=params.get('year'),
        batch=params.get('batch'),
        roll_no=params.get('roll_no'),
        phone=params.get('phone'),
        email=params.get('email')
        )   


        book_name = params.get('name')
        author_name = params.get('author_name')
        publisher = params.get('publisher')
        quantity = params.get('quantity')


        instance = LibBook.objects.create(
            name = book_name,
            author_name = author_name,
            publisher = publisher,
            quantity = quantity
            )

        instance = BookTracker.objects.create(
            
        )



        return JsonResponse({
            "message": "New Student is created",
            "data": instance.obj_to_dict()

        })
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


def create_subject (request,):
    if request.method == "POST":
        params = json.loads (request.body)

    instance = Subject.objects.create(
        title = params.get('title'),
        subject_book = params.get('subject_book'),
        std = params.get('std')

    )
    
    return JsonResponse({

        "message": "New subject is created",
        "data": instance.obj_to_dict()

        })


def read_subject (request,pk= None):
    if request.method == "GET":
        params= request.GET
        response = []
        subject_book = params.get('subject_book')

        qeryset = Subject.objects.all()

        if subject_book:
            qeryset = qeryset.filter(subject_book=subject_book)
        
        if pk:
            qeryset = qeryset.filter(id=pk)

        for instance in qeryset:
            response.append(instance.obj_to_dict())
    
        return JsonResponse({
            "message": "success",
            "data": response
        })



def update_department(request):
    if request.method == "PATCH":
        # branch=params.get('branch')
        # year=params.get('year')
        # batch=params.get('batch')
        # roll_no=params.get('roll_no')
        # phone=params.get('phone')
        #  email=params.get('email')

        
        #  instance = Student.objects.get(id=pk)

        #  if subject:
        #      instance.subject = subject

        #  instance.save()

         return JsonResponse({
             "message": "success_updated data",
             "data": instance.obj_to_dict()
        })

def update_student_subjects(request, pk=None):
    print("API Call")
    params = json.loads(request.body)
    subjects_ids = params.get('subjects_ids')

    student_instance = Student.objects.get(id=pk)

    
    if subjects_ids:
        subjects = Subject.objects.filter(id__in=subjects_ids)
        student_instance.subjects.clear()
        student_instance.subjects.add(*subjects_ids)


    return JsonResponse({
        "message": "it done",
        "data":student_instance.obj_to_dict() 
    })

def student_detail(request, pk):
    student = Student.objects.get(pk=3)
    subjects = Subject.objects.filter(id__in=[2, 3])
    student.subjects.add(*subjects)

    
    return JsonResponse({
        "message":"student_detail many to many "


    }) 
    