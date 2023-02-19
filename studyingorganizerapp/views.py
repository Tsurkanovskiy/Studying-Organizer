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
	#for future CRUD functionality
	#HttpResponseRedirect("/semester/{0}".format(semester_id))

# View subject and all assignments in it
def subject(request, subject_id):
	current_subject = Subject.objects.get(id = subject_id)
	return render(request, "subject.html", {"subject": current_subject})

# View all deadlines in curent semester
def deadlines(request, semester_id):
	current_semester = Semester.objects.get(id = semester_id)
	#access several levels foreign key relationships
	assignments = Assignment.objects.filter(subject__semester=current_semester).order_by('deadline')

	#get course/semester completion score
	open_assignments = assignments.filter(is_open=True)
	completion_score = round(len(open_assignments.filter(is_finished=True))/len(open_assignments), 2)*100


	return render(request, "deadlines.html", {"assignments": assignments, "completion_score": completion_score})
