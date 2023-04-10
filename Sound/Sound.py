import arcade




class MySound(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        self.pipe_sound = arcade.load_sound("unodostres.mp3")
        self.pipe_sound_player = None

    def on_key_press(self, key, modifiers):
        # If the user hits  the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            if not self.pipe_sound_player or not self.pipe_sound_player.playing:
                self.pipe_sound_player = arcade.play_sound(self.pipe_sound)







def main():
    window = MySound(200, 200)
    arcade.run()

main()