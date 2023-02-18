from django.db import models

# Create your models here.
class Semester(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=100)
	semester = models.ForeignKey(Semester, on_delete = models.CASCADE, default = None, null = True)

	def __str__(self):
		return self.name

class Assignment(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(null = True, blank = True)
	is_finished = models.BooleanField()
	is_open = models.BooleanField()
	deadline = models.DateField()
	subject = models.ForeignKey(Subject, on_delete = models.CASCADE, default = None, null = True)

	def __str__(self):
		return self.title

