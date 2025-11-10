"""
This script draws a Mystical Fractal Flower. The user can specify the
recursion depth, size, and color scheme of the flower, creating a unique visual.

@author: Bridgette Mi (bmi@macalester.edu)
"""
import turtle


def get_user_input():
    """
    Prompts the user for drawing parameters using turtle's input dialogs.
    Validates the color scheme input.
    Returns:
        tuple: A tuple containing (size, depth, color_palette).
    """
    # Setup a temporary screen for input dialogs
    input_screen = turtle.Screen()
    input_screen.setup(width=600, height=400)  # Give some space for dialogs

    # Get fractal depth from user
    depth = turtle.numinput(
        "Input: Fractal Depth",
        "Enter the recursion depth (e.g., 3-6):",
        default=4, minval=1, maxval=7
    )

    # Get base size from user
    size = turtle.numinput(
        "Input: Flower Size",
        "Enter the base size for the petals (e.g., 80-150):",
        default=120, minval=50, maxval=200
    )

    # Define color schemes
    color_schemes = {
        "fire": ["#FF0000", "#FF4500", "#FFA500", "#FFD700", "#FFFF00"],
        "ice": ["#00BFFF", "#1E90FF", "#87CEFA", "#ADD8E6", "#F0F8FF"],
        "forest": ["#006400", "#228B22", "#3CB371", "#90EE90", "#98FB98"]
    }

    # Get color choice from user and validate it
    color_choice = ""
    valid_choices = list(color_schemes.keys())
    while color_choice.lower() not in valid_choices:
        color_choice = turtle.textinput(
            "Input: Color Scheme",
            f"Choose a color scheme: {', '.join(valid_choices)}"
        )
        if color_choice is None:  # User cancelled the dialog
            color_choice = "fire"  # Default to 'fire' if cancelled
            break

    # Clear the temporary setup screen before drawing
    input_screen.clear()

    selected_palette = color_schemes[color_choice.lower()]

    return int(size), int(depth), selected_palette


def setup_screen(title, bgcolor):
    """
    Sets up the turtle screen with a given title and background color.
    Returns:
        turtle.Screen: The configured screen object.
    """
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor(bgcolor)
    screen.tracer(0)  # Turn off automatic screen updates for max speed
    return screen


def draw_branch(t, size, depth, color_palette):
    """
    Recursively draws a single branch of the fractal flower.
    This function demonstrates recursion, conditionals, and variable use.
    Args:
        t (turtle.Turtle): The turtle object to draw with.
        size (int): The current length of the branch.
        depth (int): The current recursion depth.
        color_palette (list): A list of color strings.
    """
    # Base case: if depth is 0, stop the recursion.
    if depth == 0:
        return

    # Set the color based on the current depth
    # This uses a conditional to check if the palette is available
    if color_palette:
        color_index = depth % len(color_palette)
        t.pencolor(color_palette[color_index])

    t.pensize(depth)  # Thicker branches for lower depth
    t.forward(size)

    # Store position and heading to return to later
    position = t.position()
    heading = t.heading()

    # Recursive call for the right sub-branch
    t.right(25)
    draw_branch(t, size * 0.75, depth - 1, color_palette)

    # Return to previous position and draw the left sub-branch
    t.setposition(position)
    t.setheading(heading)
    t.left(25)
    draw_branch(t, size * 0.75, depth - 1, color_palette)

    # Return to the starting point of the branch to complete the symmetrical structure
    t.setposition(position)
    t.setheading(heading)


def draw_flower(t, num_petals, size, depth, color_palette):
    """
    Draws the full flower by arranging petals in a circle.
    This function demonstrates the use of a for loop.
    Args:
        t (turtle.Turtle): The turtle object.
        num_petals (int): The number of petals to draw.
        size (int): The base size of each petal.
        depth (int): The recursion depth for each petal.
        color_palette (list): The list of colors to use.
    """
    angle_turn = 360 / num_petals

    # Loop to draw each petal
    for _ in range(num_petals):
        draw_branch(t, size, depth, color_palette)
        t.right(angle_turn)


def main():
    """
    Main function to orchestrate the drawing process.
    """
    # 1. Get user input for customization
    base_size, recursion_depth, color_palette = get_user_input()

    # 2. Set up the drawing environment
    screen = setup_screen("Mystical Fractal Flower", "black")

    artist = turtle.Turtle()
    artist.hideturtle()
    artist.speed(0)
    artist.left(90)  # Point the turtle upwards initially
    artist.penup()
    artist.goto(0, -250)  # Start drawing from the bottom-center
    artist.pendown()

    # 3. Draw the flower using a function
    number_of_petals = 10
    draw_flower(artist, number_of_petals, base_size, recursion_depth, color_palette)

    # 4. Finalize the drawing
    screen.update()  # Show the final drawing
    screen.exitonclick()  # Keep the window open until clicked


# Run the main function when the script is executed
if __name__ == "__main__":
    main()