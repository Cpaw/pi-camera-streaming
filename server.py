#!/usr/bin/env python3
# coding:utf-8
import sys
import threading
import html_server
from camera_streaming import CameraStreaming
from streaming_server import StreamingServer

if len(sys.argv) < 4:
    print('usage: python3', __file__, 'width height framerate html_port websocket_port')
    print('example: python3', __file__, '640 480 30 6000 7000')
    sys.exit(1)

width, height, framerate, html_port, ws_port = map(lambda s: int(s), sys.argv[1:])

html_server.html_port = html_port
html_server.ws_port = ws_port


print('Initialize camera')
camera = CameraStreaming(width, height, framerate)

print('Launch websocket server port', ws_port)
server = StreamingServer.new(ws_port)
StreamingServer.run_thread(server)

print('Launch HTML server port', html_port)
html_server.run_thread()

print('Streaming Start!')
camera.streaming(StreamingServer.send_data)
