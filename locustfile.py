from locust import HttpUser, LoadTestShape, TaskSet, constant, task
from urllib3 import PoolManager
from urllib import parse
import math
import string
import random


class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")
        self.client.close()
    
    @task(1)
    def get_images(self):
        self.client.get('/images')
        self.client.close()

    @task(2)
    def testData(self):   
        dataValueGet = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))
        f = { 'load' : dataValueGet }
        encode = parse.urlencode(f)
        self.client.get("/data?{encode}")
        self.client.close()

class WebsiteUser(HttpUser):
    pool_manager = PoolManager(maxsize=5000, block=True)
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StepLoadShape(LoadTestShape):
    """
    A step load shape


    Keyword arguments:

        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds

    """

    step_time = 30
    step_load = 1000
    spawn_rate = 500
    time_limit = 1800

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)

