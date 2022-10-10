from django.db import models

class Olimp(models.Model):
    title = models.CharField(max_length=100)
    information = models.TextField()
    audience = models.TextField()
    start_dates = models.DateTimeField(blank=True, null=True)
    finish_dates = models.DateTimeField(blank=True, null=True)
    site = models.URLField(null=True)
    tegs = models.CharField(max_length=200, blank=True)

    def _str_(self):
        return self.title
    
