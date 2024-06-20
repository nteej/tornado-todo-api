# app.py
import tornado.ioloop
import tornado.web
from handlers import TodoHandler

def make_app():
    return tornado.web.Application([
        (r"/todos", TodoHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()