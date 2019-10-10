from gpiozero import LED, Button
from time import sleep
# import sys

red = LED(4)
yellow = LED(17)
green = LED(27)
pedestrian_green = LED(22)
pedestrian_btn = Button(23)

# global pedestrian_crossing
# pedestrian_crossing = False
# while True:
def run():
    # global pedestrian_crossing
    pedestrian_crossing = False

    def press_pedestrian():
        nonlocal pedestrian_crossing
        pedestrian_crossing = True

    pedestrian_btn.when_activated = press_pedestrian

    while not pedestrian_crossing:
        red.off()
        green.on()
        sleep(2)
        green.off()
        yellow.on()
        sleep(0.5)
        yellow.off()
        red.on()
        sleep(2)
        
    red.on()
    pedestrian_green.on()
    sleep(2)
    print("pedestrian")
    pedestrian_green.off()
    sleep(2)
    red.off()
    pedestrian_crossing = False
    run()

run()
