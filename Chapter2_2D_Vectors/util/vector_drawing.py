from math import sqrt, pi
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def draw_origin(plane):
    plt, ax = plane
    plt.scatter([0],[0], color='k', marker='x')

def draw_polygon(plane, vertices):
    plt, ax = plane
    patches = []
    polygon = Polygon(vertices, True)
    patches.append(polygon)
    p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
    colors = 100*np.random.rand(len(patches))
    p.set_array(np.array(colors))
    ax.add_collection(p)

def draw_vectors(plane, vectors, color=None):
    plt, ax = plane
    xs = map(lambda x:x[0], vectors)
    ys = map(lambda x:x[1], vectors)
    plt.scatter(xs,ys,color=color)

def draw_arrow(plane, tail, head, color=None):
    plt, ax = plane
    head_length = 0.4
    length = sqrt((head[1]-tail[1])**2 + (head[0]-tail[0])**2)
    new_length = length - head_length
    new_y = (head[1] - tail[1]) * (new_length / length)
    new_x = (head[0] - tail[0]) * (new_length / length)
    ax.arrow(tail[0], tail[1], new_x, new_y,
    #head_width=0.05, head_length=0.1,
    head_width=0.2, head_length=head_length,
    fc=color, ec=color)

def draw_segment(plane, p1,p2, color=None):
    plt, ax = plane
    x1, y1 = p1
    x2, y2 = p2
    plt.plot([x1,x2],[y1,y2], color=color)

def draw_grid(plane):
    plt, ax = plane
    ax.set_xticks(np.arange(-20,20,1))
    ax.set_yticks(np.arange(-20,20,1))
    plt.grid(True)
    ax.set_axisbelow(True)

def set_bounds(plane, bottom_left, top_right):
    plt, ax = plane
    xmin,ymin = bottom_left
    xmax,ymax = top_right
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)

def connect_the_dots(plane, vectors, color=None):
    for i in range(0,len(vectors)):
        draw_segment(plane, vectors[i], vectors[(i+1)%len(vectors)], color=color)

def draw_axes(plane):
    plt, ax = plane
    ax.axhline(linewidth=1, color='k')
    ax.axvline(linewidth=2, color='k')

def display(plane):
    plt, ax = plane
    plt.show()

def draw_points(plane, vectors):
    x, y = zip(*vectors)
    plt.scatter(x, y)
    # plt.axis([-8, 8, -8, 8])

import numpy as np

import matplotlib.pyplot as plt

plane = plt, plt.subplots()[1]