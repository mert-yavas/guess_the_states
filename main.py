import turtle
import pandas
from state_turtle import State  # Assuming 'state_turtle.py' contains the 'State' class
import sys

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=730, height=500)
screen.title("U.S. States Game")a

# Load the U.S. states map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the U.S. states data
states_names = pandas.read_csv("50_states.csv")

# Keep track of guessed states and initialize the score
guessed_states = []
score = 0

# Main game loop
while score < 50:
    # Create a new State object
    new_state = State()

    # Get user input for a state
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state?").title()

    # Check if the user wants to exit
    if answer_state == "Exit":
        sys.exit()

    # Skip if the state has already been guessed
    if answer_state in guessed_states:
        continue

    # Check if the guessed state is valid
    if answer_state in states_names["state"].tolist():
        guessed_states.append(answer_state)
        x = int(states_names.loc[states_names["state"] == answer_state, "x"].iloc[0])
        y = int(states_names.loc[states_names["state"] == answer_state, "y"].iloc[0])

        # Display the guessed state on the map and update the score
        new_state.state_position(x, y, answer_state)
        score += 1

# Close the turtle screen on click
screen.exitonclick()
