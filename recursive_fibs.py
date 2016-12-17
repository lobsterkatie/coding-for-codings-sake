def make_fibs(n, fibs=[1, 1]):

    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    if len(fibs) == n:
        print "IN HERE"
        print "final fibs:", fibs
        print "about to return fibs"
        return fibs
    else:
        fibs.append(fibs[-1] + fibs[-2])
        print "about to call make_fibs on", fibs
        make_fibs(n, fibs)
        print "back from make_fibs"
        print "about to return None"


a = make_fibs(5)
print
print "a = ", a
