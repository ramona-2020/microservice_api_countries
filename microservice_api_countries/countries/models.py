from django.db import models


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ('name',)

    name = models.CharField(max_length=30)
    local_currency = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
