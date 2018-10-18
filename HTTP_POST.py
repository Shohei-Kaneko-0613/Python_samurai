import requests
import urllib.parse
import yaml
import os
import subprocess

r1 = requests.post("http://localhost:8888/post_test/", data={"files_data2":open("command.txt","rb").read()})
response = (r1.content).decode()
print(response)

if 1 <= len(response):
    print("ファイルあります")
    r3 = requests.post("http://localhost:8888/post_test2/", data={"files_data3":response})
elif response == "NG":
    print("ファイルありません")
    post_data = "test_post.py"

    with open("parameter.yaml") as file:
        yaml_file = yaml.load(file)
        path = yaml_file["file_path"]

    data = path + post_data
    print(data)


    if os.path.exists(data):
        r2 = requests.post("http://localhost:8888/post_test3/", files={"files_data":open("static/test_post.py","r")})
        print(r2.text,type(r2))
    else:
        print("file is does not exist")
