# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    delay_timesteps = [300, 150, 75, 0]
    post_delay_timesteps = 150
    subplot = 0
    
    for timesteps in delay_timesteps:
        population = simulationWithDrug2(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, resistances = {'guttagonol': False} ,
                       mutProb = 0.005, delay_timesteps = timesteps, post_delay_timesteps = post_delay_timesteps, numTrials = numTrials) 
        subplot += 1
        pylab.subplot(2, 2, subplot)
        pylab.hist(population, bins = 12, range = (0, 600))
        pylab.xlabel('Total Virus Count')
        pylab.ylabel('Trials')
        pylab.title('Survived Virus Count for Delay: %s' %timesteps)
        
    pylab.show()



def simulationWithDrug2(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delay_timesteps, post_delay_timesteps, numTrials):
    """
    Runs simulations and plots histogram for problem 1.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    300, 150, 75, and 0 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end a histogram of the virus population size
    (for the total virus population) at the last time point.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    final_total_virus_pop = []
    for trial in range(numTrials):
        viri_instances = []
        for v in range(numViruses):
            viri_instances.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        treated_patient = TreatedPatient(viri_instances, maxPop)
        for x in range(delay_timesteps):
            treated_patient.update()
        treated_patient.addPrescription('guttagonol')
        for x in range(post_delay_timesteps):
            treated_patient.update()    
            
        final_total_virus_pop.append(treated_patient.getTotalPop())

    return final_total_virus_pop

#simulationDelayedTreatment(10)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delay_timesteps = [300, 150, 75, 0]
    pre_delay_timesteps = 150
    post_delay_timesteps = 150
    subplot = 0
    
    for timesteps in delay_timesteps:
        population = simulationWithDrug3(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, resistances = {'guttagonol': False, 'grimpex': False} ,
                       mutProb = 0.005, delay_timesteps = timesteps, pre_delay_timesteps = pre_delay_timesteps, post_delay_timesteps = post_delay_timesteps, numTrials = numTrials) 
        subplot += 1
        pylab.subplot(2, 2, subplot)
        pylab.hist(population, bins = 12 ,range = (0, 600))
        pylab.xlabel('Total Virus Count')
        pylab.ylabel('Trials')
        pylab.title('Survived Virus Count for Delay: %s' %timesteps)
        
    pylab.show()

def simulationWithDrug3(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delay_timesteps, pre_delay_timesteps, post_delay_timesteps, numTrials):
    """
    Runs simulations and plots histogram for problem 2.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    300, 150, 75, and 0 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end a histogram of the virus population size
    (for the total virus population) at the last time point.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    pre_delay_timesteps: number of timesteps before addition of guttagnol
    delay_timestep: number of timesteps with just guttagnol
    post_delay_timesteps; number of timestemps with guttagnol and grimpex
    numTrials: number of simulation runs to execute (an integer)
    
    """
    final_total_virus_pop = []
    for trial in range(numTrials):
        viri_instances = []
        for v in range(numViruses):
            viri_instances.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        treated_patient = TreatedPatient(viri_instances, maxPop)
        for x in range(pre_delay_timesteps):
            treated_patient.update()
        treated_patient.addPrescription('guttagonol')
        for x in range(delay_timesteps):
            treated_patient.update()
        treated_patient.addPrescription('grimpex')
        for x in range(post_delay_timesteps):
            treated_patient.update()    
            
        final_total_virus_pop.append(treated_patient.getTotalPop())

    return final_total_virus_pop

#simulationTwoDrugsDelayedTreatment(50)
