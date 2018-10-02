import requests
import yaml

files = {"file": open("test_post.py","rb")}
r = requests.post("http://localhost:8888/post_test/", files=files)
print(r.text)

with open("parameter.yaml") as file:
    yaml_file = yaml.load(file)
    text = yaml_file["file_path"]
    print(text)
    q = requests.post("http://localhost:8888/post_test/", data=text)
print(q.text)
