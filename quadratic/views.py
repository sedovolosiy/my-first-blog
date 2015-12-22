# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm
from django import forms

def discr(a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  d=(b*b)-(4*a*c)
  return int(d)


def deq(a,b):
  x=-float(b)/(2*float(a)) 
  return x


def dbig(a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  x1=(-b+((b*b-4*a*c)**(1/2.0)))/2*a
  x2=(-b-((b*b-4*a*c)**(1/2.0)))/2*a
  x1=round(x1,2)
  x2=round(x2,2)
  t={'1':x1,'2':x2}
  return t

def quadratic_results(request):
  x1 = None
  x2 = None
  d = None
  form = QuadraticForm()
  if request.method == "GET":
    form = QuadraticForm(request.GET)
    if form.is_valid():
      a = form.cleaned_data['a']
      b = form.cleaned_data['b']
      c = form.cleaned_data['c']
      d = discr(a,b,c)
      if d == 0:
        x1 = x2 = deq(a, b)
      elif d > 0:
        temp = dbig(a, b, c)
        x1 = temp['1']
        x2 = temp['2']
  
  
  return render(request,'quadratic/results.html',{'form':form,'d':d,'x1':x1,'x2':x2})