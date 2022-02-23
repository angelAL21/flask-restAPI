import requests

BASE = "http://127.0.0.1:5000/"


# data=[{"name": "video_name", "views": 100000, "likes": 10000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/7" + str(i), data[i])
#     print(response.json())
    

response = requests.get(BASE + "video/2") #get one video with id.
#response = requests.patch(BASE + "video/2"), {"views":999999, "likes": 99999} patch one video with id.

# input()
# response = requests.get(BASE + "video/6")
print(response.json)