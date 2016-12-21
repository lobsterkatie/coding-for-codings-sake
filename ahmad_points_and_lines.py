
class Line(object):
    """A line in two-space."""

    def __init__(self):
        self.verticality = None
        self.x_int = None
        self.y_int = None
        self.slope = None


    def __repr__(self):
        """Provides helpful output when Line is printed"""

        #if the line is vertical
        if self.verticality:
            return "<Line x = {x_int}>".format(x_int=self.x_int)

        #otherwise
        return "<Line y = {m}x + {b}, x-int: {x_int}>".format(m=self.slope,
                                                           b=self.y_int,
                                                           x_int=self.x_int)

    def includes_point(point):
        """Returns True if given point is on line, False otherwise"""

        x, y = point
        if self.verticality:
            return x == self.x_int
        else:
            return y == self.slope * x + self.y_int
            # should this be y - self.slope * x - self.y_int < .000000001 or
            # something, to account for rounding error of floats?


def find_line_equation(pointA, pointB):
    """Given two points (tuples of x-coord, y-coord), return the slope,
       x- and y-intercepts, and verticality of the line containing them,
       as a Line object."""

    #create a new Line object
    line = Line()

    #unpack the points into coords
    x0, y0 = pointA
    x1, y1 = pointB

    #deal with vertical lines
    if x0 == x1:
        line.verticality = True
        line.x_int = x0
        return line

    #now that we know the line's not vertical...
    line.verticality = False

    #calculate the slope
    line.slope = float(y1 - y0)/(x1 - x0)

    #calculate the x- and y-intercepts
    line.y_int = y0 - line.slope * x0
    line.x_int = -1 * (line.y_int / line.slope)

    #return the line object
    return line

print find_line_equation((0, 4), (1, 7.5))
# print find_line_equation((2, 1), (2, 5))




def find_popular_lines(points):
    """Given a list of points (tuples of x-coord, y-coord), return a list of
       Line objects which include at least three points."""

    point_set = set(points)
    popular_lines = []

    for i, point in enumerate(points):
        base_point = point
        point_set.remove(base_point)
        for second_point in points[i+1:]:
            line = find_line_equation(base_point, second_point)



    # y = mx + b
    # 0 = mx + b
    # -b = mx
    # -b/m = x
