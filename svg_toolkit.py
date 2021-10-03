from random import randint, normalvariate
from math import sin, pi

filename = "temp.svg"
fout = open(filename, 'w')


def init_svg(width=400, height=400, fout=fout):
    fout.write(
        f'<svg version="1.1" height="{height}" width="{width}" xmlns="http://www.w3.org/2000/svg">')


def save_svg(fout=fout):
    fout.write("</svg>")
    fout.close()


def line(x1, y1, x2, y2, stroke='black', stroke_width=1, fout=fout):
    fout.write(
        f'<line x1="{x1}" x2="{x2}" y1="{y1}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}"/>')


def rect(x, y, width, height, stroke="black", fill="transparent", stroke_width=1, fout=fout):
    fout.write(
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}"  stroke="{stroke}" fill="{fill}" stroke-width="{stroke_width}"/>')

def pixel(x, y, fill="black", size=1, fout=fout):
    fout.write(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{fill}" stroke-width="{0}"/>')

def polyline(points, stroke="black", fill="transparent", stroke_width=1, closed=False, fout=fout):
    point_str = " ".join([f'{point[0]:.2f},{point[1]:.2f}' for point in points])
    z = "z " if closed else ""
    fout.write(
        f'<polyline points="{point_str}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" {z}/>')


def path_c(points, stroke="black", fill="transparent", stroke_width=1, closed=False, smooth_factor=0.2, rounding=2, fout=fout):
    d_str = f'M {round(points[0][0], rounding)} {round(points[0][1], rounding)}'
    if len(points) > 2:
        d_str += f' C {round(points[0][0]+(points[1][0]-points[0][0])*smooth_factor,rounding)} {round(points[0][1]+(points[1][1]-points[0][1])*smooth_factor, rounding)}, {round(points[1][0]-(points[2][0]-points[0][0])*smooth_factor, rounding)} {round(points[1][1]-(points[2][1]-points[0][1])*smooth_factor, rounding)}, {round(points[1][0], rounding)} {round(points[1][1], rounding)}'

        for i in range(2, len(points)-1):
            d_str += f' S {round(points[i][0]+(points[i-1][0]-points[i+1][0])*smooth_factor, rounding)} {round(points[i][1]+(points[i-1][1]-points[i+1][1])*smooth_factor, rounding)}, {round(points[i][0], rounding)} {round(points[i][1], rounding)}'
        i = len(points)-1
        d_str += f' S {round(points[i-1][0]-(points[i][0]-points[i-1][0])*smooth_factor, rounding)} {round(points[i-1][1]-(points[i][1]-points[i-1][1])*smooth_factor, rounding)}, {round(points[i][0], rounding)} {round(points[i][1], rounding)}'
    z = "z " if closed else ""
    
    fout.write(
        f'<path d="{d_str}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" {z}/>')

"""
width = 400
height = 400
init_svg(width, height)
rect(0, 0, width, height)

step = 10
amp = 160
hstep = 2
klim = 400
for k in range(klim):
    y_disp = 1.5*height*(k/klim)**0.3
    phase = sin(4*k/klim)*5*pi
    points = []
    for i in range(0, width+step, step):
        points.append([i, y_disp+amp/2*(-sin(phase+i/width*2*pi))])
        points[-1][1] += normalvariate(0, (k/klim)**0.5*hstep)
    path_c(points)
save_svg()
"""
""" 
box_size=10
for i in range(height//box_size):
    for j in range(width//box_size):
        if randint(0,1)==0:
            line(j*box_size, i*box_size, (j+1)*box_size, (i+1)*box_size)
        else:
            line((j+1)*box_size, i*box_size, j*box_size, (i+1)*box_size)
 """
