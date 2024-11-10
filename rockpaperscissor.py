import random
import tkinter as tk
from tkinter import messagebox

# Initialize global variables
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)
    
    # Display choices
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    
    # Determine outcome
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    # Display result and update scores
    result_label.config(text=result_label.cget("text") + f"\nResult: {result}")
    score_label.config(text=f"Scores - You: {user_score} | Computer: {computer_score}")

# Function to handle reset
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Scores - You: 0 | Computer: 0")

# Main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Instruction label
instruction_label = tk.Label(window, text="Choose rock, paper, or scissors to play!", font=("Arial", 14))
instruction_label.pack(pady=10)

# Result label
result_label = tk.Label(window, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(window, text="Scores - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Buttons for user choices
rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Start the tkinter event loop
window.mainloop()