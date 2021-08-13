from django.test import TestCase
from todoapp.models import Task
from django.urls import reverse, reverse_lazy
from rest_framework import status

from rest_framework.test import APIClient

# class TaskTest(TestCase):
#     """ Test module for Task model """

#     def setUp(self):
#         a = Task.objects.get_or_create(
#             title='w1', completed=True)
#         Task.objects.get_or_create(
#             title='w2', completed=True)

#     def get_task(self):
#         w1 = Task.objects.filter(title='hello')
#         w2 = Task.objects.filter(title='hello')
#         # print(dir(w1))
#         self.assertEqual(
#             w1.get_task(),'hello')
#         self.assertEqual(
#             w1.get_task(), "hello")



class TestModel1Api(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_Model1_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Model1_detail(self):
        mm_objs = Task.objects.all()
        if mm_objs:
            response = self.client.get(reverse('task-list', args=[mm_objs[0].id]))
            self.assertEqual(response.status_code, status.HTTP_200_OK)