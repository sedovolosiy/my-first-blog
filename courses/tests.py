# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.test import Client


class CoursesListTest(TestCase):

  def test_course_create(self):
    course1 = Course.objects.create(
      name = 'PyBursa',
      short_description = '',
      description = 'Web development')
    self.assertEqual(Course.objects.all().count(),1)

  def test_list_courses(self):    
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)

  def test_choose_name_of_course(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development')    
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'PyBursa')

  def test_choose_url_detail_course(self):    
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'<a href="/courses/1/')
    
  def test_choose_edit_url_course(self):
    
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'<a href="/courses/edit/1/">')

  def test_link_remove(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    course1 = Course.objects.create(
    name = 'JSBursa',
    short_description = 'testq',
    description = 'JS development')
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'<a href="/courses/remove/1/">')
    self.assertContains(response,'<a href="/courses/remove/2/">')
    
  def test_two_courses(self):    
    Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    Course.objects.create(
    name = 'JSBursa',
    short_description = 'testq',
    description = 'JS development')      
    client = Client()
    response = client.get('/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'JSBURSA')

class CoursesDetailTest(TestCase):
  def test_title(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'<h1>PyBursa</h1>')

  def test_add_lesson(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,u'Добавить занятие')

  def test_tema_uroka(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,u'Тема')

  def test_num_lesson(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,u'#')

  def test_view_lesson(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'python is a cool language')

  def test_url_students_of_course(self):
    course1 = Course.objects.create(
    name = 'PyBursa',
    short_description = 'test0',
    description = 'Web development') 
    lesson1 = Lesson.objects.create(
      subject ='python is a cool language',
      description = 'basic of python',
      course = course1,
      order = '1'
      )   
    client = Client()
    response = client.get('/courses/1/')
    self.assertEqual(response.status_code,200)
    self.assertContains(response,'<a href="/students/?course_id=1">Students</a>')
    