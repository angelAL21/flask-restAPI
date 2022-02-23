from flask import Flask
from flask_restful import Api, Resource, reqparse

app= Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of video is required", required=True)
video_put_args.add_argument("views", type=int, help="views of video", required=True)
video_put_args.add_argument("likes", type=int, help="likes on video", required=True)

videos={}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] =args
        return videos[video_id], 201

#endpoint helloworld.
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)