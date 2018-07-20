# Corey Sokol

def min_max(list):
    # When the length of the list is broken down to only one item,
    # return a tuple and work back up
    if len(list) == 1:
        return list[0], list[0]
    else:
        # Pass list into min_max() and store result in minmax variable
        minmax = min_max(list[1:])
        
        # Sets the initial maximum and minimum values using items in the list
        max = minmax[0]
        min = minmax[1]
        
        # Checks against pre-existing max and min items in list to see
        # if there are values that are larger or smaller and re-assigns them to
        # max and min when necessary.
        return max if minmax[0] > list[0] else list[0], min if minmax[1] < list[0] else list[0]
            
list = [3, 22, 11, 6, 120, 49, 23, 298]

print(min_max(list))
    