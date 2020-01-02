# -*- coding: utf-8 -*-
# pylint: disable=

from locust import HttpLocust, TaskSet, between


def whoami(l):
    l.client.get("/whoami")


class UserBehavior(TaskSet):
    tasks = {whoami: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 10.0)
