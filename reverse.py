# Corey Sokol

def rev_list(list):
    # When the list becomes empty, return the empty list
    if list == []:
        return list
    else:
        # Passes the list to rev_list and breaks it down until empty
        # Empty list returned and then added to each instance of the broken down list
        # Lists are concatenated with first item in the list as the functions work their way back up
        return rev_list(list[1:]) + [list[0]]
        
        # Notes: Failed attempts
            #return rev_list(list[1:] + list[0])
            #list[start], list[stop - 1] = list[stop - 1], list[start]
            #return rev_list(list[1:], start, stop - 1)
        
            #return [''.join(value) for value in rev_list(list[1:])]
            #list[0] = len(list - 1)

            #reverse = rev_list(list[1:])
            #return ''.join(str(reverse)) if len(reverse) >= 1 else reverse
            #return [value for value in list[1:]]
            #return rev_list(list[1:])
    

list = [1, 2, 3, 4, 5]

print(rev_list(list))