from flask import Flask, render_template, request #, redirect, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/', methods = ['POST', 'GET'])
def req2ser():
    if request.method == 'GET':
        print('GET over HERE')
    if request.method == 'POST':
        print('POST over HERE')

socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(message):
    print('received msg: ' + message)
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)