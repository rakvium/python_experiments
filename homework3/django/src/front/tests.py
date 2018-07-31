"""
Good application test
"""
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Good


class GoodModelTests(TestCase):
    """
    Good model tests
    """

    # pylint: disable=invalid-name
    def test_was_published_recently_with_future_good(self):
        """
        was_published_recently() returns False for goods whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_good = Good(pub_date=time)
        self.assertIs(future_good.was_published_recently(), False)

    # pylint: disable=invalid-name
    def test_was_published_recently_with_old_good(self):
        """
        was_published_recently() returns False for goods whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_good = Good(pub_date=time)
        self.assertIs(old_good.was_published_recently(), False)

    # pylint: disable=invalid-name
    def test_was_published_recently_with_recent_good(self):
        """
        was_published_recently() returns True for goods whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59)
        recent_good = Good(pub_date=time)
        self.assertIs(recent_good.was_published_recently(), True)
