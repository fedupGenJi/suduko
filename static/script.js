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