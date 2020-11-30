# github_repo_cache
This repo collects and updates data about a github repo and saves it to redis.
It then gives clients access to this data through an API run by a Flask server.

Steps to run the server.

1. Create an environment file with the key GITHUB_REPO for the name of the repo
you want to keep track of. Also create a GITHUB_TOKEN key for access to the repo.
2. Start redis by running the command redis-server.
3. Run github_collect.collector.py
4. Run github_flask.app.py
5. Run github_client.main.py
6. In the terminal the client is running in, press enter at anytime to
display the list of branch names in your repo. If you add or remove any
branches to your repo it will update in the terminal after pressing enter.
