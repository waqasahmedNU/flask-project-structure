from app import App
from app.configuration import Config

app = App('development').initialize()
# app = app('production').initialize()
# print(app.url_map)

if __name__ == "__main__":
    app.run(Config.HOST, Config.PORT)
