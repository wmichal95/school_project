from locust import HttpUser, task
import os


class LocustTestPicture(HttpUser):
    def __init__(self, env, *args, **kwargs):
        super().__init__(env, *args, **kwargs)
        with open(f'{os.path.abspath(__file__ + "/../")}/test_image.jpg', 'rb') as file:
            self.image = file.read()

    @task
    def test_invert_picture(self):
        self.client.put('/picture/invert', data=self.image, verify=False)
