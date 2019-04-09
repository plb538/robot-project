#!/usr/bin/env python

import RPi.GPIO as gpio
from inputs import devices,get_gamepad
import time


def quantize(value, new_min=0, new_max=255, orig_min=0, orig_max=1023):
    result = int(((float(value) - float(orig_min))*(float(new_max) - float(new_min)) / (float(orig_max) - float(orig_min)) + float(new_min)))
    return result



if __name__ == "__main__":
    print("Hello Boyz")

    for device in devices:
        print(device)

    left_x = 0
    left_y = 0

    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_X":
                left_x = event.state
            elif event.code == "ABS_Y":
                left_y = event.state
        print("Quantized X: {}".format(quantize(left_x, orig_min=-32768, orig_max=32768)))
        print("Quantized Y: {}".format(quantize(left_y, orig_min=-32768, orig_max=32768))) 
