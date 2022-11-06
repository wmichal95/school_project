from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_healthcheck(self):
        self.client.get("/healthcheck")
