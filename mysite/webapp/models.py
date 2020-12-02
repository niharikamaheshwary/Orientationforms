from django.db import models
from gsheets import mixins
from uuid import uuid64


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    rno = models.IntegerField()
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    def __str__(self):
        return self.name, self.rno, self.q1, self.q2, self.q3



class Student(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id='1qajdtiZ0sqeNcxKZiOQdoLIFcEIMAm2wudvw1mhee1A/edit#gid=0'
    model_id_field ='guid'
    name= models.CharField(max_length=100)
    rno= models.IntegerField()
    q1=models.TextField()
    q2=models.TextField()
    q3=models.TextField()



    def __str__(self):
        return f'{self.name} {self.rno} {self.q1} {self.q2} {self.q3}'


