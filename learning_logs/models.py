from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	"""Topic, which user learns."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return string of the model"""
		return self.text

class Entry(models.Model):
	"""Some info about the theme"""		
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Returns representation of the model as a string"""
		return f"{self.text[:50]}..."
