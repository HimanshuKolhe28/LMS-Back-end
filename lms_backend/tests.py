# import json



# # CREATE (Student)


# from lms_backend.models import Student, Book, BookIssueTracker
# from django.http import JsonResponse

# def student(request, pk=None):
#     if request.method == "POST":
#         params  = json.loads(request.body)

#         instance = Student.objects.create(
#             name=params.get('name'),
#             branch=params.get('branch'),
#             year=params.get('year'),
#             batch=params.get('batch'),
#             roll_no=params.get('roll_no'),
#             phone=params.get('phone'),
#             email=params.get('email')
#         )

#         return JsonResponse({
#             "message": "Its okk",
#             "data": instance.obj_to_dict()
#         })

# # READ (Student)

#     if request.method == "GET":
#         params = request.GET
#         response = []
#         branch = params.get('branch')

#         qeryset = Student.objects.all()

#         if branch:
#             qeryset = qeryset.filter(branch=branch)
        
#         if pk:
#             qeryset = qeryset.filter(id=pk)

#         for instance in qeryset:
#             response.append(instance.obj_to_dict())
    
#         return JsonResponse({
#             "message": "success",
#             "data": response
#         })
    

# # UPDATE & PATCH (Student)

#     if request.method == "PATCH":
#         params  = json.loads(request.body)

#         name=params.get('name')
#         branch=params.get('branch')
#         year=params.get('year')
#         batch=params.get('batch')
#         roll_no=params.get('roll_no')
#         phone=params.get('phone')
#         email=params.get('email')

#         instance = Student.objects.get(id=pk)

#         if name:
#             instance.name = name

#         instance.save()

#         return JsonResponse({
#             "message": "success",
#             "data": instance.obj_to_dict()
#         })
    

#   # Delete (Student) using 

# def student_delete(request):
#     if request.method == "POST":
#         params  = json.loads(request.body)

#         name = params.get('name')

#         roll_no = params.get('roll_no')

#         phone= params.get('phone')

#         email = params.get ('email')


#         queryset = Student.objects.all()

#         if name:
#             queryset.filter(name=name).delete()
        
#         if roll_no:
#             qeryset.filter(roll_no=roll_no).delete()

#         if phone:
#             queryset.filter(phone=phone).delete()

#         if email:
#             queryset.filter (email.email).delete()

        

#         return JsonResponse({
#             "message": "Its all done",
#         })


# # Delete using unique ID (Student)

# def student_unique (request, roll_no = None):
#     if request.method == "DELETE":
#         instance = Student.objects.filter(roll_no=roll_no).delete()
#         return JsonResponse({
#             "message": "student deleted sucessfully"
#         })


# #  Create (Book)
# def book(request):
#     if request.method == "POST":
#         params  = json.loads(request.body)

#         book_name = params.get('name')
#         author_name = params.get('author_name')
        
#         publisher = params.get('publisher')
#         quantity = params.get('quantity')

#         instance = Book.objects.create(name = book_name,
#             author_name = author_name,
#             publisher = publisher,
#             quantity = quantity)

            
#         return JsonResponse({
#             "message": "Successfully done",
#             "data": instance.obj_to_dict()
#         })


# # update & Patch (Book)
# def book_update(request, pk):
#      if request.method == "PATCH":
#         params = json.loads(request.body)

#         name = params.get('name')
#         author_name = params.get('author_name')
#         publisher = params.get('publisher')
#         quantity = params.get('quantity')
#         quantity = params.get ('id')


#         instance = Book.objects.get(id=pk)

#         if name:
#             instance.name = name
#         if author_name:
#             instance.author_name = author_name
#         if publisher:
#             instance.publisher = publisher
#         if quantity:
#             instance.quantity = quantity
        

#         instance.save()

#         return JsonResponse({
#             "message": "success",
#             "data": instance.obj_to_dict()
#         })


# # READ (Book)

# def book_read(request,pk=None):
#     if request.method == "GET":
#         params = request.GET
#         response = []
#         name = params.get('name')

#         qeryset = Book.objects.all()

#         if name:
#             print("Name Filter Applying", name)
#             qeryset = qeryset.filter(name=name)
        
#         if pk:
#             print("Pk filter applying", pk)
#             qeryset = qeryset.filter(id=pk)

#         for instance in qeryset:
#             response.append(instance.obj_to_dict())
    
#         return JsonResponse({
#             "message": "success",
#             "data": response
#         })


# # Delete (Book)

# def book_delete (request, pk = None):
#     if request.message == "DELETE":
#         instance = Book.objects.get (author_name=pk).delete()
#         return JsonResponse({
#             "message": "author_name deleted sucessfully"
#         })



# # Create (Book issuer)

# def book_issuer(request, pk = None):
#     if request.method == "POST":
#         params = json.loads (request.body)
#         student_id = params.get('student_id')
#         book_id = params.get('book_id')
#         due_timestamp = params.get('due_timestamp')


