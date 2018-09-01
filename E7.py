import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E7.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        item=[]
        text1=self.get_argument('text1')
        
        item.append(text1)
        #print(item)

        self.render("static/E7.html",item=item)


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