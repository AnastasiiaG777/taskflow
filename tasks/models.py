from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнено'),
    ]

    title = models.CharField('Заголовок',max_length=100)
    description = models.TextField('Описание')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices= STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField('Время создания',  auto_now_add=True)
