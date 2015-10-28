def answer(heights):
    """
    This function searches for places in the hutches that will 
    be filled in by searching for valleys. The first large for loop 
    searches the line of hutches from left to right looking for valleys. 
    The loop iterates over the indicies of the heights list. A valley 
    is identified as starting at index i if the hutches at index i + 1 
    are strictly shorter than those at index i. Then the list heights is 
    looked through starting at index i + 1 and going up. The end of the 
    valley is defined to be the first instance the hutches reach the same 
    height or higher as the hutches as index i (the beginning of the valley).
    Then the valley is filled with the appropriate amount of water. The new 
    heights of the hutches, including the water on top of them are stored 
    in the list y.
    
    The second large for loop then sweeps through the list y of new heights 
    from right to left looking for valleys. The (anti)symmetry of the 
    problem means that valleys missed going from left to right in the 
    first loop will be caught going from right to left. The same process is 
    followed, and the new heights, including water, are stored in y. 
    
    The amount of water that is resting on top of the hutches will be the 
    sum of the list (heights - y) where the subtraction operation is 
    performed coordinatewise.
    """
    
    
    len_heights = len(heights)
    
    y = []
    
    for i in range(0, len_heights):
        y.append(heights[i])
    
    for i in range(0, len_heights - 1):
        if y[i] > y[i + 1]:
            for k in range(i + 1, len_heights):
                if y[i] <= y[k]:
                    next_peak = k
                    fill_height = min(y[i], y[next_peak])
                    y[i] = max(y[i], fill_height)
                    y[next_peak] = max(y[next_peak], fill_height)
                    
                    for l in range(i + 1, next_peak):
                        if y[l] < fill_height:
                            y[l] = fill_height
                            
                    break
 
    for i in range(1, len_heights)[::-1]:
        if y[i] > y[i - 1]:
            for k in range(0, i - 1)[::-1]:
                if y[i] <= y[k]:
                    next_peak = k
                    fill_height = min(y[i], y[next_peak])
                    
                    y[i] = max(y[i], fill_height)
                    y[next_peak] = max(y[next_peak], fill_height)
                    
                    for l in range(next_peak, i + 1):
                        if y[l] < fill_height:
                            y[l] = fill_height
                            
                    break
            
    
    return sum([y[i] - heights[i] for i in range(0, len_heights)])
