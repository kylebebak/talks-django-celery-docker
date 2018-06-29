from __future__ import absolute_import

from datetime import timedelta


CELERY_IMPORTS = (
    'jobs.test',
)

CELERY_ENABLE_UTC = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

CELERYBEAT_SCHEDULE = {
    'test_task': {
        'task': 'test_task',
        'schedule': timedelta(seconds=60 * 1),
    },
}
