from app.routes import api
from app.resources.example_resource import ExampleResource

api.add_resource(ExampleResource, 'test_api', 'todo_ep')

