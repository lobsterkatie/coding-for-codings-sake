# Write a function that takes a list of points in 2D space as an input, and
# returns a list of lines that have more than 2 input points on them. That is:

# You have a list of points [(x0, y0),..., (xK, yK)]

# From the basic geometry, you can always draw a straight line through any pair
# of points. If such line has more than 2 points from the input list on it, it
# needs to be included in the result.

# Test example:

# test_example = [(0., 0.), (1., 1.), (3., 4.), (2., 2.)]

# In this example, the points (0,0), (1,1), and (2,2) are all on the same line.
# Your function should return a list that will contain this line as its only
# element. All other lines you can make from test_example (e.g. (0,0), (3,4))
# will only have two points.


def find_line_eqn(pointA, pointB):
    """Given two pairs of (x,y) coordinates, return a tuple of the form
       (slope, y-int) (for non-vertical lines) or (None, x-int) (for vertical
       lines).

       for example:
       >>> find_line_eqn((0, 0), (2, 6))
       (3.0, 0.0)

       >>> find_line_eqn((1, 2), (5, 8))
       (1.5, 0.5)

       >>> find_line_eqn((-1, 3), (-1, 9))
       (None, -1)

    """

    #unpack the points into coords
    x0, y0 = pointA
    x1, y1 = pointB


    #deal with vertical lines
    if x0 == x1:
        return (None, x0)

    #now that we know the line's not vertical, calculate the slope and y-int
    #and return the results
    slope = float(y1 - y0)/(x1 - x0)
    y_int = y0 - slope * x0
    return (slope, y_int)


def find_popular_lines(points):
    """Given a list of points (tuples of x-coord, y-coord), return a list of
       lines which include at least three points. Lines will be tuples of the
       form (slope, y-int) (for non-vertical lines) or (None, x-int) (for
       vertical lines).

       For example:
       >>> find_popular_lines([(0, 0), (1, 1), (3, 4), (2, 2)])
       [(1.0, 0.0)]

       >>> find_popular_lines([(0, 0), (2, 6), (3, 9), (1, 2), (5, 8), (-1, 3),
       ...                     (-1, 9), (-1, 5)])
       [(None, -1), (3.0, 0.0)]

       Runs in O(n^2) time.

    """

    #create sets to hold all lines described by the points and to hold lines
    #containing at least three points
    all_lines = set()
    popular_lines = set()

    #for each point, find the lines it makes with all subsequent points (since
    #the line through pointA and pointB is the same as the line through pointB
    #and pointA, no need to look backwards in the list)
    for i, pointA in enumerate(points):
        #look at all points after the current pointA
        for pointB in points[i+1:]:
            #find the equation of the line through points A and B
            line = find_line_eqn(pointA, pointB)
            #check if the line is in our set
            #(note that since all_lines is a set, this check is done in
            #constant time)
            if line in all_lines:
                #if it already is, that means we've seen it before, which in
                #turn means that it contains at least three of our points
                popular_lines.add(line)
            #otherwise, it's a new line, so add it to our set
            else:
                all_lines.add(line)

    #return our results set (which is actually a list!), sorted so it's easier
    #to test the function
    return sorted(list(popular_lines))



if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED." % result.attempted
    print
