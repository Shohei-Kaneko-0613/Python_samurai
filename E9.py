import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E9.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        usr_name=self.get_argument('text1')
        password=self.get_argument('pass1')
        f = open("static/E9-usr-pass","r")
        json_dict=json.load(f)
        try:
            x=json_dict[usr_name]["pw"]
            y=json_dict[usr_name]["id"]

            if usr_name==y and password == x:
                self.render("static/E9_OK.html")
            else:
                self.render("static/E9_NG.html")
        except KeyError:
            self.render("static/E9_NG.html")


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
