# -*- coding: utf-8 -*-
# pylint: disable=

import random

from locust import HttpLocust, TaskSet, between


def vote(l):
    l.client.get('/')
    l.client.post('/', data={"vote": random.choice(['a', 'b'])})


class UserBehavior(TaskSet):
    tasks = {vote: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 10.0)
