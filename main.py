from flask import Flask, render_template
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

sudukoSolver = Flask(__name__)

@sudukoSolver.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    sudukoSolver.run(host=ip_address, port=1001, debug=False)