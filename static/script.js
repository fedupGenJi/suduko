document.addEventListener("DOMContentLoaded", function () {
    let selectedNumber = null;
    let board = document.getElementById("board");
    let digitsContainer = document.getElementById("digits");

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            let tile = document.createElement("div");
            tile.classList.add("tile");
            tile.dataset.row = i;
            tile.dataset.col = j;
            tile.addEventListener("click", function () {
                if (selectedNumber) {
                    if (this.textContent === selectedNumber) {
                        this.textContent = "";
                    } else {
                        this.textContent = selectedNumber;
                    }
                } else {
                    this.textContent = "";
                }
            });
            board.appendChild(tile);
        }
    }

    for (let i = 1; i <= 9; i++) {
        let number = document.createElement("div");
        number.classList.add("number");
        number.textContent = i;
        number.addEventListener("click", function () {
            if (selectedNumber === this.textContent) {
                selectedNumber = null;
                this.classList.remove("selected");
            } else {
                document.querySelectorAll(".number").forEach(num => num.classList.remove("selected"));

                selectedNumber = this.textContent;
                this.classList.add("selected");
            }
        });
        digitsContainer.appendChild(number);
    }
});

function clearBoard() {
    document.querySelectorAll(".tile").forEach(tile => {
        tile.textContent = "";
    }); 
}

function solveSudoku() {
    if (!isValidBoard()) {
        showPopup("This Sudoku board is invalid. Ensure no duplicates exist in any row, column, or 3×3 box.");
        return;
    }
    // flask code rakhnu prne
}

function isValidBoard() {
    let board = [];
    document.querySelectorAll(".tile").forEach((tile, index) => {
        let row = Math.floor(index / 9);
        let col = index % 9;
        if (!board[row]) board[row] = [];
        board[row][col] = tile.textContent || ".";
    });

    return isValidSudoku(board);
}

function isValidSudoku(board) {
    let rows = Array(9).fill().map(() => new Set());
    let cols = Array(9).fill().map(() => new Set());
    let boxes = Array(9).fill().map(() => new Set());

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            let num = board[r][c];
            if (num !== ".") {
                let boxIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3);
                if (rows[r].has(num) || cols[c].has(num) || boxes[boxIndex].has(num)) {
                    return false;
                }
                rows[r].add(num);
                cols[c].add(num);
                boxes[boxIndex].add(num);
            }
        }
    }
    return true;
}

function showPopup(message) {
    let popup = document.createElement("div");
    popup.classList.add("popup");
    popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn" onclick="closePopup()">&times;</span>
            <img src="https://cdn-icons-png.flaticon.com/512/463/463612.png" class="popup-icon">
            <h2>Invalid Sudoku!</h2>
            <p>${message}</p>
            <button onclick="closePopup()">Got it!</button>
        </div>
    `;
    document.body.appendChild(popup);
}


function closePopup() {
    document.querySelector(".popup").remove();
}