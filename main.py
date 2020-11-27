def on_button_pressed_a():
    music.play_melody("G F A G F A F G ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        """)
    basic.show_leds("""
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
