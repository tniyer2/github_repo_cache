
from redis import Redis
from flask import Flask, jsonify
import json

r = Redis()

def create_app():
    app = Flask(__name__)

    @app.route('/commits')
    def get_commits():
        value = r.get('MoravianCollege/capstone2020').decode('utf-8')
        dict_of_user_values = json.loads(value)
        commits = list(zip(dict_of_user_values['names'], dict_of_user_values['commits']))
        return jsonify({'commits': commits}), 200

    return app

def main():
    app = create_app()
    app.run(port=3000)


if __name__ == '__main__':
    main()
