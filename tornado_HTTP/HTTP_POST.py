import urllib.parse
import yaml
import os
import subprocess
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

r1 = requests.post("https://localhost:8443/post_test/",verify=False, data={"files_data2":open("command2.txt","rb").read()})
response = (r1.content).decode()
print(response)

if 1 <= len(response):
    print("ファイルあります")
    r3 = requests.post("https://localhost:8443/post_test2/",verify=False, data={"files_data3":open("command2.txt","rb").read()})
elif response == "":
    print("ファイルありません")
    #post_data = "test_post.py"
    with open("command2.txt") as file2:
        data = file2.read()
        print(data)
    with open("parameter.yaml") as file:
        yaml_file = yaml.load(file)
        path = yaml_file["file_path"]
        print(path)

    data2 = path + data
    data = "/Users/kanekoshohei/Documents/"+"test_post20.py"
    print(data)
    print(data2)
    print(data==data2)
    print(len(data))
    print(len(data2))


    if os.path.exists(data):
        r2 = requests.post("https://localhost:8443/post_test3/",verify=False, files={"files_data":open("static/test_post.py","r")})
        print(r2.text,type(r2))
    else:
        print("file is does not exist")

