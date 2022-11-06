from tests.base import BaseTestCase
import os


class TestGetPictureInvert(BaseTestCase):

    def setUp(self) -> None:
        with open(f'{os.path.abspath(__file__ + "/../../")}/test_image.jpg', 'rb') as file:
            self.image = file.read()

    def test_should_return_inverted_picture(self):
        response = self._get_picture_invert()

        self.assert200(response)
        self.assertNotEqual(response.json, self.image)

    def _get_picture_invert(self):
        return self.client.put(
            '/picture/invert',
            content_type='image/png',
            data=self.image
        )
