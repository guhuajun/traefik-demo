import random

from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1.0, 3.0)

    @task(1)
    def vote(self):
        self.client.get('/')
        self.client.post('/', data={'vote': random.choice(['a', 'b'])})

