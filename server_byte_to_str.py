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
        with open(filename,"w") as f:
            print(f)
            content_decoded = program_content.decode()
            print(content_decoded)
            print(type(content_decoded))
            f.write(content_decoded)
 
app = tornado.web.Application([
        (r"/post/", PostHandler)
    ])

app.listen(8888)
tornado.ioloop.IOLoop.current().start()
