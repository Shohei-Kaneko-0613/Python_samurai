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
            x=f.read() #D8.txtの読み込み
        m=re.findall(self.keyword,x) #D8.txtからkeywordマッチをmに代入
        self.count=len(m) #マッチした数をカウント
        return m[0] #配列となっているkeywprdを１つに纏める

    def saveNoKeyword(self):
        with open(filepath) as f:
            x=f.read() #D8.txtの読み込み
        with open(filepath, mode='w',newline="\n") as f:
            f.write(x) #D9-1にD8.txtをコピー
        y=x.replace(self.analyze(),"") 
        with open(self.filepathTo, mode='w',newline="\n") as f:
            f.write(y) #D9-1からkeywordを削除

filepath="D8.txt"
keyword="https"
count=0
filepathTo="D9-1"
fileparser=FileParser(filepath,keyword,count,filepathTo)
fileparser.saveNoKeyword()
