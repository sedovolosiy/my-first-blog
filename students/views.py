# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)

class StudentDetailView(DetailView):
  model = Student
  def get_context_data(self, **kwargs):
    logger.debug("Students detail view has been debugged")
    logger.info("Logger of students detail view informs you!")
    logger.warning("Logger of students detail view warns you!")
    logger.error("Students detail view went wrong!")
    context = super(StudentDetailView, self).get_context_data(**kwargs)
    return context

class StudentListView(ListView):
  model = Student  
  paginate_by = 2 

  def get_queryset(self):
    id = self.request.GET.get('course_id',None)  
    if id:
      students = Student.objects.filter(courses=id)
      
    else:
      students = Student.objects.all()
    return students

  def get_context_data(self, **kwargs):
    context = super(StudentListView, self).get_context_data(**kwargs)
    id = self.request.GET.get('course_id',None) 
    if id:
      context['course_url'] = 'course_id=%s&' % id
    return context


#CreateView, UpdateView, DeleteView
class StudentCreateView(CreateView):
  model = Student
  
  def get_context_data(self, **kwargs):
    context = super(StudentCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Student registration'
    return context

  def form_valid(self,form):
    form.save()
    messages.success(self.request, 'Student %s %s has been successfully added.' % (form.cleaned_data['name'], form.cleaned_data['surname']))
    return super(StudentCreateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
  model = Student
  success_url = reverse_lazy('students:list_view')
  
  def delete(self, request, *args, **kwargs):
    student = self.get_object()
    messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
    return super(StudentDeleteView, self).delete(request, *args, **kwargs)
  

  def get_context_data(self, **kwargs):
    context = super(StudentDeleteView, self).get_context_data(**kwargs)
    student =  Student.objects.get(id=self.kwargs['pk'])
    context['title'] = 'Student info suppression'
    context['message'] ='%s %s' % (student.name, student.surname)    
    return context
    

class StudentUpdateView(UpdateView):
  model = Student
  form_class = StudentModelForm
  success_url = reverse_lazy('students:list_view')
  

  def get_context_data(self, **kwargs):
    context = super(StudentUpdateView, self).get_context_data(**kwargs)    
    context['title'] = 'Student info update'
    return context

  def form_valid(self,form):
    student = form.save()
    messages.success(self.request, u'Info on %s %s the student has been sucessfully changed.'  % (student.name, student.surname))
    return super(StudentUpdateView, self).form_valid(form)
