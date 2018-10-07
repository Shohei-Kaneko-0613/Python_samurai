import requests
import urllib.parse
import yaml

with open("parameter.yaml") as file:
    yaml_file = yaml.load(file)
    path = yaml_file["file_path"]

files = {"file": open("test_post.py","rb")}
r = requests.post("http://localhost:8888/post_test/", files=files)
print(r.text)

