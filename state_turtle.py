from turtle import Turtle

# Define the font style for the scoreboard text
FONT = ("arial", 10, "normal")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")  # Set the color of the scoreboard text
        self.penup()  # Lift the pen to move without drawing
        self.hideturtle()  # Hide the turtle icon

    def state_position(self, x, y, state):
        """
        Display the game state at the specified position.

        :param x: X-coordinate of the display position
        :param y: Y-coordinate of the display position
        :param state: The game state to be displayed
        """
        self.clear()  # Clear previous state display
        self.goto(x, y)  # Move to the specified position
        self.write(f"{state}", align="center", font=FONT)  # Write the game state
