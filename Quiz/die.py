import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    if title != None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()

#makeHistogram([21,20,19,1,2,2,2,5,6,6,9,10], 5, "Aaaaa", "Bbbbb", "Ccccc")
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    longest_runs_each_trial = []
    for i in range(numTrials):
        current_trial =[]
        longest_run = 1
        current_run = 1
        previous = None
        for j in range(numRolls):
            current_trial.append(die.roll())
        for k in current_trial:
            if k == previous:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
                    previous = k
            else:
                current_run = 1
                previous = k
        longest_runs_each_trial.append(longest_run)
    makeHistogram(longest_runs_each_trial, 10, 'Longest Runs', 'Frequency', title=None)
    mean, std = getMeanAndStd(longest_runs_each_trial)
    return mean

#die = Die([1,2,3,4,5,6,6,6,7]) 
#print die.roll()
# One test case
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
