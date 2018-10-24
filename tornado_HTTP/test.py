import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../static/tornado_post_html.html")

class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, samurai")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	(r"/test/", MainHandler2),
    ])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(make_app, ssl_options={
        "certfile":"server.crt",
        "keyfile":"server.key",
    })

#    app = make_app()
#    app.listen(8888)
    http_server.listen(443)
tornado.ioloop.IOLoop.current().start()