#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from urllib3 import PoolManager
from locust import HttpUser, task, between

class SeelaTest(HttpUser):
    wait_time = between(1, 5)
    pool_manager = PoolManager(maxsize=10, block=True)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/admin")
        self.client.get("/images")
