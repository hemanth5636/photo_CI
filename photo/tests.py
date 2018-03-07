from django.test import TestCase
import io
from django.urls import reverse
from http import HTTPStatus as status
from PIL import Image
from .views import response_page
# Create your tests here.
class PhotoTestCasses(TestCase):

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_photo_upload(self):

        image = self.generate_photo_file()

        response = self.client.post(reverse(response_page), {'pic':image}, format='multipart')

        self.assertEqual(response.status_code, status.OK._value_)
