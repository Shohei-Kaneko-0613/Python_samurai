import re
class FileParser:
    def __init__(self,filepath,keyword,count,filepathTo):
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
            
        if type(filepathTo) == str:
            self.filepathTo = filepathTo
        else:
            raise TypeError
            
    def analyze(self):
        with open(self.filepath) as f:
            x=f.read() 
        m=re.findall(self.keyword,x)
        self.count=len(m)
        print(self.count)
        
    def saveNoKeyword(self):
        with open(filepath) as f:
            x=f.read().replace(self.keyword,"")
        with open(filepathTo, mode='w',newline="\n") as f:
            f.write(x)
            return True

filepath="D8.txt"
keyword="https"
count=0
filepathTo="D9-1"
fileparser=FileParser(filepath,keyword,count,filepathTo)
fileparser.analyze()
print(fileparser.saveNoKeyword())
