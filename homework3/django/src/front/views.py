"""
Poll views
"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Good


# pylint: disable=too-many-ancestors
class IndexView(generic.ListView):
    """
    Index view
    """
    template_name = 'goods/index.html'
    context_object_name = 'goods'

    def get_queryset(self):
        """Return the last five published goods."""
        return Good.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    """
    Good details view
    """
    model = Good
    template_name = 'goods/detail.html'
