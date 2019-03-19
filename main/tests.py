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

        self.assertTrue(self.new_image.image_view == "wati.jpeg")

    def test_save_image(self):

        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_set_description(self):

        self.new_image.save_image()
        image = Image.objects.get(id = 1)
        image.set_description("qwertyuiop")
        self.assertTrue(image.description == "qwertyuiop")
