<<<<<<< HEAD

import arcade




# Import arcade module

"""
ESTRELLA DE DAVID
"""
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.BLACK)

arcade.start_render()
arcade.draw_triangle_outline(110, 190, 300, 520, 490, 190, arcade.csscolor.MAROON, border_width=8)
arcade.draw_triangle_outline(110, 410, 300, 80, 490, 410, arcade.csscolor.MAROON, border_width=8)
arcade.draw_circle_outline(300, 300, 230, arcade.csscolor.MAROON, border_width=8)
arcade.draw_text("דם", 255, 290, arcade.csscolor.MAROON, 60)

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
>>>>>>> d31640cbe5daa00944275327bcb14737e94f0b0c
arcade.run()