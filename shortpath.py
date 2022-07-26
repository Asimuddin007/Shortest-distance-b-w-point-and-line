from __future__ import annotations
lines: list = [[[1, -1], [1, 1]], [[2, -1], [2, 1]]]

angle: int = 0

distance: list = []

import math

def distance_between_point_and_line(pt1, pt2) -> tuple[list, float] | None:
   a = pt2[1] - pt1[1]  # y2-y1
   b = pt2[0] - pt1[0]  # x2-x1
   if (a == 0 and angle == 0) or (angle == 90 and b == 0):
       return
   elif b != 0:
       slope = a / b
       c = pt1[1] - (slope * pt1[0])
       slope_origin = math.tan(math.radians(angle))
       x_intercept = round(c / (slope_origin - slope), 2)
       y_intercept = round(slope * x_intercept + c, 2)
   else:
       x_intercept = pt1[0]  # x1
       slope_origin = (math.tan(math.radians(angle)))
       y_intercept = slope_origin * x_intercept
   if min(pt1[0], pt2[0]) <= x_intercept <= max(pt1[0], pt2[0]) and min(pt1[1], pt2[1]) <= \
           y_intercept <= max(pt1[1], pt2[1]):
       return [pt1, pt2], round(math.dist((0, 0), (x_intercept, y_intercept)), 2)



for l in lines:
   P, Q = l
   print(P, Q)
   val = distance_between_point_and_line(P, Q)
   distance.append(val)


if len(distance) != 0:
    print(min(distance, key=lambda t: t[0]))
else:
    print("No intersection!")





