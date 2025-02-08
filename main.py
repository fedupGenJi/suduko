from flask import Flask, render_template, request, jsonify
import socket
from operations import *

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

sudukoSolver = Flask(__name__)

@sudukoSolver.route('/')
def home():
    return render_template('home.html')

@sudukoSolver.route("/solve", methods=["POST"])
def solveSudoku():
    data = request.get_json()
    board = data.get("board", [])
    printBoard(board)

if __name__ == '__main__':
    sudukoSolver.run(host=ip_address, port=1001, debug=False)