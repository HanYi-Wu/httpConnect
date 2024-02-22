from flask import Flask

app = Flask(__name__)


@app.route("/test/<thing>")
def haha(thing):
    print(thing)
    ReturnTg = "发送成功"
    return ReturnTg


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)