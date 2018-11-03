import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
	<!DOCTYPE html>
	<html>
	<head>
	</head>
	<body>
	<a href="http://localhost:8888/test/">jump to link!</a>
	</body>
	</html>

''')

class MainHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write('''
	<!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <p>hello,world</p>
        </body>
        </html>
''')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	(r"/test/", MainHandler2),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
