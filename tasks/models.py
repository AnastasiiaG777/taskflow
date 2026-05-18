from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнено'),
    ]

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    title = models.CharField('Заголовок',max_length=100)
    description = models.TextField('Описание')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices= STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField('Время создания',  auto_now_add=True)
    updated_at = models.DateTimeField('Время обновления', auto_now=True)

    def __str__(self):
        return self.title