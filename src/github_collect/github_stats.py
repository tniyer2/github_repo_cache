
from github_collect.repo_users import RepoStats
from github_collect.user_cache import user_cache


def make_repo_stats(repo_name, github):
    repo = github.get_repo(repo_name)
    stats = RepoStats(repo_name)

    _register_branches(repo, stats)
    _register_contributions(repo, stats)
    # _register_open_pull_requests(repo, stats)
    # _register_closed_pull_requests(repo, stats)

    return stats


def _register_branches(repo, stats):
    for b in repo.get_branches():
        stats.register_branch(b.name)


def _register_contributions(repo, stats):
    for c in repo.get_stats_contributors():
        stats.register_commits(get_name(c.author), c.total)


def _register_open_pull_requests(repo, stats):
    for pr in repo.get_pulls():
        stats.register_open_pull_requests(get_name(pr.user), 1)

        for comment in pr.get_comments():
            stats.register_comments(get_name(comment.user), 1)


def _register_closed_pull_requests(repo, stats):
    for pr in repo.get_pulls(state='closed'):
        stats.register_closed_pull_requests(get_name(pr.user), 1)

        if pr.merged_by is not None:
            stats.register_merges(get_name(pr.merged_by), 1)

        for comment in pr.get_review_comments():
            stats.register_comments(get_name(comment.user), 1)

        for comment in pr.get_issue_comments():
            stats.register_comments(get_name(comment.user), 1)


def get_name(named_user):
    if not user_cache.is_cached(named_user.login):
        if named_user.name is None:
            user_cache.cache(named_user.login, named_user.login)
        else:
            user_cache.cache(named_user.login, named_user.name)

    return user_cache.get_value(named_user.login)
