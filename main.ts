let カウンター = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    カウンター = randint(0, 10)
    if (pins.digitalReadPin(DigitalPin.P0) == 1) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.No)
    }
    
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
})
