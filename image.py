#!/usr/bin/env python3

import random, argparse
from PIL import Image

parser = argparse.ArgumentParser(description='random image generator, file format=png.')
parser.add_argument('width', help='width of the image in pixels', type=int, nargs='?', default=800)
parser.add_argument('height', help='height of the image in pixels', type=int, nargs='?', default=600)
parser.add_argument('xdensity', help='pixel density on x axis', type=int, nargs='?', default=2)
parser.add_argument('ydensity', help='pixel density on y axis', type=int, nargs='?', default=2)
args = parser.parse_args()

pixels = []

for i in range(int(args.height/args.ydensity)):
        temp = []
        for j in range(int(args.width/args.xdensity)):
                color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
                for sdf in range(args.xdensity):
                    temp.append(color)
        for jddj in range(args.ydensity):
            pixels += temp

image = Image.new('RGB', (args.width, args.height))
image.putdata(pixels)
image.save('a.png')
