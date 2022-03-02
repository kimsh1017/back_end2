from email.policy import default
from django.db import models
from django.forms import CharField

# notice


class Notice(models.Model):
    subject = models.CharField(max_length=200, default="")
    content = models.TextField()
    create_date = models.DateTimeField()
    writer = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="1111")
    page_number = models.IntegerField(default=0)

    def __str__(self):
        return self.subject
