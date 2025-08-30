# posts/models.py
from django.db import models
from django_quill.fields import QuillField
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tb_posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.created_at}"
