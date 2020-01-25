#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math
import sys
from PIL import Image

w, h = 512, 512
z = 1
if len(sys.argv) > 2:
    z = 2 ** float(sys.argv[2])

img = Image.new('RGBA', (w, h), (29, 31, 33, 0))
pixels = img.load()

f = {0:1, 1:1}
l = {0:2, 1:1}

def fib(n):
    if n not in f:
        f[n] = fib(n - 1) + fib(n - 2)
    return f[n]

def luc(n):
    if n not in l:
        l[n] = luc(n - 1) + luc(n - 2)
    return l[n]

def pol_to_xy(r, t):
    x = r * math.cos(t) + (w / 2)
    y = -r * math.sin(t) + (h / 2)
    return (x, y)

def point(x, y, s, c = (255, 255, 255, 255)):
    for i in xrange(-s, s + 1):
        for j in xrange(-s, s + 1):
            xx, yy = x + i, y + j
            if xx >= 0 and yy >= 0 and xx < w and yy < h:
                pixels[xx, yy] = c

for i in xrange(150):
    t = fib(i)
    r = t / z
    x, y = pol_to_xy(r, t)
    s = 1 + int(2 * r * 10 / w)
    point(x, y, s, (204, 102, 102, 255))
    if r > w:
        print i
        break

for i in xrange(150):
    t = luc(i)
    r = t / z
    x, y = pol_to_xy(r, t)
    s = 1 + int(2 * r * 10 / w)
    point(x, y, s, (129, 162, 190, 255))
    if r > w:
        print i
        break

img.save(sys.argv[1])
