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
    #printBoard(board)
    emptyBoxes = countEmpty(board)
    if(solver(board,emptyBoxes)):
        #print("Solved Board:")
        #printBoard(board)
        return jsonify({"status": "success", "board": board})
    else:
        #print("Could not solve")
        return jsonify({"status": "failure", "message": "Could not solve the board"})

if __name__ == '__main__':
    sudukoSolver.run(host=ip_address, port=1001, debug=False)