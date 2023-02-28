#######################################################################    Code Organization Notes  #######################################################################
#
# The experiment is split into a series of routines that run sequentially (i.e one by one). Within each routine,
# all the components that need to be shown and all condition assignments that dictate the experiment flow are
# constructed. They only are presented on screen if they are *explicitly* summoned.
#
# The script is organized such that all the components are systematically defined according to the routine they
# belong to in one large section. They are then summoned to be presented on-screen in the next section.

# ##########################################################     Imports     ######################################
from __future__ import division
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import psychopy
import pylink
import os
import platform
import random
import time
import sys
import random
import time
from psychopy import visual, core, event, monitors, gui, hardware, data
from PIL import Image  # for preparing the Host backdrop image
from string import ascii_letters, digits
from psychopy.visual import TextStim
from psychopy.visual import Window
from psychopy.hardware.keyboard import Keyboard
import random, copy
from random import randint
from decimal import *
import csv
from numpy import *
#######################################################################       Experiment  Instruction Texts     #######################################################################

welcome_text = '''
Hello! Thank you for participating in our experiment! 

In this experiment, your task is to read a text and answer some questions about its contents in a memory test later on in Qualtrics. 
As you read, we will record your eye movements with the eye tracker you see just in front of you. 

The researcher will now set you up for experiment. Please let them know if you have any questions and/or concerns.

Press "Space bar" to continue. 
'''

#######################################################################                            Common Components                            ######################################################################
################## Create Data directory ##########################

# store some useful info about this experiment
info = {'participant': '', 'gender': ['m', 'f', 'n/a'], 'consent given': False, 'dateStr': data.getDateStr()}
# present dialog to participant
dlg = gui.DlgFromDict(info, fixed=['dateStr'])
if dlg.OK == False or not info['consent given']:
    core.quit()

filename = "data/%s_%s" % (info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(
    name='MW_Eyelink', version='1.0',  # not needed, just handy
    extraInfo=info,  # the info we created earlier
    dataFileName=filename,  # using our string with data/name_date
)

# Call all the important functions..... INITIALIZE.
win = visual.Window([2560, 1440], fullscr=False, units='pix')

#######################################################################     Define Routines and their components in order     #######################################################################

# 1. Launch/C
##ONE TIME INITIALIZATION START
#setting a bunch of defaults here (we will reset these in every practice or reading loop)
opacityImage1 = 0 #PC image opacity (by default our probe and intentionality images are hidden)
opacityImage2 = 0 #SC image opacity
time1=0 #variables for recording response time data
time2=0
resp1=0 #variables for recording key press data
resp2=0
printNow = 0 #used to trigger data writing to output file
keys = "" #stores keypress values
#these three variables are used to start our timers at the right spot and avoid some edge cases
firstLoop2 = True
firstRoutine2 = True
timerStarted2 = False


#start two clocks
mainTimer2 = core.Clock() # this one just runs for the whole PracticeTrial loop
probeTimer2 = core.Clock() # this one stops and restarts every time one of our probe/intentionality images pops up

myCount = 1 #this counts up and tells which value from the probe list we should use

# import some stuff just in case


event.getKeys() #clear the keyboard buffer just in case they recently pressed a relevant key
##ONE TIME INITIALIZATION END

#Counter for iterating through our probe2 list
myCount2 = 1

event.clearEvents() #clear events just in case they recently pressed a relevant key

# here's a list of the time in seconds between probes
# change this to adjust the probes for the Reading loop
probe2 = [0,91,112,74,98,113,62,92,79,76,62]
# first item in probe, 0, never happens because myCount starts at 1

###################################################################### Condition Assignment ##############################################

# Use the machine time as a seed to generate a random number from (allows for closer to "truly random" numbers)
random.seed(time.process_time())
# set variable myRand to a random number (either 1 or 2); myRandP (EITHER 3 OR 4)
rand = random.randint(1, 2)  # random number for choosing experimental condition order
randP = random.randint(3, 4)  # random number for choosing reading pages order

# set new variable 'currCondition' depending on what random number we generated
if rand == 1:
    # 50% chance of being in the PC condition
    currCondition = "PC"
elif rand == 2:
    # 50% chance of being in the SC condition
    currCondition = "SC"

# CREATE A VARIABLE CALLED currConditionP and set it depending on randP
if randP == 3:
    # 50% chance of being Tropo pages
    currConditionP = "Tropo"
elif randP == 4:
    # 50% chance of being Life pages
    currConditionP = "Life"
###################################################################### File Assignment #####################################################
# 2. setFiles
# SETTING ALL OUR FILE VARIABLES FOR THE EXPERIMENT BASED ON currCondition AND currConditionPs
if currCondition == "PC":
    # if we're in the PC condition then show the PC instructions first run and the SC instructions second run
    InstrFile = "InstrFile/Instr_PC.csv"
    InstrFile2 = "InstrFile/Instr_SC_v2.csv"
    # if we're in the PC condition then show the PC probe message first run and the SC probe message second run
    probeMessage = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."
    probeMessage2 = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
elif currCondition == "SC":
    # if we're in the SC condition then show the SC instructions first run and the PC instructions second run
    InstrFile = "InstrFile/Instr_SC.csv"
    InstrFile2 = "InstrFile/Instr_PC_v2.csv"
    # if we're in the SC condition then show the SC probe message first run and the PC probe message second run
    probeMessage = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
    probeMessage2 = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."

if currConditionP == "Life":
    # if we're in the Life condition then show LifePages first run and TropoPages second run
    stimFile = "LifePages.csv"
    stimFile2 = "TropoPages.csv"
    # if we're in the Life condition then show Life quiz questions first run and Tropo quiz questions second run
    quizFile = "lifeQs.csv"
    quizFile2 = "tropoQs.csv"

elif currConditionP == "Tropo":
    # if we're in the Tropo condition then show TropoPages first run and LifePages second run
    stimFile = "TropoPages.csv"
    stimFile2 = "LifePages.csv"
    # if we're in the Tropo condition then show Tropo quiz questions first run and Life quiz questions second run
    quizFile = "tropoQs.csv"
    quizFile2 = "lifeQs.csv"

############################### Stimuli Initialization ###############################

# Mindwandering instructions based on Condition defined above.
# Build the stim set based on the conditions, build the trial handler and then build the stim presentation function.