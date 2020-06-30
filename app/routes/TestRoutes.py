from app.routes import api
from app.resources.example_resource import TestResource

api.add_resource(TestResource, 'test_api', 'todo_ep')