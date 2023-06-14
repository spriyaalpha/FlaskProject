from flask import Flask, request, jsonify
from routes.task1 import task1_blueprint
from routes.task2 import task2_blueprint

app = Flask(__name__)
app.register_blueprint(task1_blueprint)
app.register_blueprint(task2_blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8801, debug=False)
