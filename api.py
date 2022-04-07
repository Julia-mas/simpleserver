from flask import Flask
import json

f = open('users.json')
users = json.load(f)

api = Flask(__name__)


@api.route('/users', methods=['GET'])
def get_users():
    return json.dumps(users, indent=4)


if __name__ == '__main__':
    api.run(debug=True)
