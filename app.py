from flask import Flask

import models
from resources.courses import courses_api
from resources.reviews import reviews_api
from resources.users import user_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(user_api, url_prefix='/api/v1')


@app.route('/')
def hello_world():
    return 'Hello World!'


models.initialize()

if __name__ == '__main__':
    app.run()
