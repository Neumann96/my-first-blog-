from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class kkexam(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название экзамена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    exam_date = models.DateTimeField(verbose_name="Дата проведения экзамена")
    image = models.ImageField(upload_to='exam_images/', verbose_name="Изображение задания")
    users = models.ManyToManyField(User, related_name='exams', verbose_name="Пользователи")
    is_public = models.BooleanField(default=False, verbose_name="Публичный экзамен")

    def __str__(self):
        return self.name