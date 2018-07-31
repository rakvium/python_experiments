import requests
from celery import Celery

app = Celery('app', broker='redis://redis:6379/0')


@app.task
def fetch_url(url):
    try:
        resp = requests.get(url)
        print(f"{url} - {resp.status_code}")
    except requests.ConnectionError as e:
        print("{} - Connection Error".format(url))


def send_emails():
    None


# TODO: constantly check Redis on emails and send them
if __name__ == "__main__":
    send_emails()
