from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):

        self.new_user = User(username = "wati", email = "moringaprojects@gmail.com",password = "123456789")
        self.new_user.save()
        self.new_image = Image(image_view = 'wati.jpeg', image_description = 'asdfghjkl;;;;;')
        self.new_image.save()

    def test_instance(self):

        self.assertTrue(isinstance(self.new_image, Image))

    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """

        self.assertTrue(self.new_image.image_view == "wati.jpeg")
