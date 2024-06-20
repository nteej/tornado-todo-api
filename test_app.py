# test_app.py
import pytest
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.testing import AsyncHTTPTestCase, gen_test
from models import Base, engine, SessionLocal, TodoItem
from app import make_app
import json

class TodoTest(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def setUp(self):
        super().setUp()
        Base.metadata.create_all(bind=engine)
        self.session = SessionLocal()

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)
        self.session.close()
        super().tearDown()

    @gen_test
    async def test_get_todos(self):
        response = await self.http_client.fetch(self.get_url('/todos'))
        self.assertEqual(response.code, 200)
        response_data = json.loads(response.body.decode())
        self.assertEqual(response_data, {"todos": []})

    @gen_test
    async def test_create_todo(self):
        data = {"title": "Test Title", "description": "Test Description"}
        response = await self.http_client.fetch(
            self.get_url('/todos'), method="POST", body=json.dumps(data)
        )
        self.assertEqual(response.code, 200)
        response_data = json.loads(response.body.decode())
        self.assertIn("todo", response_data)
        self.assertEqual(response_data["todo"]["title"], "Test Title")
        self.assertEqual(response_data["todo"]["description"], "Test Description")

if __name__ == "__main__":
    pytest.main()