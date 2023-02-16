
import arcade

arcade.open_window(600, 600, "David")

# Import arcade module


def main():
    """
    ESTRELLA DE DAVID ROJA Y NEGRA
    """


    def fondo():
        """Colorea el fondo"""
        arcade.set_background_color(arcade.csscolor.BLACK)

    arcade.start_render()

    def estrella():
        """Dibuja una estrella de David"""

        #Dibuja los triangulos
        arcade.draw_triangle_outline(110, 190, 300, 520, 490, 190, arcade.csscolor.MAROON, border_width=8)
        arcade.draw_triangle_outline(110, 410, 300, 80, 490, 410, arcade.csscolor.MAROON, border_width=8)



        #Dibuja el circulo de la estrella de David
        arcade.draw_circle_outline(300, 300, 230, arcade.csscolor.MAROON, border_width=8)


        #Escribe el texto en el interior de la estrella
        arcade.draw_text("דם", 255, 290, arcade.csscolor.MAROON, 60)

    arcade.finish_render()
    arcade.run()

def paint_it_gold():
    """
        ESTRELLA DE DAVID BLANCA Y AZUL
        """

    arcade.set_background_color(arcade.csscolor.BLACK)

    arcade.start_render()

    # triangulos
    arcade.draw_triangle_outline(110, 190, 300, 520, 490, 190, arcade.csscolor.GOLD, border_width=8)
    arcade.draw_triangle_outline(110, 410, 300, 80, 490, 410, arcade.csscolor.GOLD, border_width=8)

    # circulo
    arcade.draw_circle_outline(300, 300, 230, arcade.csscolor.GOLD, border_width=8)

    # texto
    arcade.draw_text("דם", 255, 290, arcade.csscolor.GOLD, 60)

    arcade.finish_render()
    arcade.run()


def paint_it_white():
    """
        ESTRELLA DE DAVID BLANCA Y AZUL
        """

    arcade.set_background_color(arcade.csscolor.NAVY)

    arcade.start_render()

    # triangulos
    arcade.draw_triangle_outline(110, 190, 300, 520, 490, 190, arcade.csscolor.GHOST_WHITE, border_width=8)
    arcade.draw_triangle_outline(110, 410, 300, 80, 490, 410, arcade.csscolor.GHOST_WHITE, border_width=8)

    # circulo
    arcade.draw_circle_outline(300, 300, 230, arcade.csscolor.GHOST_WHITE, border_width=8)

    # texto
    arcade.draw_text("דם", 255, 290, arcade.csscolor.GHOST_WHITE, 60)

    arcade.finish_render()
    arcade.run()

main()