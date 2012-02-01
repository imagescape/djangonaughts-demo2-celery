import time 
from celery.decorators import task

@task
def add(x, y):
    return x + y

# If we don't care about task metadata
@task(ignore_result=True)  
def subtract(x, y):
    return x - y

@task
def start(contest_id, **kwargs):
    from cel import models
    contest = models.Contest.objects.get(id=contest_id)
    contest.status = 1  # started status
    contest.save()
    time.sleep(5) # just to waste some time
    task = end.apply_async(args=[contest_id,], eta=contest.end_date, )

@task
def end(contest_id, **kwargs):
    from cel import models
    contest = models.Contest.objects.get(id=contest_id)
    contest.status = 2  # stopped status
    contest.save()
