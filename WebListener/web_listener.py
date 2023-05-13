# web_listener.py
import argparse
from flask import Flask, request, jsonify
from threading import Thread

class WebListener:

    def __init__(self, port=80):
        self.subscribers = []
        self.app = Flask(__name__)
        self.port = port
        self.setup_routes()
        self.server_thread = Thread(target=self.run_server)
        self.server_thread.start()

    def setup_routes(self):
        @self.app.route('/', methods=['POST'])
        def handle_data():
            data = request.json
            self.notify(data)
            return jsonify(success=True)

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, data):
        for callback in self.subscribers:
            callback(data)

    def run_server(self):
        self.app.run(port=self.port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=80, help='Port number for the web server')
    args = parser.parse_args()

    wl = WebListener(port=args.port)
