from lms_backend.models import Student

from rest_framework import viewsets
from lms_backend.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer