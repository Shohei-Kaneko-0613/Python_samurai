
import tornado.ioloop
import tornado.web

class PostHandler(tornado.web.RequestHandler):
    def post(self):
        program_content = self.request.files["files_index"][0]["body"]
        filename = self.request.files["files_index"][0]["filename"]
        print(program_content)
        print(type(program_content))
        print(filename)
        filename = "server_directory/" + filename
        with open(filename,"wb") as f:
            print(f)
            f.write(program_content)
 
app = tornado.web.Application([
        (r"/post/", PostHandler)
    ])

app.listen(8888)
tornado.ioloop.IOLoop.current().start()
