from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from courses.models import Course
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['course'] = Course.objects.all()
    return context

