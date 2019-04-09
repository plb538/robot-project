#!/usr/bin/env python

import RPi.GPIO as gpio
from inputs import devices,get_gamepad
import time


def quantize(value, new_min=0, new_max=100, orig_min=0, orig_max=1023):
    result = int(((float(value) - float(orig_min))*(float(new_max) - float(new_min)) / (float(orig_max) - float(orig_min)) + float(new_min)))
    return result


def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

if __name__ == "__main__":
    print("Hello Boyz")
    setup()
    for device in devices:
        print(device)

    plx = gpio.PWM(23, 100)
    plx.start(0)

    ply = gpio.PWM(24, 100)
    ply.start(0)

    left_x = 0
    left_y = 0

    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_X":
                left_x = event.state
            elif event.code == "ABS_Y":
                left_y = event.state
        q_left_x = quantize(left_x, orig_min=-32768, orig_max=32768)
        q_left_y = quantize(left_y, orig_min=-32768, orig_max=32768)
        print("Quantized X: {}".format(quantize(left_x, orig_min=-32768, orig_max=32768)))
        print("Quantized Y: {}".format(quantize(left_y, orig_min=-32768, orig_max=32768))) 
        
        plx.ChangeDutyCycle(q_left_x)
        ply.ChangeDutyCycle(q_left_y)

