from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


# Create your models here.

class Publish(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
    logic_delete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.date_posted} - {self.published}'

    def save(self, *args, **kwargs):
        if self.published:
            self.published_date = timezone.now()
        return super().save(*args, **kwargs)

