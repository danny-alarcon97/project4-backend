from django.db import models

# Create your models here.

class Chatroom(models.Model):
    chat_name = models.CharField(max_length=100)
    post = models.TextField()
    date_time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name



