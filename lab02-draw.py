<<<<<<< HEAD
import arcade




# Import arcade module

"""
ESTRELLA DE DAVID
"""
arcade.open_window(599, 599, "Drawing Example")
arcade.set_background_color(arcade.csscolor.CRIMSON)

arcade.start_render()
arcade.draw_triangle_filled(129, 179, 299, 549, 469, 179, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(129, 419, 299, 49, 469, 419, arcade.csscolor.BLACK)
arcade.finish_render()
=======
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
>>>>>>> eec112e4ab64526c4a80b8d10dbe0e736a39cb94
arcade.run()