from django.db import models

STATUSES = ((0, 'Not Started'),
    (1,'Running'), (2,'Complete'),)

class Contest(models.Model):
    status = models.IntegerField(choices=STATUSES,  default=0)
    name = models.CharField(max_length=12)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
