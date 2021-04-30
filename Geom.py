#  File: Geom.py

#  Description: Creates line and point class

#  Student Name:Dane Piper

#  Student UT EID:dap3498

#  Partner Name:Travis West

#  Partner UT EID:tmw2785

#  Course Name: CS 313E

#  Unique Number:50300

#  Date Created:2/11/20

#  Date Last Modified:2/14/20

import math


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance to other which is another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # create a string representation of a Point (x, y)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # test for equality between two points
    def __eq__(self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)


class Line(object):
    # line is defined by two Point objects p1 and p2
    # constructor assign default values if user does not define
    # the coordinates of p1 and p2 or the two points are the same
    def __init__(self, p1_x=0, p1_y=0, p2_x=1, p2_y=1):
        self.p1_x = p1_x
        self.p1_y = p1_y
        self.p2_x = p2_x
        self.p2_y = p2_y

    # returns True if the line is parallel to the x axis
    # and False otherwise
    def is_parallel_x(self):
        p1 = Point(0, self.p1_y)
        p2 = Point(0, self.p2_y)
        return p1.__eq__(p2)

    # returns True if the line is parallel to the y axis
    # and False otherwise
    def is_parallel_y(self):
        p1 = Point(0, self.p1_x)
        p2 = Point(0, self.p2_x)
        return p1.__eq__(p2)

    # determine slope for the line
    # return float ('inf') if line is parallel to the y-axis
    def slope(self):
        if self.is_parallel_y():
            return 'inf'
        else:
            return (self.p2_y - self.p1_y) / (self.p2_x - self.p1_x)

    # determine the y-intercept of the line
    # return None if line is parallel to the y axis
    def y_intercept(self):
        if self.is_parallel_y():
            return None
        else:
            return self.p1_y - self.slope() * self.p1_x

    # determine the x-intercept of the line
    # return None if line is parallel to the x axis
    def x_intercept(self):
        if self.is_parallel_x():
            return None
        else:
            return (0 - self.y_intercept()) / self.slope()

    # returns True if line is parallel to other and False otherwise
    def is_parallel(self, other):
        slope1 = self.slope()
        slope2 = other.slope()
        return slope1 == slope2

    # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular(self, other):
        slope1 = self.slope()
        slope2 = other.slope()
        return slope1 == (0 - (1 / slope2))

    # returns True if Point p is on the line or an extension of it
    # and False otherwise
    def is_on_line(self, p):
        py = self.slope() * p.x + self.y_intercept()
        lines = Point(p.x, py)
        return py == p.y

    # determine the perpendicular distance of Point p to the line
    # return 0 if p is on the line
    def perp_dist(self, p):
        if self.is_on_line(p):
            return 0
        else:
            return abs(self.slope * p.x + p.y + self.y_intercept()) / math.sqrt(self.slope * self.slope() + 1)

    # returns a Point object which is the intersection point of line
    # and other or None if they are parallel
    def intersection_point(self, other):
        if self.is_parallel(other):
            return None
        else:
            x = (other.y_intercept() - self.y_intercept()) / (self.slope() - other.slope())
            y = self.slope() * x + self.y_intercept()
            return Point(x, y)

    # return True if two points are on the same side of the line
    # and neither points are on the line
    # return False if one or both points are on the line or both
    # are on the same side of the line
    def on_same_side(self, p1, p2):
        if self.is_on_line(p1) or self.is_on_line(p2):
            return False
        else:
            return self.slope() * p1.x - self.y_intercept() > p1.y == self.slope() * p2.x - self.y_intercept() > p2.y
    # string representation of the line - one of three cases
    # y = c if parallel to the x axis
    # x = c if parallel to the y axis
    # y = m * x + b
    def __str__(self):
        if self.is_parallel_x():
            return 'y' + '=' + str(self.p1_y)
        elif self.is_parallel_y():
            return 'x' + '=' + str(self.p1.x)
        else:
            return 'y = ' + str(self.slope()) + ' * x + ' + str(self.y_intercept())



def main():
    # open file "geom.txt" for reading
    file = open('geom.txt')
    # read the coordinates of the first Point P
    point_str = file.readline()
    points = point_str.split()
    point_px = float(points[0])
    point_py = float(points[1])
    # read the coordinates of the second Point Q
    point_str = file.readline()
    points = point_str.split()
    point_qx = float(points[0])
    point_qy = float(points[1])
    # print the coordinates of points P and Q
    point_p = Point(point_px, point_py)
    point_q = Point(point_qx, point_qy)
    print('Coordinates of P: ' + point_p.__str__())
    print('Coordinates of Q: ' + point_q.__str__())
    # print distance between P and Q
    print('Distance between P and Q: ' + str(point_p.dist(point_q)))
    # print the slope of the line PQ
    line_pq = Line(point_p.x, point_p.y, point_q.x, point_q.y)
    print('Slope of PQ: ' + str(line_pq.slope()))
    # print the y-intercept of the line PQ
    print('Y-Intercept of PQ:' + str(line_pq.y_intercept()))
    # print the x-intercept of the line PQ
    print('X-Intercept of PQ: ' + str(line_pq.x_intercept()))
    # read the coordinates of the third Point A
    lines = file.readline()
    lines = lines.split()
    point_ax = float(lines[0])
    point_ay = float(lines[1])
    point_a = Point((point_ax), (point_ay))
    # read the coordinates of the fourth Point B
    lines = file.readline()
    lines = lines.split()
    point_bx = float(lines[0])
    point_by = float(lines[1])
    point_b = Point((point_bx), (point_by))
    line_ab = Line(point_ax, point_ay, point_bx, point_by)
    # print the string representation of the line AB
    print('Line AB: ', end='')
    print(line_ab)
    # print if the lines PQ and AB are parallel or not
    if line_pq.is_parallel(line_ab):
        print('PQ is perpendicular to AB')
    else:
        print('PQ is not perpendicular to AB')
    # print if the lines PQ and AB (or extensions) are perpendicular or not
    if line_pq.is_perpendicular(line_ab):
        print('PQ is parallel to AB')
    else:
        print('PQ is not parallel to AB')
# print coordinates of the intersection point of PQ and AB if not parallel
    if line_pq.is_parallel(line_ab):
        pass
    else:
        print('Intersection point of PQ and AB: ' + str(line_pq.intersection_point(line_ab)))
# read the coordinates of the fifth Point G
    lines = file.readline()
    lines = lines.split()
    point_gx = float(lines[0])
    point_gy = float(lines[1])
    point_g = Point((point_gx), (point_gy))
# read the coordinates of the sixth Point H
    lines = file.readline()
    lines = lines.split()
    point_hx = float(lines[0])
    point_hy = float(lines[1])
    point_h = Point((point_hx), (point_hy))
    line_gh = Line(point_gx, point_gy, point_hx, point_hy)
# print if the the points G and H are on the same side of PQ
    print(line_pq.on_same_side(point_g, point_h))
# print if the the points G and H are on the same side of AB
    print(line_ab.on_same_side(point_g, point_h))


# close file "geom.txt"

if __name__ == "__main__":
    main()
