#max_to_L = go through and either max before or prev guy
#max_to_R = do the same thing backwards

#underwater:
#   if max to R and L are both strictly higher
#   water level is lesser of R and L maxes

#at water level:
#   sides work separately
#   for each side
#       this happens if max to that side is >= this guy
#       water level is 0

#above water level:
#   if max to both sides is strictly less

#don't care about latter two cases because they don't add to water total



def find_maxes(heights, direction):
    """Given a list of building heights, returns a list either of
       height-of-highest-building-anywhere-to-the-left's or
       height-of-highest-building-anywhere-to-the-right's,
       depending on the given direction parameter.

       O(n) because it requires just one pass through the list."""

    #if we want to work R->L, the easiest thing to do is work L->R on a
    #reversed list, since vanilla for loops work L->R
    if direction == "R":
        heights = heights[::-1] #O(n) if it has to happen

    #create a list to hold the maxes-to-that-point
    #we know the first entry will be zero, because the first building has no
    #buildings to its left
    maxes = [0]

    #loop through the heights, starting with the second, since we've already
    #dealt with the first
    #this is O(n) to make the slice, O(n) to enumerate it, and O(n) to loop
    #over the enumeration (all the stuff actually inside the loop is O(1))
    for prev_index, height in enumerate(heights[1:]):

        #either the building right before this one is higher than the previous
        #highest building (in which case it wins), or the previous max is the
        #max for this one, too
        immediately_prev_height = heights[prev_index]
        max_to_the_L_of_immediately_prev_building = maxes[prev_index]
        new_max = max(max_to_the_L_of_immediately_prev_building,
                      immediately_prev_height)
        maxes.append(new_max)

    #if we were secretly working R->L, we need to reverse the list we've made
    if direction == "R":
        maxes = maxes[::-1]

    return maxes




def get_total_water(heights):
    """Returns the amount of water captured by a skyline consisting of
       buildings of the given heights."""

    #for each building, to determine if it's underwater (and under how much
    #water if so), we need to know the height of the tallest building anywhere
    #to its left, and the tallest building anywhere to its right
    #(computing these is O(n) for each call to find_maxes)
    maxes_to_L = find_maxes(heights, "L")
    maxes_to_R = find_maxes(heights, "R")

    total_water = 0

    #loop through the buildings, determining if each is underwater, and if so,
    #how much water it's under, adding that water to our total
    #(this loop is O(n) since everything inside it is O(1))
    for i, height in enumerate(heights):

        #a building is only underwater if it has a taller building both to its
        #left and its right
        if maxes_to_L[i] > height and maxes_to_R[i] > height:
            #the water level will be the lesser of the heights of the two
            #buildings containing the water
            water_level = min(maxes_to_L[i], maxes_to_R[i])

            #the amount of water above the current building will be the
            #difference between the water level and the building's height
            water_amount = water_level - height

            #add this to our total
            total_water += water_amount

    #now we're done - return the answer!
    return total_water



print get_total_water([]), "(should be 0)"

print get_total_water([0, 0, 0]), "(should be 0)"

print get_total_water([1, 2, 3]), "(should be 0)"

heights1 = [2, 2, 4, 2, 5, 2, 3, 1, 4, 2, 4, 3, 1, 4, 0, 3, 4, 4, 0, 4]
print get_total_water(heights1), "(should be 23)"

heights2 = [4, 2, 5, 2, 1, 5, 3, 5, 3, 0, 0, 2, 1, 2, 3, 4, 4, 1, 3, 4]
print get_total_water(heights2), "(should be 32)"

heights3 = [5, 0, 4, 5, 2, 3, 1, 0, 4, 2, 3, 0, 0, 4, 5, 5, 1, 4, 4, 4]
print get_total_water(heights3), "(should be 40)"

heights4 = [4, 5, 4, 0, 1, 5, 1, 1, 0, 5, 4, 5, 1, 4, 5, 4, 2, 2, 3, 4]
print get_total_water(heights4), "(should be 34)"


