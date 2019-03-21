from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class ProjectTestClass(TestCase):

    def setUp(self):

        self.new_user = User(username = "wati", email = "moringaprojects@gmail.com",password = "123456789")
        self.new_user.save()
        self.new_project = Project(image_view = 'wati.jpeg', image_description = 'asdfghjkl;;;;;')
        self.new_project.save()

    def test_instance(self):

        self.assertTrue(isinstance(self.new_project, Project))

    def test_init(self):

        self.assertTrue(self.new_project.view == "wati.jpeg")

    def test_save_project(self):

        self.new_project.save_project()
        self.assertTrue(len(Project.objects.all()) > 0)

    def test_set_description(self):

        self.new_project.save_image()
        project = Image.objects.get(id = 1)
        project.set_description("qwertyuiop")
        self.assertTrue(project.description == "qwertyuiop")
