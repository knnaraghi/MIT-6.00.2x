import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    success = 0
    for trial in range(numTrials):
        bucket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
        drawn_ball1 = bucket.pop(random.randrange(8))
        drawn_ball2 = bucket.pop(random.randrange(7))
        drawn_ball3 = bucket.pop(random.randrange(6))
        if drawn_ball1 == drawn_ball2 and drawn_ball2 == drawn_ball3:
            success += 1
    return success / float(numTrials)

#print noReplacementSimulation(10000)
