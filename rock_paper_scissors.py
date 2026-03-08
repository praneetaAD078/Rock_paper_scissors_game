#TASK 4 - Rock paper scissors game
import gradio as gr
import random

# Score tracking
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

def play_game(user_choice):
    global user_score, computer_score

    # Get computer's choice
    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Display results
    return f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}\n\nScore -> You: {user_score} | Computer: {computer_score}"

# Gradio UI
game_interface = gr.Interface(
    fn=play_game,
    inputs=gr.Radio(choices, label="Choose Rock, Paper, or Scissors"),
    outputs="text",
    title="Rock-Paper-Scissors Game",
    description="Play Rock-Paper-Scissors against the computer. Click a choice to begin!"
)

# Launch the game
game_interface.launch()

