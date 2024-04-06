カウンター = 0

def on_button_pressed_a():
    global カウンター
    カウンター = randint(0, 10)
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)
