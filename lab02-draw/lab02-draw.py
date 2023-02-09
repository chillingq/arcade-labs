import arcade

# Import arcade module

"""
ESTRELLA DE DAVID
"""
arcade.open_window(599, 599, "Drawing Example")
arcade.set_background_color(arcade.csscolor.CRIMSON)

arcade.start_render()
arcade.draw_triangle_filled(100, 150, 300, 550, 500, 150, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(100, 449, 300, 50, 500, 449, arcade.csscolor.BLACK)
arcade.finish_render()
arcade.run()