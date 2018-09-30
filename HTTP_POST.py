import requests

#payload = {'key1': 'value1', 'key2': 'value2'}
files = {"file": open("test_post.py","rb")}
r = requests.post("http://localhost:8888/post_test/", files=files)
print(r.text)