#         student_obj = Student.objects.get(id = student_id)
#         book_obj = Book.objects.get (id = book_id)
        
#         instance = BookIssueTracker.objects.create(student=student_obj, 
#                 book=book_obj, due_timestamp=due_timestamp
#         )
        
#         return JsonResponse({
#             "message": "book issuer create is done",
#             "data": instance.obj_to_dict()
#         })



# def book_reupdate(request,pk = None):
#     if request.method == "GET":
    
#         params = request.GET
#         response = []
#         name = params.get('name')

#         qeryset = BookIssueTracker.objects.all()

#         if name:
#             print("Name Filter Applying", name)
#             qeryset = qeryset.filter(name=name)
        
#         if pk:
#             print("Pk filter applying", pk)
#             qeryset = qeryset.filter(id=pk)

#         for instance in qeryset:
#             response.append(instance.obj_to_dict())
    
#         return JsonResponse({
#             "message": "success",
#             "data": response
#         })


    






# # model.py


# class Book(models.Model):
  #   name = models.CharField(max_length=100)
 #    author_name = models.CharField(max_length=100)
   #  publisher = models.CharField(max_length=100)
 #    quantity = models.IntegerField()

  #   def obj_to_dict(self):
   #      return dict(

    #            id = self.id,
     #           name = self.name,
      #          author_name = self.author_name,
       #         publisher = self.publisher,
        #        quantity = self.quantity,
                

      #)


# class BookIssueTracker(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     issue_timestamp = models.DateTimeField(auto_now=True)
#     due_timestamp = models.DateTimeField()

#     def obj_to_dict(self):
#         return dict(
#             id=self.id,
#             student_id = self.student.id,
#             name = self.student.name,
#             book_id = self.book.id,
#             book_name= self.book.name,
#             issue_timestamp = self.issue_timestamp,
#             due_timestamp = self.due_timestamp

#         )


# #admin

# admin.site.register(Book)


# admin.site.register(BookIssueTracker)

"""

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

        
issue_timestamp_ymd = issue_timestamp.strftime("%Y-%m-%d")
        due_timestamp_ymd = due_timestamp.strftime("%Y-%m-%d")
        '''

        def update_student_subjects(request, pk=None):
	params = json.loads(request.body)
	subject = params.get('subject_id')

	if subject:
		student_instance = Student.objects.get(id=pk)
		subject_instance = Subject.objects.get(id=subject)
		student_instance.subjects.add(subject_instance)
	
	data = student_instance.obj_to_dict()
	response =  []

	# for subject in subjects:
	# 	response.append(subject.obj_to_dict())
	
	data['subjects'] = [subject.obj_to_dict() for subject in student_instance.subjects.all()] 

	return JsonResponse(dict(
		data=data
	))

def update_student_subjects(request, pk=None):
    params = json.loads(request.body):
    subject = params.get("subject_id")

    if subject:
        subject_instance = Student.objects.get(id=pk)
        subject_instance = Student.objects.get(id=subject)
        subject_instance = Student.objects.get

        	params = json.loads(request.body)
	subject = params.get('subject_id')

	if subject:
		student_instance = Student.objects.get(id=pk)
		subject_instance = Subject.objects.get(id=subject)
		student_instance.subjects.add(subject_instance)
	
	data = student_instance.obj_to_dict()
	response =  []

	# for subject in subjects:
	# 	response.append(subject.obj_to_dict())
	
	data['subjects'] = [subject.obj_to_dict() for subject in student_instance.subjects.all()] 

	return JsonResponse(dict(
		data=data
	))




def update_employee_information(request):
    params = json.loads(request.body)
     project_assignment = params.get("employee_id")

    
    if project_assigned:
        employee_instance = Employee.objects.get(id=pk)
         project_assignment_instance = Employee_information.objects.get(id=subject)
        employee_instance =  project_assignment.add(subject_instance)

    print(student_instance.subjects.all())
    data = [subject.obj_to_dict() for subject in student_instance.subjects.all()]

    return JsonResponse({
        "message": "it done",
        "data":data 
    })

class Employee (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    project_assignments = models.ManyToManyField('Employee_information')

    
   

    def __str__(self):    
        return f'{self.name}'

    def obj_to_dict(self):
        project_assignments = self.project_assignment.all()
        response =  []
        for project_assignment in project_assignments:
            response.append(subject.obj_to_dict())


    def obj_to_dict(self):
        return dict (
            id = self.id,
            name = self.name,
            email = self.email,
            phone = self.phone,
        )



def update_employee_information(request, pk=None):

    params = json.loads(request.body)
    employee_id = params.get("employee_id")

    if employee_id:
        employee_instance = Employee.objects.get(id=pk)
        employee_instance.project_assignments.add(employee_id)

        print(employee_instance.project_assignments.all())
        data = [subject.obj_to_dict() for subject in employee_instance.project_assignments.all()]

    return JsonResponse({
        "message": "it done",
        "data": data
    })
