from celery import shared_task, task


@task()
def see_you():
    print("See you in ten seconds!")


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
