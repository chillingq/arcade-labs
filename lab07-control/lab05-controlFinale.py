import arcade

import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class Triangle:
    """ This class manages a triangle bouncing on the screen. """

    def __init__(self, position_x_side, position_y_side1, position_x_peak, position_y_peak
                ,position_y_side2, change_x_side, change_x_peak, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x_side = position_x_side
        self.position_y_side1 = position_y_side1
        self.position_x_peak = position_x_peak
        self.position_y_peak = position_y_peak
        self.position_y_side2 = position_y_side2
        self.change_x_side = change_x_side
        self.change_x_peak = change_x_peak
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_triangle_filled(self.position_x_side, self.position_y_side1, self.position_x_peak,
                                    self.position_y_peak,
                                    self.position_x_side, self.position_y_side2, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_x_side += self.change_x_side
        self.position_x_peak += self.change_x_peak

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x_side > SCREEN_WIDTH:
            self.change_x_side *= -1

        if self.position_x_peak > SCREEN_WIDTH:
            self.change_x_peak *= -1

        if self.position_x_side < 0:
            self.change_x_side *= -1

        if self.position_x_peak < 0:
            self.change_x_peak *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Attributes to store where our triangle is
        self.tri_x_side = 135
        self.tri_x_peak = 200
        self.tri_y_side1 = 290
        self.tri_y_side2 = 260
        self.tri_y_peak = 275

        self.triangle = Triangle(self.tri_x_side, self.tri_y_side1, self.tri_x_peak, self.tri_y_peak,
                                    self.tri_y_side2, 5, 5 , arcade.color.MAROON)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        self.triangle.draw()
    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.triangle.update()
def main():
    window = MyGame(1200, 600, "Ventana")

    arcade.run()


main()