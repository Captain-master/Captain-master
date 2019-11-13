from flask import Flask
from flask_cors import CORS
from controller import Class, pro, admin, user

app = Flask(__name__)
app.register_blueprint(Class.Class)
app.register_blueprint(pro.Pro)
app.register_blueprint(admin.Admin)
app.register_blueprint(user.User)


@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='localhost', port=80)