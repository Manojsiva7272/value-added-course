import tkinter as tk
from tkinter import messagebox

# Function to check for a win or a tie
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    for row in board:
        if "" in row:
            return None
    return "Tie"

# Function to handle button clicks
def on_button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and winner is None:
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        result = check_winner()
        if result:
            if result == "Tie":
                messagebox.showinfo("Result", "It's a tie!")
            else:
                messagebox.showinfo("Result", f"Player {result} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, buttons, current_player, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
    current_player = "X"
    winner = None

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Initialize game variables
current_player = "X"
winner = None
board = [["" for _ in range(3)] for _ in range(3)]

# Create buttons for the game board
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(window, text="", font=('Arial', 24), width=5, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Run the main loop
window.mainloop()
