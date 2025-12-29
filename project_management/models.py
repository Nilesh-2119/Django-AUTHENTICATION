from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, )
    discription = models.CharField(max_length=1000)
    owner = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title