#!/usr/bin/env python3

from adxl345 import ADXL345
import json
import time

def get_graph_data():

    adxl345 = ADXL345()
    axes = adxl345.getAxes(True)

    graph_to_send = json.dumps({
        'x':axes['x'],
        'y':axes['y'],
        'z':axes['z']
    })
    return graph_to_send


if __name__ == '__main__':
    while True:
        data = get_graph_data()
        print(data)
        time.sleep(0.5)

