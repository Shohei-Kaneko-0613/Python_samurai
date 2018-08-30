import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E6.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        button1=self.get_argument('but1','1')
        button2=self.get_argument('but3','2')
        button3=self.get_argument('but3','3')
        #print(button1)
        #print(button3)

        if button1==1:
            self.write(button1)
            self.write("button1")
        elif button1==2:
            self.write(button1)
            self.write("button2")
        elif button1==3:
            self.write(button1)
            self.write("button3")


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
