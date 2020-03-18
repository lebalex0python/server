from django.db import models

class Ip(models.Model):
	ip = models.CharField('IP of the server', max_length = 100)
	time = models.DateTimeField('Time of starting the server')
	name = models.CharField('User of the server', max_length = 100)

	def __str__(self):
		return self.ip
