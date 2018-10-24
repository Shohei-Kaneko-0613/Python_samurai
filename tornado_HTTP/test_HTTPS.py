import tornado.httpserver
import tornado.ioloop
import tornado.web

class getToken(tornado.web.RequestHandler):
    def get(self):
        self.render("../static/tornado_post_html.html")

application = tornado.web.Application([
    (r'/', getToken),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": "./ca.csr",
        "keyfile": "./ca.key",
    })
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
