import re
class FileParser:
    def __init__(self,filepath,keyword,count):
        if type(filepath) == str:
            self.filepath = filepath
        else:
            raise TypeError
 
        if type(keyword) == str:
            self.keyword = keyword
        else:
            raise TypeError
 
        if type(count) == int:
            self.count = count
        else:
            raise TypeError
    def analyze(self):
        with open(self.filepath) as f:
            x=f.read()

        m=re.findall(self.keyword,x)
        print(m)
        self.count=len(m)
        print(self.count)
        

filepath="../../A1.py"
keyword="test"
count=0
fileparser=FileParser(filepath,keyword,count)
fileparser.analyze()
