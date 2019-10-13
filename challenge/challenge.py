from gpiozero import LED, Button
from time import sleep

# to declare a LED on GPIO Pin 4
red = LED(4)

# to switch on and off LED
red.on()
sleep(2) # waits 2 seconds
red.off()

# to declare a Button on GPIO Pin 23
pedestrian_button = Button(23)

# to listen to button press
def function_to_run():
    print("Button is pressed")
    red.on()
    red.off()

pedestrian_button.when_activated = function_to_run

# Challenge: Create a traffic light that cycles through green, yellow and red
# When a pedestrian presses the button, the traffic light should cycle to red
# stop, and the pedestrian light should turn on. Then continue