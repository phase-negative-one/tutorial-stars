from django.shortcuts import render

from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Course."""
        serializer.save()