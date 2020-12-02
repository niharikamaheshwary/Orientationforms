from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    rno = models.IntegerField()
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()

    def __str__(self):
        return self.name, self.rno, self.q1, self.q2, self.q3


