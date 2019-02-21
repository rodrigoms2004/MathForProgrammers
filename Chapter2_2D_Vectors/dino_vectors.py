import sys
# sys.path.append('./util')
# print(sys.path)

from util.vector_drawing import *


dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

draw_axes(plane)
draw_grid(plane)
draw_origin(plane)
set_bounds(plane, (-8,-8), (8,8))
draw_points(plane, dino_vectors)
# draw_segment(plane, (6,4), (3,1), color='blue')
connect_the_dots(plane, dino_vectors, color='blue')
display(plane)


