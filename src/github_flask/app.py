
from redis import Redis
from flask import Flask, jsonify
import json

import os
from dotenv import load_dotenv

load_dotenv()

r = Redis()
REPO_NAME = os.environ['GITHUB_REPO']


def get_repo_data():
    value = r.get(REPO_NAME).decode('utf-8')
    return json.loads(value)


def create_app():
    app = Flask(__name__)

    @app.route('/commits')
    def get_commits():
        dict_of_user_values = get_repo_data()
        commits = list(zip(dict_of_user_values['names'], dict_of_user_values['commits']))
        return jsonify({'commits': commits}), 200

    @app.route('/branches')
    def get_branches():
        dict_of_user_values = get_repo_data()
        return jsonify({'branches': dict_of_user_values['branches']}), 200

    return app


def main():
    app = create_app()
    app.run(port=3000)


if __name__ == '__main__':
    main()
