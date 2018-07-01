"""
Store models
"""
import datetime

from django.db import models
from django.utils import timezone


class Good(models.Model):
    """
    Good model
    """
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=100)
    pub_date = models.DateTimeField('date published')

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.name

    def was_published_recently(self):
        """
        Was a good published recently (last day)

        :return: boolean
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
