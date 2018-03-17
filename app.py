from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
import pyqrcode
import logging

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['HOST'] = "0.0.0.0"

socket = SocketIO(app)

@app.route('/joined')
def joined():
    return "Joined the game successfully!"


@socket.on('move')
def handle_message(position):
    logging.error(('position: ', position['x'], position['y']))
    emit('move_broadcast', position, broadcast=True)


@socket.on('message')
def handle_message(message):
    logging.error('received message: ' + message)


@socket.on('json')
def handle_json(json):
    logging.error('received message: ' + str(json))


@socket.on('connected')
def handle_my_custom_event(json):
    logging.error('received message: ' + str(json))


@app.route('/')
def qr():


    # Create qr code
    if not os.path.exists('static/code.png'):
        url = pyqrcode.create("http://" + request.host + "/joined", error='Q', version=8)
        url.png('static/code.png', scale=3, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

    # Serve page
    return render_template('qrcode.html')


@app.route('/touch')
def touch():
    return render_template('touch_movement.html')


if __name__ == '__main__':
    socket.run(app)
