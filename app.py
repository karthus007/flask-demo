from flask import Flask
from flask import request, redirect
from myapp.china.route import index

# static_url_path: 静态资源的访问路径
# static_folder: 静态资源的存放路径
# template_folder: 模板的默认存放位置

app_name = "/china"
app = Flask(__name__, static_url_path=app_name, static_folder="static", template_folder="templates")
app.register_blueprint(index.china, url_prefix=app_name)


@app.before_request
def app_before():
    print("请求路径： " + request.path)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8888)
