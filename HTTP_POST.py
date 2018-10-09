import requests
import urllib.parse
import yaml
import os

post_data = "test_post.py"

with open("parameter.yaml") as file:
    yaml_file = yaml.load(file)
    path = yaml_file["file_path"]

data = path + post_data
print(data)


if os.path.exists(data):
    files = {"file": open(data,"rb")}
    r = requests.post("http://localhost:8888/post_test/", files=files)
    print(r.text)
else:
    print("file is does not exist")

