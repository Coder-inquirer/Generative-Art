from numpy import absolute, sign
from svg_toolkit import *
from random import choice, random, normalvariate, randint, uniform,seed
from opensimplex import OpenSimplex
from math import sin, cos, pi
from palettable.cartocolors.sequential import *
from colorsys import rgb_to_hls
import matplotlib.image as img

def simplex(x=0, y=0, freq=0.004):
    global tmp
    return tmp.noise2d(x*freq, y*freq)

def simplex_reseed():
    global tmp
    tmp = OpenSimplex(randint(0, 10000))

def flowline(nsteps, start_point, step=5, h=0, s=100, l=50, a=1, stroke_width=2):
    points = []
    point = start_point.copy()
    points.append(point.copy())
    for t in range(nsteps):
        angle = 2*pi * simplex(point[0], point[1])
        point[0] += step*cos(angle)
        point[1] += step*sin(angle)
        points.append(point.copy())
    path_c(points, stroke=f'hsla({h:.2f},{s:.2f}%,{l:.2f}%,{a})', stroke_width=stroke_width)

def hls(color):
    arr =  rgb_to_hls(color[0],color[1],color[2])
    return arr[0]*360, arr[1]*100, arr[2]*100

def skew(x,n=1.2):
    return 0.5 + 0.48 * sign(x-0.5)*absolute(((2*x-1))**(1/n))

def choose_cmap():
    return choice([Teal_7.mpl_colors, Sunset_7.mpl_colors, PinkYl_7.mpl_colors, Emrld_7.mpl_colors, Burg_7.mpl_colors])

width = 757
height = 599
init_svg(width, height)

seed()
tmp = OpenSimplex(randint(0, 10000))

step = 10
nsteps = width//step//2
nlines = 10000
stroke_width=10
cmap = choose_cmap()
cl = len(cmap)

image = img.imread("C:\\Users\\Agrim Sharma\\Downloads\\757px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg")
h,l,s = hls([c/255 for c in image[1][width//2]])#cmap[3])
rect(0, 0, width, height, stroke_width="0", fill=f'hsla({h:.2f},{s:.2f}%,{l:.2f}%,{1})')

for i in range(nlines):
    iter = i/nlines
    start_point=[width*skew(random()), height*skew(random())]
    color = [c/255 for c in image[int(start_point[1])][int(start_point[0])]] #choice(cmap[0:int(cl*iter)+1])
    h,l,s = hls(color)
    flowline(nsteps=int(normalvariate(nsteps*(1-iter), nsteps/2)),
             start_point=start_point,
             step=step,
             h=h, l=l,s=s,
             a=1,#round(uniform((1-iter)/2,1),2),
             stroke_width=stroke_width *(1-iter))
    #if i%(nlines//2)==0:
    #    simplex_reseed()

save_svg()