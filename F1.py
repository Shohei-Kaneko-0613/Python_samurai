import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/F1.html")
        
class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        num1=self.get_argument("check1","")
        num2=self.get_argument("check2","")
        num3=self.get_argument("check3","")
        num4=self.get_argument("check4","")
        num5=self.get_argument("check5","")
        num_list=[]
        for num in num1,num2,num3,num4,num5:
            if num == str(1):
                num_list.append(num)
        alert=len(num_list)
        self.render("static/F1_alert.html",num=alert)

def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}
    return tornado.web.Application([
    (r"/", MainHandler),
    (r'/post_test/', MainHandler_post),
], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
