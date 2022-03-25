from planeks_app.celery import app
from .make_tasks import make_files


@app.task
def make_file(req):
    make_files(req)
