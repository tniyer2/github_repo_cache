
from github_collect.user_stats import UserStats


class RepoStats:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.users = {}

    def get_repo_name(self):
        return self.repo_name

    def _add_user_if_missing(self, name):
        if name not in self.users:
            self.users[name] = UserStats(name)

    def register_commits(self, name, num):
        self._add_user_if_missing(name)
        self.users[name].register_commits(num)

    def register_merges(self, name, num):
        self._add_user_if_missing(name)
        self.users[name].register_merges(num)

    def register_comments(self, name, num):
        self._add_user_if_missing(name)
        self.users[name].register_comments(num)

    def register_open_pull_requests(self, name, num):
        self._add_user_if_missing(name)
        self.users[name].register_open_pull_requests(num)

    def register_closed_pull_requests(self, name, num):
        self._add_user_if_missing(name)
        self.users[name].register_closed_pull_requests(num)

    def get_dict_of_user_values(self):
        users_as_dicts = [u.as_dict() for u in self.users.values()]
        sorted_users = sorted(users_as_dicts, key=lambda u: u['name'])

        names = [u['name'] for u in sorted_users]
        commits = [u['commits'] for u in sorted_users]
        merges = [u['merges'] for u in sorted_users]
        comments = [u['comments'] for u in sorted_users]
        open_pull_requests = [u['open_pull_requests'] for u in sorted_users]
        closed_pull_requests = [u['closed_pull_requests'] for u in sorted_users]

        return {'names': names,
                'commits': commits,
                'merges': merges,
                'comments': comments,
                'open_pull_requests': open_pull_requests,
                'closed_pull_requests': closed_pull_requests}
