from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Semester, Subject, Assignment

# Create your views here.
def home(request):
	semesters = Semester.objects.all()
	return render(request, "home.html", {"semesters": semesters})

# View semester and all subjects in it
def semester(request, semester_id):
	current_semester = Semester.objects.get(id = semester_id)
	return render(request, "semester.html", {"semester": current_semester})

# View subject and all assignments in it
def subject(request, subject_id):
	current_subject = Subject.objects.get(id = subject_id)
	return render(request, "subject.html", {"subject": current_subject})