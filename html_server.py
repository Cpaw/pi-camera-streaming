# coding:utf-8
import threading
import netifaces
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
html_port = None
ws_port = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streaming.js')
def streaming_js():
    ws_server = 'ws://%s:%d' % (get_my_ip(), ws_port)
    return render_template('streaming.js', ws_server=ws_server)

def get_my_ip():
    device = netifaces.gateways()['default'][netifaces.AF_INET][1]
    return netifaces.ifaddresses(device)[netifaces.AF_INET][0]['addr']

def run_thread():
    threading.Thread(target=lambda: app.run(host='', port=html_port, debug=True, use_reloader=False)).start()
