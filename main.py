from flask import Flask
from flask_restful import Api, Resource

app= Flask(__name__)
api = Api(app)

#helloworld class test.
class HelloWorld(Resource):
    def get(self):
        return {"data":"hello world"}

#endpoint helloworld.
api.add_resource(HelloWorld, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True)