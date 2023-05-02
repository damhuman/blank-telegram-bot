import logging
from celery import Celery

app = Celery('tasks', broker='redis://redis:6379')
logger = logging.getLogger(__name__)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls update_user_subscriptions_task every 10 minutes.
    # sender.add_periodic_task(crontab(minute='*/1'), resend_to_discord_task)
    pass


# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
