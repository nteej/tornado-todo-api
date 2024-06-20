# handlers.py
import tornado.web
from models import SessionLocal, TodoItem

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = SessionLocal()

    def on_finish(self):
        self.db.close()

class TodoHandler(BaseHandler):
    async def get(self):
        todos = self.db.query(TodoItem).all()
        self.write({"todos": [{"id": todo.id, "title": todo.title, "description": todo.description} for todo in todos]})

    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        new_todo = TodoItem(title=data['title'], description=data['description'])
        self.db.add(new_todo)
        self.db.commit()
        self.write({"message": "Todo item created", "todo": {"id": new_todo.id, "title": new_todo.title, "description": new_todo.description}})