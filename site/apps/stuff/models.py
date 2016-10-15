from django.db import models
from django.core.urlresolvers import reverse

class Stuff(models.Model):
    junk = models.CharField(max_length=200)
    things = models.TextField()
    somenum = models.IntegerField()

    def __str__(self):
        return self.junk

    def get_absolute_url(self):
        return reverse('stuff_edit', kwargs={'pk': self.pk})
