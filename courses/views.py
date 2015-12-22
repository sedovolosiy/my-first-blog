from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from courses.models import Lesson,Course
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
import logging
logger = logging.getLogger(__name__)



class CourseDetailView(DetailView):
  model = Course
  template_name = "courses/detail.html"
  context_object_name = 'course'
  fields = '__all__'

  

  def get_context_data(self, **kwargs):
    logger.debug("Courses detail view has been debugged")
    logger.info("Logger of courses detail view informs you!")
    logger.warning("Logger of courses detail view warns you!")
    logger.error("Courses detail view went wrong!")
    context = super(CourseDetailView, self).get_context_data(**kwargs)
    lessons = Lesson.objects.filter(course=self.object)
    context['lessons'] = lessons
    return context 

class CourseCreateView(CreateView):
  model = Course
  context_object_name = 'course'
  template_name = 'courses/add.html'
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(CourseCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Course creation'
    return context 

  def form_valid(self,form):
    form.save()
    messages.success(self.request, 'Course %s has been successfully added.' % (form.cleaned_data['name']))
    return super(CourseCreateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
  model = Course
  success_url = reverse_lazy('index')
  context_object_name = 'course'
  template_name = 'courses/remove.html'

  def delete(self, request, *args, **kwargs):
    course = self.get_object()
    messages.success(self.request, 'Course %s has been deleted.' % (course.name))
    return super(CourseDeleteView, self).delete(request, *args, **kwargs)
  
  def get_context_data(self, **kwargs):
    context = super(CourseDeleteView, self).get_context_data(**kwargs)
    course =  Course.objects.get(id=self.kwargs['pk'])
    context['title'] = 'Course deletion'
    return context


class CourseUpdateView(UpdateView):
  model = Course
  success_url = reverse_lazy('index')
  context_object_name = 'course'
  template_name = 'courses/edit.html' 
  fields = '__all__'
   

  def get_context_data(self, **kwargs):
      context = super(CourseUpdateView, self).get_context_data(**kwargs)
      context['title'] = 'Course update'
      return context

  def form_valid(self,form):
    course = form.save()
    messages.success(self.request, u"The changes have been saved.")
    return super(CourseUpdateView, self).form_valid(form)

  def get_success_url(self):
    return reverse_lazy('courses:edit', None, [self.object.id])

class AddLessonCreateView(CreateView):
  model = Lesson
  context_object_name = 'lesson'
  template_name = 'courses/add_lesson.html'


  def get_context_data(self, **kwargs):
      context = super(AddLessonCreateView, self).get_context_data(**kwargs)
      context['title'] = 'Add Lesson'
      return context

  def get_initial(self):
    return {'course':self.kwargs['pk']} 

  def form_valid(self,form):
    form.save()
    messages.success(self.request, 'Lesson %s has been successfully added.' % (form.cleaned_data['subject']))
    return super(AddLessonCreateView, self).form_valid(form)

  def get_success_url(self):    
    return  reverse_lazy('courses:detail', None, [self.object.course_id])
