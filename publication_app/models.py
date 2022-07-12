from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse

from media_app.models import Media


class Post(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id}.{self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_time', '-id']


class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to='posts/%Y', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/image{self.id}'

    class Meta:
        verbose_name = 'Картинка  поста'
        verbose_name_plural = 'Картинки постов'