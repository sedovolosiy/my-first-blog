# -*- coding: utf-8 -*-
from django import forms
from students.models import Student


class StudentModelForm(forms.ModelForm):
  class Meta:
    model = Student
    