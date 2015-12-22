from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from feedbacks.models  import Feedback
from feedbacks.forms import FeedbackForm
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins

class FeedbackView(CreateView):
  model = Feedback
  template_name = 'feedback.html'
  form_class = FeedbackForm
  success_url = reverse_lazy('feedback')

  def get_context_data(self, **kwargs):
    context = super(FeedbackView, self).get_context_data(**kwargs)
    context['title'] = 'Sending feedback'
    return context

  def form_valid(self, form):
    form.save()
    data = form.cleaned_data
    
    mail_admins(data['subject'], data['message'], fail_silently=True)
    messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
    return super(FeedbackView, self).form_valid(form)


# Create your views here.
