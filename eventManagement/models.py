from django.db import models

# Create your models here.
class Event(models.Model):
	code=models.IntegerField()
	name=models.CharField(max_length=200)
	max_attendees=models.IntegerField()
	type=models.CharField(max_length=10)
	start=models.DateTimeField('Starting date')
	end=models.DateTimeField('Ending Date')
	def __str__(self):
		return self.name

class Member(models.Model):
	code=models.IntegerField()
	name=models.CharField(max_length=25)
	username=models.CharField(max_length=200)
	password_key=models.CharField(max_length=30)
	def __str__(self):
		return self.name


class Event_Member(models.Model):
	event_code=models.IntegerField()
	member_code=models.IntegerField()
	def __str__(self):
		return 'Event Code : '+str(self.event_code)+' Member Code : '+str(self.member_code)
