from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coaid):
  coach = Coach.objects.get(id=coaid)
  coach.full_name = coach.user.get_full_name()
  coach.email = coach.user.email
  coach.courses_coach = Course.objects.filter(coach=coach)
  coach.courses_assistant = Course.objects.filter(assistant=coach)
  return render(request, 'coaches/detail.html', {
        "coach": coach,
        })