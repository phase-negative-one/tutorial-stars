import datetime
from django.test import TestCase
from .models import Course

class ModelTestCase(TestCase):
    """This class defines the test suite for the course model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.course_title = "Write world class code"
        self.description = "A fantastic tutorial"
        self.created_at =  datetime.datetime.now().time()
        self.star_rating = 5
        self.course = Course(title=self.course_title,
            description = self.description,
            created_at = self.created_at,
            star_rating = self.star_rating)


    def test_model_can_create_a_course(self):
        """Test the course model can create a course."""
        old_count = Course.objects.count()
        self.course.save()
        new_count = Course.objects.count()
        self.assertNotEqual(old_count, new_count)


from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.course_data = {'title': "learn Rust", 
            'description': "a rusty language", 
            'created_at': datetime.datetime.now().time(),
            'star_rating': 5
            }
        self.response = self.client.post(
            self.course_data,
            format="json")

    def test_api_can_create_a_course(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
