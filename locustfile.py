from locust import HttpLocust, TaskSet, task
import requests

proxies = {
	"http": "192.168.1.240:8081",
	"https": "192.168.1.240:8081",
}
auth = requests.auth.HTTPProxyAuth("user1", "password1")

class UserBehavior(TaskSet):
	def on_start(self):
		""" on_start is called when a Locust start before any task is scheduled """
		pass

	@task(1)
	def index(self):
		self.client.get("/path", proxies = proxies,
			auth = auth, verify = False)

class WebsiteUser(HttpLocust):
	task_set = UserBehavior
