from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	# content = models.TextField()
	content = RichTextField()
	date_posted = models.DateTimeField(default=timezone.now)
	last_edit = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	def __str__(self):
	    return self.title

	def get_absolute_url(self):
	    return reverse('post-detail', kwargs={'pk': self.pk})

class Preference(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.IntegerField()
	date = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ("user", "post", "value")

	def __str__(self):
		return str(self.user)+' : '+str(self.post)+' : '+str(self.value)