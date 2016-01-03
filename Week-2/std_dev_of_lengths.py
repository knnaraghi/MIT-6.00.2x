def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    total = 0.0
    average = 0.0
    if len(L) == 0:
        return float('NaN') 
    for e in L:
        average += float(len(e))
    average = average / len(L)
    for x in L:
        x = float(len(x))
        total += float(x - average)**2
    stddev = (total / float(len(L)))**0.5
    return stddev

#Test Cases    
#L = ['a', 'z', 'p']
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
#L = []
#print stdDevOfLengths(L)
