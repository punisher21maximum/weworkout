from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	section_CHOICES = [('Startup Story', 'Startup Story'), ('Random Reads', 'Random Reads'),
	('Top N', 'Top N'), ('Tech Corner', 'Tech Corner'), ('Convid-19', 'Covid-19'),
	('News', 'News'), ('Competetive Exams', 'Competetive Exams')] 
	section = models.CharField(max_length=100, choices=section_CHOICES, default='Random Reads')
	
	# content = models.TextField()
	content = RichTextUploadingField(blank=True)

	content2 = RichTextUploadingField(blank=True, config_name='special', 
                                      external_plugin_resources=[
                                          ('youtube', 
                                            '/static/blog/vendor/ckeditor_plugins/youtube/youtube/', 
                                            'plugin.js', 
                                            )
                                      ])

	date_posted = models.DateTimeField(default=timezone.now)
	last_edit = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	claps = models.IntegerField(default=0)

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