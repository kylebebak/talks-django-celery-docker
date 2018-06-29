from celery import shared_task


@shared_task(name='test_task', default_retry_delay=30, max_retries=3)
def test_task():
    print('qué onda')
