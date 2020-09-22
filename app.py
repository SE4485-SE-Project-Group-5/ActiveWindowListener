import os
import platform
import shutil
import sys
from subprocess import PIPE, Popen
from threading import Thread

from flask import Flask, render_template
from flask_cors import CORS
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from apis.input_methods.icons_helper import find_and_save_all_icons
from apis.input_methods.mouse_and_keyboard_listener import start_listeners
from flask_blueprints.example_bp import example_bp, example_ws
from flask_blueprints.webview_bp import webview_bp

from config import BUNDLE_DIR

OS = str(platform.system()).lower()
SIGKILL = 9

app = Flask(__name__, static_folder="static", template_folder="templates")

CORS(app)

# Disables caching for each flair app that uses PyWebView
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

# Registers webview API's under /webview/<api-name> to keep code separate and clean
app.register_blueprint(webview_bp, url_prefix='/webview_bp')
app.register_blueprint(example_bp, url_prefix='/example_bp')

ws = Sockets(app)

ws.register_blueprint(example_ws, url_prefix='/example_ws')


@app.after_request
def add_header(response):
    """
        Disables caching for each flair app that uses PyWebView
    """
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route("/")
def home():
    """
        Templates should be stored inside templates folder
    """
    return render_template("index.html")


def kill_port(port):
    process = Popen(
        ["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, _ = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:
        data = [x for x in process.split(" ") if x != '']
        if len(data) <= 1:
            continue

        os.kill(int(data[1]), SIGKILL)


def run_app(url, port):
    find_and_save_all_icons(os.path.join(BUNDLE_DIR, "static/icons"))

    server = pywsgi.WSGIServer(
        (url, port), app, handler_class=WebSocketHandler)
    server.serve_forever()
    # app.run(host=url, port=port, threaded=True)


if __name__ == '__main__':
    """
        App can be launched from this file itself
        without needing to package or launch Window.
        Can be useful for chrome tools debugging. Make sure port number
        is the same as in flair.py
    """
    t = Thread(target=start_listeners, args=())
    t.start()
    print("Listeners started")
    run_app('localhost', port=43968)
