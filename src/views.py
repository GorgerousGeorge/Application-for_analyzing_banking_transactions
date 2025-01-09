import json
from datetime import datetime


def prime(timedate: str) -> json:
    hour = int(timedate[-8:-7])
    if hour < 4:
        greetings = ""