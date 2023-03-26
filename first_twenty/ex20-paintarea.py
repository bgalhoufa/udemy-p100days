#!/usr/bin/env python

from math import ceil

def paint_calc(height, width, cover):
    total = height * width / cover
    print(f'You\'ll need {ceil(total)} cans')



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


