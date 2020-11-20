
from redis import Redis
from github import Github
import json

import time
import datetime

import os
from dotenv import load_dotenv

from github_collect.github_stats import make_repo_stats

load_dotenv()
r = Redis()

repos = ['tniyer2/github_repo_cache']
DELAY_SECONDS = 5 * 60


def make_hour_minute_time_string(timestamp):
    return timestamp.strftime('%-I:%M')


def collect():
    github = Github(os.environ['GITHUB_TOKEN'])

    while True:
        before = github.rate_limiting[0]

        last_update = datetime.datetime.now()
        try:
            update_redis(github, last_update)
            print(str(last_update) + ': Successful Update')
        except Exception as e:
            print(str(last_update) + ': Failed Update')
            print(e)

        github.get_rate_limit()
        after = github.rate_limiting[0]
        used = before - after

        r.set('used', used)
        r.set('remaining', after)

        time.sleep(DELAY_SECONDS)


def update_redis(github, last_update):
    for repo_name in repos:
        stats = make_repo_stats(repo_name, github)
        r.set(repo_name, json.dumps(stats.get_dict_of_user_values()))

    next_update = last_update + datetime.timedelta(seconds=DELAY_SECONDS)

    r.set('last_update', make_hour_minute_time_string(last_update))
    r.set('next_update', make_hour_minute_time_string(next_update))


if __name__ == '__main__':
    collect()

