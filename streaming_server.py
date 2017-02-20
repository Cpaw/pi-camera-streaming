# coding:utf-8
import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class StreamingServer(WebSocket):
    clients = []

    def handleConnected(self):
        print('Connected:', self.address)
        self.clients.append(self)

    def handleClose(self):
        print('Closed:', self.address)
        self.clients.remove(self)

    def handleMessage(self):
        print('Received:', self.address, self.data)

    @classmethod
    def send_data(self, data):
        for c in self.clients:
            c.sendMessage(data)

    @classmethod
    def new(self, port):
        return SimpleWebSocketServer('', port, StreamingServer)

    @classmethod
    def run_thread(self, server):
        threading.Thread(target=server.serveforever).start()
