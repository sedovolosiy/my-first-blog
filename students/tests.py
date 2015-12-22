# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course

def add_course():
  course = {}
  course[1] = Course.objects.create(
      name = 'PyBursa',
      short_description = '',
      description = 'Web development')
  course[2] = Course.objects.create(
      name = 'JSBursa',
      short_description = 'javascript',
      description = 'JS development')
  course[3] =  Course.objects.create(
      name = 'JavaBursa',
      short_description = '',
      description = 'Java development')
  return course


def add_students():
  course  = add_course()
  students = {}
  students[1] = Student.objects.create(
      name = 'Vad',
      surname = 'Zamb',
      date_of_birth = '2015-01-01',
      email = 'dsdsd@email.com',
      phone = '323232323',
      address = 'erere',
      skype = 'zamb_vad') 
  students[1].courses.add(course[1].id)
  students[2] = Student.objects.create(
      name = 'Dudolad',
      surname = 'Gab',
      date_of_birth = '2015-01-01',
      email = 'gab@email.com',
      phone = '23456787',
      address = 'pessdvcv',
      skype = 'dudola_gab')
  students[2].courses.add(course[1].id)
  students[2].courses.add(course[2].id)
  students[3] = Student.objects.create(
      name = 'test',
      surname = 'testovich',
      date_of_birth = '2015-01-01',
      email = 'testovich@email.com',
      phone = '9876543',
      address = 'manchen',
      skype = 'testovich_test')
  students[3].courses.add(course[1].id)
  students[3].courses.add(course[2].id)
  students[3].courses.add(course[3].id)
  return students

class StudentsListTest(TestCase):

  def test_null_list_students(self):    
    client = Client()
    response = client.get('/students/')
    self.assertEqual(response.status_code,200)

  def test_button_add_students(self):    
    client = Client()
    response = client.get('/students/')
    self.assertContains(response,'<a href="/students/add/">')

  def test_table(self):
    client = Client()
    response = client.get('/students/')
    self.assertContains(response,u'Фамилия и имя')

  def test_pagination_without_course(self):
    students = add_students()
    client = Client()
    response = client.get('/students/')
    self.assertContains(response,'<ul class="pagination">')

  def test_edit_student(self):
    students = add_students()
    client = Client()
    response = client.get('/students/')
    self.assertContains(response,'<a href="/students/edit/')

  def test_remove_student(self):
    students = add_students()
    client = Client()
    response = client.get('/students/')
    self.assertContains(response,'<a href="/students/remove/')

class StudentsDetailTest(TestCase):

  def test_student_if_null(self):
    client = Client()
    response = client.get('/students/1/')  
    self.assertEqual(response.status_code, 404)
    
  def test_student_detail(self):
    client = Client()
    students = add_students()
    response = client.get('/students/1/')
    self.assertEqual(response.status_code, 200)

  def test_active_punkt_menu(self):
    client = Client()
    students = add_students()
    response = client.get('/students/1/')
    self.assertContains(response,'<li  class="active"><a href="/students/">Students</a></li>')

  def test_title_of_page(self):
    students = add_students()
    client = Client()
    response = client.get('/students/1/')
    text = u'<h1>%s %s</h1>' % (students[1].name,students[1].surname)
    self.assertContains(response,text)

  def test_row_in_table(self):
    students = add_students()
    client = Client()
    url = '/students/%s/' % students[1].id
    response = client.get(url)
    self.assertContains(response,u'дата рождения')
    self.assertContains(response,u'адрес')
    self.assertContains(response,u'почта')
    self.assertContains(response,u'логин skype')
    self.assertContains(response,u'телефон')
    self.assertContains(response,u'курсы')

  def test_url_course(self):
    students = add_students()
    client = Client()
    response = client.get('/students/3/')
    self.assertContains(response,'<a href="/courses/1/">')
