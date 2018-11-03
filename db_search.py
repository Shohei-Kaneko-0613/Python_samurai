import subprocess
def search():
    result = subprocess.check_output(["python", "column_search.py"])
    return result.decode().strip()

search()
