from celery import shared_task
from random import randint
import time



@shared_task(name="run_page_followers")
def run_page_followers():
    print("Updating number of page followers...")
    time.sleep(randint(50, 120))
    print(f"We'got {randint(3, 10)} new followers")


@shared_task(name="run_page_posts")
def run_page_posts():
    print("Updating posts performance...")
    time.sleep(randint(120, 360))
    print("Posts Updated")


@shared_task(name="test_task")
def test_queue():
    print("Testing queue...")

