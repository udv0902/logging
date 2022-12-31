from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
	content = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse_lazy('post_detail', args=[str(self.id)])
