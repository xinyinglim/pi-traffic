from gpiozero import LED, Button
from time import sleep

red = LED(4)
yellow = LED(17)
green = LED(27)
pedestrian_green = LED(22)
pedestrian_btn = Button(23)

red_duration = 2 #in seconds
yellow_duration = 1
green_duration = 2
pedestrian_duration = 3
traffic_to_pedestrian_buffer_duration = 1

pedestrian_crossing = False

# listen for button push event and changing global variable
def press_pedestrian():
    global pedestrian_crossing
    pedestrian_crossing = True

pedestrian_btn.when_activated = press_pedestrian

while True:
    global pedestrian_crossing
    green.on()
    sleep(green_duration)
    green.off()
    yellow.on()
    sleep(yellow_duration)
    yellow.off()
    red.on()
    if not pedestrian_crossing:
        sleep(red_duration)
    else :  
        print("pedestrian")
        sleep(traffic_to_pedestrian_buffer_duration)
        pedestrian_green.on()
        sleep(pedestrian_duration)
        pedestrian_green.off()
        sleep(traffic_to_pedestrian_buffer_duration)
        pedestrian_crossing = False
        continue
    red.off()

