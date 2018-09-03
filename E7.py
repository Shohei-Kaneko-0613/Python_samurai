import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E7.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        text=self.get_argument('text1')
        file="static/E7_POST_TEXT"
        with open(file,"a")  as f:
            f.write(text)
        self.render("static/E7.html")
        

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
