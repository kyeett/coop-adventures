from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
import pyqrcode

app = Flask(__name__)


@app.route('/joined')
def joined():
    return "Joined the game successfully!"


@app.route('/qrcode')
def qr():


    # Create qr code
    if not os.path.exists('static/code.png'):
        url = pyqrcode.create("http://" + request.host + "/joined", error='Q', version=8)
        url.png('static/code.png', scale=3, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

    # Serve page
    return render_template('qrcode.html')


@app.route('/')
def routing():
    return "Foo is whenever I'm with you" + request.host


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
