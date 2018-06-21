from django.db import models


class Thought(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title