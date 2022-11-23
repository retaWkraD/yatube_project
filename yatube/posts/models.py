from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # group = models.ForeignKey(
    #     blank=True,
    #     null=True
    # )


class Group(models.Model):
    title = models.TextField()

    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
