from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

import pyqrcode

app = Flask(__name__)


@app.route('/')
def home():
    users = ['Magnus', 'John', 'Andrew', 'Alexandra']
    return render_template('home.html', user_list=users)


@app.route('/joined')
def joined():
    return "Joined the game successfully!"


def add_logo():
    from PIL import Image
    img = Image.open('static/zombie_small.png', 'r')
    img_w, img_h = img.size
    background = Image.open('static/code.png', 'r')
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    background.save('out.png')


@app.route('/qrcode')
def qr():

    # Create qr code
    url = pyqrcode.create("http://" + request.host + "/joined", error='Q', version=8)
    url.png('static/code.png', scale=3, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    add_logo()

    # Serve page
    return render_template('qrcode.html')


@app.route('/foobar')
def routing():
    return "Foo is whenever I'm with you" + request.host


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
