from django.db import models

class Job(models.Model):
    Name = models.CharField(max_length=20)
    past_job = models.TextField()
    profile_image = models.ImageField(blank=True)

    def __str__(self):
        return self.name