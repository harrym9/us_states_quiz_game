import turtle
import pandas
from write_state import WriteState
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import sys
import time
import tkinter as tk
from tkinter import ttk

# Initialize screen
screen = turtle.Screen()
screen.title("U.S. States Game")
usa_image = "./data/blank_states.png"  # Make sure this path is correct
screen.setup(width=725, height=491)
screen.bgpic(usa_image)  # Set the image as the background

data = pandas.read_csv("./data/50_states.csv")
state_list = data["state"].to_list()
ycor_list = data["y"].to_list()
xcor_list = data["x"].to_list()

guessed_list = []
score = 0
wrong_counter = 0
wrong_list = []  # Keep track of wrong answers

app = QApplication(sys.argv)

def style_input_dialog():
    """Styled input dialog for asking user to guess a state."""
    dialog = QInputDialog()
    dialog.setWindowTitle("U.S. States Quiz")
    dialog.setLabelText(f"{score}/50 States Correct\nWhat's another state name?")

    # Set font and background color
    font = QFont("Arial", 12)
    dialog.setFont(font)

    palette = dialog.palette()
    palette.setColor(QPalette.Background, QColor("#f0f8ff"))  # Light blue background
    dialog.setPalette(palette)

    # Set the text color
    dialog.setStyleSheet("QLabel {color: #2c3e50;}")  # Dark text color

    # Set window position (x=100, y=100 for example)
    dialog.move(100, 100)  # Change this to the desired coordinates

    # Show dialog
    if dialog.exec_():
        return dialog.textValue().title()
    return None


def update_screen_message(message):
    """Updates the screen title with the given message."""
    screen.title(message)

def clear_previous_answer():
    """Clears the previous answer from the screen."""
    turtle.undo()  # Undo the last drawn state name (only text, not the map)

def handle_answer(answer):
    """Handles the user's answer and updates the game state."""
    global score, wrong_counter
    if answer:
        clear_previous_answer()
        if answer in state_list and answer not in guessed_list:
            index = state_list.index(answer)
            score += 1
            guessed_list.append(answer)
            wrong_counter = 0  # Reset wrong counter after a correct answer
            WriteState(state_list[index], xcor_list[index], ycor_list[index])  # Write the state name on map
            update_screen_message(f"{score}/50 States Correct - Keep Going!")
        elif answer in guessed_list:
            update_screen_message("Already Guessed! Try another one.")
            wrong_counter += 1
        else:
            update_screen_message("Invalid State! Try again.")
            wrong_counter += 1
        
        # Provide hint after 3 consecutive wrong answers
        if wrong_counter == 3:
            remaining_states = [state for state in state_list if state not in guessed_list]
            hint = remaining_states[0]  # Provide a hint from the remaining states
            update_screen_message(f"Hint: Try {hint}.")
            wrong_counter = 0  # Reset after giving the hint
            time.sleep(1)  # Pause before continuing

def display_remaining_states():
    """Displays unanswered states in red."""
    for state in [state for state in state_list if state not in guessed_list]:
        index = state_list.index(state)
        WriteState(state, xcor_list[index], ycor_list[index], "red")  # Display unanswered states in red

def create_results_window():
    """Creates and displays the results window with a table."""
    root = tk.Tk()
    root.title("Game Results")
    root.geometry("700x500")

    tree = ttk.Treeview(root, columns=("State", "Correct/Incorrect"))
    tree.heading("#1", text="State")
    tree.heading("#2", text="Correct/Incorrect")
    tree['show'] = 'headings'  # Hide the default first empty column

    # Style the table
    tree.tag_configure("correct", background="lightgreen")
    tree.tag_configure("incorrect", background="lightcoral")
    tree.tag_configure("unanswered", background="lightyellow")

    # Adding correct and incorrect guesses to the table
    for state in state_list:
        tree.insert("", "end", values=(state, "Correct" if state in guessed_list else "Incorrect"), tags=("correct" if state in guessed_list else "incorrect"))

    # Adding the unguessed states to the table
    tree.insert("", "end", values=("Incorrect attempts:", wrong_counter), tags=("incorrect",))

    # Add the table to the Tkinter window
    tree.pack(padx=10, pady=10, expand=True, fill="both")

    # Display final results
    final_result_label = tk.Label(root, text=f"Game Over! You guessed {score} states correctly!", font=("Arial", 14))
    final_result_label.pack(pady=10)

    # Display the total score
    score_label = tk.Label(root, text=f"Total Score: {score}/50", font=("Arial", 12))
    score_label.pack(pady=10)

    root.mainloop()

def main():
    clear_previous_answer()
    while score < 50:
        turtle.hideturtle()  # Hide the cursor
        answer = style_input_dialog()
        if answer:
            handle_answer(answer)
        else:
            break  # Exit if user cancels the dialog

    # Display unanswered states in red
    display_remaining_states()
    
    # Create and display the results window
    create_results_window()


if __name__ == "__main__":
    main()
