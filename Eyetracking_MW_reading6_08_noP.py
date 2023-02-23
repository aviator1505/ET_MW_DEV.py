#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 15, 2022, at 16:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'MW_reading2_07'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\BAR Lab\\Documents\\LF_AM_MindWandering_EyeTracking\\MW_reading_6_08_no_practice copy\\Eyetracking_MW_reading6_08_noP.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2048, 1152], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.pupil_labs.pupil_core.EyeTracker'] = {
    'name': 'tracker',
    'runtime_settings': {
        'pupillometry_only': False,
        'surface_name': 'Monitor',
        'gaze_confidence_threshold': 0.6,
        'pupil_remote': {
            'ip_address': '127.0.0.1',
            'port': 50020.0,
            'timeout_ms': 1000.0,
        },
        'pupil_capture_recording': {
            'enabled': True,
            'location': 'C:/Users/BAR Lab/Documents/LF_AM_MindWandering_EyeTracking/MW_reading_6_08_no_practice copy/EyeData',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Launch" ---
# Run 'Begin Experiment' code from code
#import what we need to generate a random number
import random, xlrd
import time

#Use the machine time as a seed to generate a random number from (allows for closer to "truly random" numbers)
random.seed(time.process_time())
#set variable myRand to a random number (either 1 or 2); myRandP (EITHER 3 OR 4)
rand = random.randint(1,2) #random number for choosing experimental condition order
randP = random.randint(3,4) #random number for choosing reading pages order

#set new variable 'currCondition' depending on what random number we generated
if rand == 1:
    #50% chance of being in the PC condition
    currCondition = "PC"
elif rand == 2:
    #50% chance of being in the SC condition
    currCondition = "SC"
 
#CREATE A VARIABLE CALLED currConditionP and set it depending on randP
if randP == 3:
    #50% chance of being Tropo pages
    currConditionP = "Tropo"
elif randP == 4:
    #50% chance of being Life pages
    currConditionP = "Life"

#For testing purposes we can set our condition and pages here. 
#Just comment out the two lines below to run the experiment randomly.
currCondition = "SC"
#currConditionP = "Tropo"



# --- Initialize components for Routine "Welcome" ---
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='Welcome to the experiment!\n\nBefore we begin, please complete the following multiple choice questions by using the number keys to enter your answers.\n\n\n(Press the spacebar to continue)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Welcome_text_resp = keyboard.Keyboard()

# --- Initialize components for Routine "DemographicQs" ---
DemoQs = visual.ImageStim(
    win=win,
    name='DemoQs', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
DemographicQs_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AgeQuestion" ---
AgeQuestion_textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.15),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='AgeQuestion_textbox',
     autoLog=True,
)
text_4 = visual.TextStim(win=win, name='text_4',
    text="Using the number keys please enter your age. Then press 'space' to continue.",
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Age_resp = keyboard.Keyboard()

# --- Initialize components for Routine "AQintro" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='Please answer the following questions.\n\n\n\n(Press the spacebar to continue.)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
AQintro_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "AQ_10_Qs" ---
AQ_10 = visual.ImageStim(
    win=win,
    name='AQ_10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
AQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "adhdQ1_2" ---
adhdQ = visual.TextStim(win=win, name='adhdQ',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Qanswer = visual.TextStim(win=win, name='Qanswer',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_QA = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AlwaysQ" ---
AlwaysQText = visual.TextStim(win=win, name='AlwaysQText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
AlwaysAnswer = visual.TextStim(win=win, name='AlwaysAnswer',
    text='1. Yes\n2. No',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_AlwaysResp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "adhdDx" ---
adhdDxQ = visual.TextStim(win=win, name='adhdDxQ',
    text='Have you ever been given an official diagnosis of attention-deficit / hyperactivity disorder (ADHD) (e.g., by a registered psychologist, psychiatrist, counsellor, etc.)?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Dx_answer = visual.TextStim(win=win, name='Dx_answer',
    text='1. Yes\n2. No\n3. No, but I strongly suspect I might have ADHD',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_Dx = keyboard.Keyboard()

# --- Initialize components for Routine "setFiles" ---
# Run 'Begin Experiment' code from code_8
#SETTING ALL OUR FILE VARIABLES FOR THE EXPERIMENT BASED ON currCondition AND currConditionPs
if currCondition == "PC":
    #if we're in the PC condition then show the PC instructions first run and the SC instructions second run
    InstrFile = "InstrFile/Instr_PC.csv"
    InstrFile2 = "InstrFile/Instr_SC_v2.csv"
    #if we're in the PC condition then show the PC probe message first run and the SC probe message second run
    probeMessage = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."
    probeMessage2 = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
elif currCondition == "SC":
    #if we're in the SC condition then show the SC instructions first run and the PC instructions second run
    InstrFile = "InstrFile/Instr_SC.csv"
    InstrFile2 = "InstrFile/Instr_PC_v2.csv"
    #if we're in the SC condition then show the SC probe message first run and the PC probe message second run
    probeMessage = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
    probeMessage2 = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."
 
if currConditionP == "Life":
    #if we're in the Life condition then show LifePages first run and TropoPages second run
    stimFile = "LifePages.csv"
    stimFile2 = "TropoPages.csv"
    #if we're in the Life condition then show Life quiz questions first run and Tropo quiz questions second run
    quizFile = "lifeQs.csv"
    quizFile2 = "tropoQs.csv"
    
elif currConditionP == "Tropo":
    #if we're in the Tropo condition then show TropoPages first run and LifePages second run
    stimFile = "TropoPages.csv"
    stimFile2 = "LifePages.csv"
    #if we're in the Tropo condition then show Tropo quiz questions first run and Life quiz questions second run
    quizFile = "tropoQs.csv"
    quizFile2 = "lifeQs.csv"

#All the above variables will be used in later components as such:
#InstrFile used in MWdefinitions loop as the csv file to pull instruction images from
#InstrFile2 used in MWdefinitions2 loop as the csv file to pull instruction images from
#probeMessage used in IntroExp as display text
#probeMessage2 used in IntroExp2 as display text
#stimFile used in ReadingLoop as the csv file to pull reading page images from
#stimFile2 used in ReadingLoop2 as the csv file to pull reading page images from
#quizFile used in QuizLoop as the csv file to pull quiz question images from
#quizFile2 used in QuizLoop2 as the csv file to pull quiz question images from


# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "MW_def" ---
MWdefInstr = visual.ImageStim(
    win=win,
    name='MWdefInstr', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
MWdefInstr_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "IntroExp" ---
text = visual.TextStim(win=win, name='text',
    text=probeMessage,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
IntroExp_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "PageSkipping" ---
NoSkipping = visual.TextStim(win=win, name='NoSkipping',
    text='Please read at your normal pace and do not skip pages.\n\n\n(press spacebar to continue)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_Skip = keyboard.Keyboard()

# --- Initialize components for Routine "EYE_RECORD_START" ---
etRecord_START = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)

# --- Initialize components for Routine "Reading" ---
# Run 'Begin Experiment' code from code_3
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
import random, copy
from random import randint
from decimal import *
import csv
from numpy import *
from psychopy import core, event
event.getKeys() #clear the keyboard buffer just in case they recently pressed a relevant key
##ONE TIME INITIALIZATION END

#Counter for iterating through our probe2 list
myCount2 = 1

event.clearEvents() #clear events just in case they recently pressed a relevant key

# here's a list of the time in seconds between probes
# change this to adjust the probes for the Reading loop
probe2 = [0,91,112,74,98,113,62,92,79,76,62]
# first item in probe, 0, never happens because myCount starts at 1
Reading_key_resp = keyboard.Keyboard()
imagePages = visual.ImageStim(
    win=win,
    name='imagePages', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PCProbe = visual.ImageStim(
    win=win,
    name='PCProbe', 
    image='images/PC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
SCProbe = visual.ImageStim(
    win=win,
    name='SCProbe', 
    image='images/SC_v2.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "EYE_RECORD_STOP" ---
EYE_Record_STOP = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Quiz" ---
QuizQuestion = visual.ImageStim(
    win=win,
    name='QuizQuestion', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Quiz_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "InterestingQ" ---
interestingImage = visual.ImageStim(
    win=win,
    name='interestingImage', 
    image='QuizQs/Likert_interest.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
InterestingQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "DifficultyQ" ---
difficultyImage = visual.ImageStim(
    win=win,
    name='difficultyImage', 
    image='QuizQs/Likert_difficulty.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
DifficultyQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Likert_Mot" ---
MW_mot = visual.ImageStim(
    win=win,
    name='MW_mot', 
    image='QuizQs/Likert_motivation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
MW_motQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "unIntMWcapture" ---
MWunint = visual.ImageStim(
    win=win,
    name='MWunint', 
    image='QuizQs/Likert_unintMW.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
unintMWkey_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "intMWcaptureQ" ---
MWcaptureImage = visual.ImageStim(
    win=win,
    name='MWcaptureImage', 
    image='QuizQs/Likert_intMW.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intMWcaptureQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Halfway" ---
HalfwayText = visual.TextStim(win=win, name='HalfwayText',
    text='Thank you for completing the first half of the experiment.\n\nBefore beginning the second half, please let the research assistant know if you have any questions or if you need a short break.\n\n(Press the spacebar to continue)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
HalfwayResp = keyboard.Keyboard()

# --- Initialize components for Routine "MW_def2" ---
MWdef_image = visual.ImageStim(
    win=win,
    name='MWdef_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
MW_def2_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "IntroExp2" ---
probe_message = visual.TextStim(win=win, name='probe_message',
    text=probeMessage2,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IntroExp2_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "EYE_RECORD_START" ---
etRecord_START = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)

# --- Initialize components for Routine "Reading2" ---
Reading2_key_resp = keyboard.Keyboard()
imagePages2 = visual.ImageStim(
    win=win,
    name='imagePages2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PCProbe2 = visual.ImageStim(
    win=win,
    name='PCProbe2', 
    image='images/PC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
SCProbe2 = visual.ImageStim(
    win=win,
    name='SCProbe2', 
    image='images/SC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
# Run 'Begin Experiment' code from code_2
#use new true/false variables so that the values from our Practice loop don't affect the functionality of the Reading loop
firstLoop4 = True
firstRoutine4 = True
timerStarted4 = False

#start two new clocks so the values of the previous clocks don't affect this loop
mainTimer4 = core.Clock()
probeTimer4 = core.Clock()

#create a new counter so the value of our old counter doesn't carry over to this loop
myCount4 = 1

event.clearEvents()

# here's a list of the time in seconds between probes
# change this to adjust the probes for the Quiz2 loop
probe4 = [0,91,112,74,98,113,62,92,79,76,62]
# first item in probe, 0, never happens because myCount starts at 1

# --- Initialize components for Routine "EYE_RECORD_STOP" ---
EYE_Record_STOP = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Quiz2" ---
QuizQuestion2 = visual.ImageStim(
    win=win,
    name='QuizQuestion2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Quiz2_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "InterestingQ" ---
interestingImage = visual.ImageStim(
    win=win,
    name='interestingImage', 
    image='QuizQs/Likert_interest.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
InterestingQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "DifficultyQ" ---
difficultyImage = visual.ImageStim(
    win=win,
    name='difficultyImage', 
    image='QuizQs/Likert_difficulty.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
DifficultyQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Likert_Mot" ---
MW_mot = visual.ImageStim(
    win=win,
    name='MW_mot', 
    image='QuizQs/Likert_motivation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
MW_motQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "unIntMWcapture" ---
MWunint = visual.ImageStim(
    win=win,
    name='MWunint', 
    image='QuizQs/Likert_unintMW.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.0, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
unintMWkey_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "intMWcaptureQ" ---
MWcaptureImage = visual.ImageStim(
    win=win,
    name='MWcaptureImage', 
    image='QuizQs/Likert_intMW.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intMWcaptureQ_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
textInterval = visual.TextStim(win=win, name='textInterval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EndText" ---
EndExpText = visual.TextStim(win=win, name='EndExpText',
    text="Thank you for participating in this experiment!\n\nPlease let the research assistant know if you would like to be debriefed.\n\nThank you!\n\n(Press 'space' to continue)",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='hsv', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='hsv',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='FIVE_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Launch" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
LaunchComponents = []
for thisComponent in LaunchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Launch" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LaunchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Launch" ---
for thisComponent in LaunchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Launch" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Welcome_text_resp.keys = []
Welcome_text_resp.rt = []
_Welcome_text_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Welcome_text, Welcome_text_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome_text.started')
        Welcome_text.setAutoDraw(True)
    
    # *Welcome_text_resp* updates
    waitOnFlip = False
    if Welcome_text_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text_resp.frameNStart = frameN  # exact frame index
        Welcome_text_resp.tStart = t  # local t and not account for scr refresh
        Welcome_text_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome_text_resp.started')
        Welcome_text_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome_text_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome_text_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome_text_resp.status == STARTED and not waitOnFlip:
        theseKeys = Welcome_text_resp.getKeys(keyList=['space'], waitRelease=False)
        _Welcome_text_resp_allKeys.extend(theseKeys)
        if len(_Welcome_text_resp_allKeys):
            Welcome_text_resp.keys = _Welcome_text_resp_allKeys[-1].name  # just the last key pressed
            Welcome_text_resp.rt = _Welcome_text_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Welcome_text_resp.keys in ['', [], None]:  # No response was made
    Welcome_text_resp.keys = None
thisExp.addData('Welcome_text_resp.keys',Welcome_text_resp.keys)
if Welcome_text_resp.keys != None:  # we had a response
    thisExp.addData('Welcome_text_resp.rt', Welcome_text_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Demographic_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseDemoQs.csv'),
    seed=None, name='Demographic_Loop')
thisExp.addLoop(Demographic_Loop)  # add the loop to the experiment
thisDemographic_Loop = Demographic_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemographic_Loop.rgb)
if thisDemographic_Loop != None:
    for paramName in thisDemographic_Loop:
        exec('{} = thisDemographic_Loop[paramName]'.format(paramName))

for thisDemographic_Loop in Demographic_Loop:
    currentLoop = Demographic_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisDemographic_Loop.rgb)
    if thisDemographic_Loop != None:
        for paramName in thisDemographic_Loop:
            exec('{} = thisDemographic_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "DemographicQs" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    DemoQs.setImage(chDemoQs)
    DemographicQs_resp.keys = []
    DemographicQs_resp.rt = []
    _DemographicQs_resp_allKeys = []
    # keep track of which components have finished
    DemographicQsComponents = [DemoQs, DemographicQs_resp]
    for thisComponent in DemographicQsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "DemographicQs" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DemoQs* updates
        if DemoQs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DemoQs.frameNStart = frameN  # exact frame index
            DemoQs.tStart = t  # local t and not account for scr refresh
            DemoQs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DemoQs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DemoQs.started')
            DemoQs.setAutoDraw(True)
        
        # *DemographicQs_resp* updates
        waitOnFlip = False
        if DemographicQs_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DemographicQs_resp.frameNStart = frameN  # exact frame index
            DemographicQs_resp.tStart = t  # local t and not account for scr refresh
            DemographicQs_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DemographicQs_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DemographicQs_resp.started')
            DemographicQs_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(DemographicQs_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(DemographicQs_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if DemographicQs_resp.status == STARTED and not waitOnFlip:
            theseKeys = DemographicQs_resp.getKeys(keyList=['1','2','3','4','5','6','7',], waitRelease=False)
            _DemographicQs_resp_allKeys.extend(theseKeys)
            if len(_DemographicQs_resp_allKeys):
                DemographicQs_resp.keys = _DemographicQs_resp_allKeys[-1].name  # just the last key pressed
                DemographicQs_resp.rt = _DemographicQs_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DemographicQsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DemographicQs" ---
    for thisComponent in DemographicQsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if DemographicQs_resp.keys in ['', [], None]:  # No response was made
        DemographicQs_resp.keys = None
    Demographic_Loop.addData('DemographicQs_resp.keys',DemographicQs_resp.keys)
    if DemographicQs_resp.keys != None:  # we had a response
        Demographic_Loop.addData('DemographicQs_resp.rt', DemographicQs_resp.rt)
    # the Routine "DemographicQs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Demographic_Loop'


# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "AgeQuestion" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
AgeQuestion_textbox.reset()
Age_resp.keys = []
Age_resp.rt = []
_Age_resp_allKeys = []
# keep track of which components have finished
AgeQuestionComponents = [AgeQuestion_textbox, text_4, Age_resp]
for thisComponent in AgeQuestionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "AgeQuestion" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *AgeQuestion_textbox* updates
    if AgeQuestion_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AgeQuestion_textbox.frameNStart = frameN  # exact frame index
        AgeQuestion_textbox.tStart = t  # local t and not account for scr refresh
        AgeQuestion_textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AgeQuestion_textbox, 'tStartRefresh')  # time at next scr refresh
        AgeQuestion_textbox.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    
    # *Age_resp* updates
    waitOnFlip = False
    if Age_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Age_resp.frameNStart = frameN  # exact frame index
        Age_resp.tStart = t  # local t and not account for scr refresh
        Age_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Age_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Age_resp.started')
        Age_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Age_resp.clock.reset)  # t=0 on next screen flip
    if Age_resp.status == STARTED and not waitOnFlip:
        theseKeys = Age_resp.getKeys(keyList=['space'], waitRelease=False)
        _Age_resp_allKeys.extend(theseKeys)
        if len(_Age_resp_allKeys):
            Age_resp.keys = [key.name for key in _Age_resp_allKeys]  # storing all keys
            Age_resp.rt = [key.rt for key in _Age_resp_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AgeQuestionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "AgeQuestion" ---
for thisComponent in AgeQuestionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('AgeQuestion_textbox.text',AgeQuestion_textbox.text)
# check responses
if Age_resp.keys in ['', [], None]:  # No response was made
    Age_resp.keys = None
thisExp.addData('Age_resp.keys',Age_resp.keys)
if Age_resp.keys != None:  # we had a response
    thisExp.addData('Age_resp.rt', Age_resp.rt)
thisExp.nextEntry()
# the Routine "AgeQuestion" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "AQintro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
AQintro_key_resp.keys = []
AQintro_key_resp.rt = []
_AQintro_key_resp_allKeys = []
# keep track of which components have finished
AQintroComponents = [text_3, AQintro_key_resp]
for thisComponent in AQintroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "AQintro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    
    # *AQintro_key_resp* updates
    waitOnFlip = False
    if AQintro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AQintro_key_resp.frameNStart = frameN  # exact frame index
        AQintro_key_resp.tStart = t  # local t and not account for scr refresh
        AQintro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AQintro_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'AQintro_key_resp.started')
        AQintro_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(AQintro_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(AQintro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if AQintro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = AQintro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _AQintro_key_resp_allKeys.extend(theseKeys)
        if len(_AQintro_key_resp_allKeys):
            AQintro_key_resp.keys = _AQintro_key_resp_allKeys[-1].name  # just the last key pressed
            AQintro_key_resp.rt = _AQintro_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AQintroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "AQintro" ---
for thisComponent in AQintroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if AQintro_key_resp.keys in ['', [], None]:  # No response was made
    AQintro_key_resp.keys = None
thisExp.addData('AQintro_key_resp.keys',AQintro_key_resp.keys)
if AQintro_key_resp.keys != None:  # we had a response
    thisExp.addData('AQintro_key_resp.rt', AQintro_key_resp.rt)
thisExp.nextEntry()
# the Routine "AQintro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AQ_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseAQ10.csv'),
    seed=None, name='AQ_Loop')
thisExp.addLoop(AQ_Loop)  # add the loop to the experiment
thisAQ_Loop = AQ_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAQ_Loop.rgb)
if thisAQ_Loop != None:
    for paramName in thisAQ_Loop:
        exec('{} = thisAQ_Loop[paramName]'.format(paramName))

for thisAQ_Loop in AQ_Loop:
    currentLoop = AQ_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisAQ_Loop.rgb)
    if thisAQ_Loop != None:
        for paramName in thisAQ_Loop:
            exec('{} = thisAQ_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "AQ_10_Qs" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    AQ_10.setImage(chAQ10)
    AQ_key_resp.keys = []
    AQ_key_resp.rt = []
    _AQ_key_resp_allKeys = []
    # keep track of which components have finished
    AQ_10_QsComponents = [AQ_10, AQ_key_resp]
    for thisComponent in AQ_10_QsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AQ_10_Qs" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AQ_10* updates
        if AQ_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AQ_10.frameNStart = frameN  # exact frame index
            AQ_10.tStart = t  # local t and not account for scr refresh
            AQ_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AQ_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AQ_10.started')
            AQ_10.setAutoDraw(True)
        
        # *AQ_key_resp* updates
        waitOnFlip = False
        if AQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AQ_key_resp.frameNStart = frameN  # exact frame index
            AQ_key_resp.tStart = t  # local t and not account for scr refresh
            AQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AQ_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AQ_key_resp.started')
            AQ_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AQ_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AQ_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = AQ_key_resp.getKeys(keyList=['1','2','3','4',], waitRelease=False)
            _AQ_key_resp_allKeys.extend(theseKeys)
            if len(_AQ_key_resp_allKeys):
                AQ_key_resp.keys = _AQ_key_resp_allKeys[-1].name  # just the last key pressed
                AQ_key_resp.rt = _AQ_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AQ_10_QsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AQ_10_Qs" ---
    for thisComponent in AQ_10_QsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if AQ_key_resp.keys in ['', [], None]:  # No response was made
        AQ_key_resp.keys = None
    AQ_Loop.addData('AQ_key_resp.keys',AQ_key_resp.keys)
    if AQ_key_resp.keys != None:  # we had a response
        AQ_Loop.addData('AQ_key_resp.rt', AQ_key_resp.rt)
    # the Routine "AQ_10_Qs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [text_2]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'AQ_Loop'


# set up handler to look after randomisation of conditions etc
Q_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('adhd3Qs.xlsx'),
    seed=None, name='Q_trials')
thisExp.addLoop(Q_trials)  # add the loop to the experiment
thisQ_trial = Q_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQ_trial.rgb)
if thisQ_trial != None:
    for paramName in thisQ_trial:
        exec('{} = thisQ_trial[paramName]'.format(paramName))

for thisQ_trial in Q_trials:
    currentLoop = Q_trials
    # abbreviate parameter names if possible (e.g. rgb = thisQ_trial.rgb)
    if thisQ_trial != None:
        for paramName in thisQ_trial:
            exec('{} = thisQ_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "adhdQ1_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    adhdQ.setText(Q_stim)
    Qanswer.setText('1. Yes\n2. No')
    key_QA.keys = []
    key_QA.rt = []
    _key_QA_allKeys = []
    # keep track of which components have finished
    adhdQ1_2Components = [adhdQ, Qanswer, key_QA]
    for thisComponent in adhdQ1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "adhdQ1_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *adhdQ* updates
        if adhdQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            adhdQ.frameNStart = frameN  # exact frame index
            adhdQ.tStart = t  # local t and not account for scr refresh
            adhdQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(adhdQ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'adhdQ.started')
            adhdQ.setAutoDraw(True)
        
        # *Qanswer* updates
        if Qanswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Qanswer.frameNStart = frameN  # exact frame index
            Qanswer.tStart = t  # local t and not account for scr refresh
            Qanswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Qanswer, 'tStartRefresh')  # time at next scr refresh
            Qanswer.setAutoDraw(True)
        
        # *key_QA* updates
        waitOnFlip = False
        if key_QA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_QA.frameNStart = frameN  # exact frame index
            key_QA.tStart = t  # local t and not account for scr refresh
            key_QA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_QA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_QA.started')
            key_QA.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_QA.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_QA.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_QA.status == STARTED and not waitOnFlip:
            theseKeys = key_QA.getKeys(keyList=['1', '2',], waitRelease=False)
            _key_QA_allKeys.extend(theseKeys)
            if len(_key_QA_allKeys):
                key_QA.keys = _key_QA_allKeys[-1].name  # just the last key pressed
                key_QA.rt = _key_QA_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in adhdQ1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "adhdQ1_2" ---
    for thisComponent in adhdQ1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_QA.keys in ['', [], None]:  # No response was made
        key_QA.keys = None
    Q_trials.addData('key_QA.keys',key_QA.keys)
    if key_QA.keys != None:  # we had a response
        Q_trials.addData('key_QA.rt', key_QA.rt)
    # the Routine "adhdQ1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [text_2]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "AlwaysQ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    if(key_QA.keys == '1'):
        continueRoutine = True
    else:
        continueRoutine = False
    AlwaysQText.setText('Have you always been like this? (as long as you can remember, or for most of your life)')
    key_AlwaysResp.keys = []
    key_AlwaysResp.rt = []
    _key_AlwaysResp_allKeys = []
    # keep track of which components have finished
    AlwaysQComponents = [AlwaysQText, AlwaysAnswer, key_AlwaysResp]
    for thisComponent in AlwaysQComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AlwaysQ" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AlwaysQText* updates
        if AlwaysQText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AlwaysQText.frameNStart = frameN  # exact frame index
            AlwaysQText.tStart = t  # local t and not account for scr refresh
            AlwaysQText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AlwaysQText, 'tStartRefresh')  # time at next scr refresh
            AlwaysQText.setAutoDraw(True)
        
        # *AlwaysAnswer* updates
        if AlwaysAnswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AlwaysAnswer.frameNStart = frameN  # exact frame index
            AlwaysAnswer.tStart = t  # local t and not account for scr refresh
            AlwaysAnswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AlwaysAnswer, 'tStartRefresh')  # time at next scr refresh
            AlwaysAnswer.setAutoDraw(True)
        
        # *key_AlwaysResp* updates
        waitOnFlip = False
        if key_AlwaysResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_AlwaysResp.frameNStart = frameN  # exact frame index
            key_AlwaysResp.tStart = t  # local t and not account for scr refresh
            key_AlwaysResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_AlwaysResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_AlwaysResp.started')
            key_AlwaysResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_AlwaysResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_AlwaysResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_AlwaysResp.status == STARTED and not waitOnFlip:
            theseKeys = key_AlwaysResp.getKeys(keyList=['1','2'], waitRelease=False)
            _key_AlwaysResp_allKeys.extend(theseKeys)
            if len(_key_AlwaysResp_allKeys):
                key_AlwaysResp.keys = _key_AlwaysResp_allKeys[-1].name  # just the last key pressed
                key_AlwaysResp.rt = _key_AlwaysResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AlwaysQComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AlwaysQ" ---
    for thisComponent in AlwaysQComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_AlwaysResp.keys in ['', [], None]:  # No response was made
        key_AlwaysResp.keys = None
    Q_trials.addData('key_AlwaysResp.keys',key_AlwaysResp.keys)
    if key_AlwaysResp.keys != None:  # we had a response
        Q_trials.addData('key_AlwaysResp.rt', key_AlwaysResp.rt)
    # the Routine "AlwaysQ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [text_2]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Q_trials'


# --- Prepare to start Routine "adhdDx" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_Dx.keys = []
key_Dx.rt = []
_key_Dx_allKeys = []
# keep track of which components have finished
adhdDxComponents = [adhdDxQ, Dx_answer, key_Dx]
for thisComponent in adhdDxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "adhdDx" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *adhdDxQ* updates
    if adhdDxQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        adhdDxQ.frameNStart = frameN  # exact frame index
        adhdDxQ.tStart = t  # local t and not account for scr refresh
        adhdDxQ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(adhdDxQ, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'adhdDxQ.started')
        adhdDxQ.setAutoDraw(True)
    
    # *Dx_answer* updates
    if Dx_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Dx_answer.frameNStart = frameN  # exact frame index
        Dx_answer.tStart = t  # local t and not account for scr refresh
        Dx_answer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Dx_answer, 'tStartRefresh')  # time at next scr refresh
        Dx_answer.setAutoDraw(True)
    
    # *key_Dx* updates
    waitOnFlip = False
    if key_Dx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Dx.frameNStart = frameN  # exact frame index
        key_Dx.tStart = t  # local t and not account for scr refresh
        key_Dx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Dx, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_Dx.started')
        key_Dx.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Dx.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Dx.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Dx.status == STARTED and not waitOnFlip:
        theseKeys = key_Dx.getKeys(keyList=['1','2','3'], waitRelease=False)
        _key_Dx_allKeys.extend(theseKeys)
        if len(_key_Dx_allKeys):
            key_Dx.keys = _key_Dx_allKeys[-1].name  # just the last key pressed
            key_Dx.rt = _key_Dx_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in adhdDxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "adhdDx" ---
for thisComponent in adhdDxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_Dx.keys in ['', [], None]:  # No response was made
    key_Dx.keys = None
thisExp.addData('key_Dx.keys',key_Dx.keys)
if key_Dx.keys != None:  # we had a response
    thisExp.addData('key_Dx.rt', key_Dx.rt)
thisExp.nextEntry()
# the Routine "adhdDx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setFiles" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setFilesComponents = []
for thisComponent in setFilesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setFiles" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setFilesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setFiles" ---
for thisComponent in setFilesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setFiles" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
MWdefinitions = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(InstrFile),
    seed=None, name='MWdefinitions')
thisExp.addLoop(MWdefinitions)  # add the loop to the experiment
thisMWdefinition = MWdefinitions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMWdefinition.rgb)
if thisMWdefinition != None:
    for paramName in thisMWdefinition:
        exec('{} = thisMWdefinition[paramName]'.format(paramName))

for thisMWdefinition in MWdefinitions:
    currentLoop = MWdefinitions
    # abbreviate parameter names if possible (e.g. rgb = thisMWdefinition.rgb)
    if thisMWdefinition != None:
        for paramName in thisMWdefinition:
            exec('{} = thisMWdefinition[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MW_def" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    MWdefInstr.setImage(chInstrSlide)
    MWdefInstr_key_resp.keys = []
    MWdefInstr_key_resp.rt = []
    _MWdefInstr_key_resp_allKeys = []
    # keep track of which components have finished
    MW_defComponents = [MWdefInstr, MWdefInstr_key_resp]
    for thisComponent in MW_defComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "MW_def" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MWdefInstr* updates
        if MWdefInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MWdefInstr.frameNStart = frameN  # exact frame index
            MWdefInstr.tStart = t  # local t and not account for scr refresh
            MWdefInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MWdefInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MWdefInstr.started')
            MWdefInstr.setAutoDraw(True)
        
        # *MWdefInstr_key_resp* updates
        if MWdefInstr_key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MWdefInstr_key_resp.frameNStart = frameN  # exact frame index
            MWdefInstr_key_resp.tStart = t  # local t and not account for scr refresh
            MWdefInstr_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MWdefInstr_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('MWdefInstr_key_resp.started', t)
            MWdefInstr_key_resp.status = STARTED
            # keyboard checking is just starting
            MWdefInstr_key_resp.clock.reset()  # now t=0
        if MWdefInstr_key_resp.status == STARTED:
            theseKeys = MWdefInstr_key_resp.getKeys(keyList=['space',], waitRelease=False)
            _MWdefInstr_key_resp_allKeys.extend(theseKeys)
            if len(_MWdefInstr_key_resp_allKeys):
                MWdefInstr_key_resp.keys = _MWdefInstr_key_resp_allKeys[-1].name  # just the last key pressed
                MWdefInstr_key_resp.rt = _MWdefInstr_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MW_defComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MW_def" ---
    for thisComponent in MW_defComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MW_def" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'MWdefinitions'


# --- Prepare to start Routine "IntroExp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IntroExp_key_resp.keys = []
IntroExp_key_resp.rt = []
_IntroExp_key_resp_allKeys = []
# keep track of which components have finished
IntroExpComponents = [text, IntroExp_key_resp]
for thisComponent in IntroExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IntroExp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *IntroExp_key_resp* updates
    waitOnFlip = False
    if IntroExp_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroExp_key_resp.frameNStart = frameN  # exact frame index
        IntroExp_key_resp.tStart = t  # local t and not account for scr refresh
        IntroExp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroExp_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IntroExp_key_resp.started')
        IntroExp_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IntroExp_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IntroExp_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IntroExp_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = IntroExp_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _IntroExp_key_resp_allKeys.extend(theseKeys)
        if len(_IntroExp_key_resp_allKeys):
            IntroExp_key_resp.keys = _IntroExp_key_resp_allKeys[-1].name  # just the last key pressed
            IntroExp_key_resp.rt = _IntroExp_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IntroExp" ---
for thisComponent in IntroExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IntroExp_key_resp.keys in ['', [], None]:  # No response was made
    IntroExp_key_resp.keys = None
thisExp.addData('IntroExp_key_resp.keys',IntroExp_key_resp.keys)
if IntroExp_key_resp.keys != None:  # we had a response
    thisExp.addData('IntroExp_key_resp.rt', IntroExp_key_resp.rt)
thisExp.nextEntry()
# the Routine "IntroExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PageSkipping" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_Skip.keys = []
key_Skip.rt = []
_key_Skip_allKeys = []
# keep track of which components have finished
PageSkippingComponents = [NoSkipping, key_Skip]
for thisComponent in PageSkippingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PageSkipping" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NoSkipping* updates
    if NoSkipping.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NoSkipping.frameNStart = frameN  # exact frame index
        NoSkipping.tStart = t  # local t and not account for scr refresh
        NoSkipping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NoSkipping, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'NoSkipping.started')
        NoSkipping.setAutoDraw(True)
    
    # *key_Skip* updates
    waitOnFlip = False
    if key_Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Skip.frameNStart = frameN  # exact frame index
        key_Skip.tStart = t  # local t and not account for scr refresh
        key_Skip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Skip, 'tStartRefresh')  # time at next scr refresh
        key_Skip.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Skip.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Skip.status == STARTED and not waitOnFlip:
        theseKeys = key_Skip.getKeys(keyList=['space'], waitRelease=False)
        _key_Skip_allKeys.extend(theseKeys)
        if len(_key_Skip_allKeys):
            key_Skip.keys = _key_Skip_allKeys[-1].name  # just the last key pressed
            key_Skip.rt = _key_Skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PageSkippingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PageSkipping" ---
for thisComponent in PageSkippingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_Skip.keys in ['', [], None]:  # No response was made
    key_Skip.keys = None
thisExp.addData('key_Skip.keys',key_Skip.keys)
if key_Skip.keys != None:  # we had a response
    thisExp.addData('key_Skip.rt', key_Skip.rt)
thisExp.nextEntry()
# the Routine "PageSkipping" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EYE_RECORD_START" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EYE_RECORD_STARTComponents = [etRecord_START]
for thisComponent in EYE_RECORD_STARTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EYE_RECORD_START" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *etRecord_START* updates
    if etRecord_START.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        etRecord_START.frameNStart = frameN  # exact frame index
        etRecord_START.tStart = t  # local t and not account for scr refresh
        etRecord_START.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etRecord_START, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('etRecord_START.started', t)
        etRecord_START.status = STARTED
    if etRecord_START.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord_START.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord_START.tStop = t  # not accounting for scr refresh
            etRecord_START.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord_START.stopped', t)
            etRecord_START.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EYE_RECORD_STARTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EYE_RECORD_START" ---
for thisComponent in EYE_RECORD_STARTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord_START.status != FINISHED:
    etRecord_START.status = FINISHED
# the Routine "EYE_RECORD_START" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ReadingLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(stimFile),
    seed=None, name='ReadingLoop')
thisExp.addLoop(ReadingLoop)  # add the loop to the experiment
thisReadingLoop = ReadingLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReadingLoop.rgb)
if thisReadingLoop != None:
    for paramName in thisReadingLoop:
        exec('{} = thisReadingLoop[paramName]'.format(paramName))

for thisReadingLoop in ReadingLoop:
    currentLoop = ReadingLoop
    # abbreviate parameter names if possible (e.g. rgb = thisReadingLoop.rgb)
    if thisReadingLoop != None:
        for paramName in thisReadingLoop:
            exec('{} = thisReadingLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Reading" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    #Reset a bunch of our defaults at the start of this loop. We only do this once.
    #This stops the values from our previous practice loop from affecting this reading loop.
    if firstRoutine2:
        firstRoutine2 = False
        mainTimer2.reset(0)
        probeTimer2.reset(0)
        timerStarted2 = True
    Reading_key_resp.keys = []
    Reading_key_resp.rt = []
    _Reading_key_resp_allKeys = []
    imagePages.setImage(ChPage)
    # keep track of which components have finished
    ReadingComponents = [Reading_key_resp, imagePages, PCProbe, SCProbe]
    for thisComponent in ReadingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Reading" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_3
        keys = event.getKeys()
        
        if (mainTimer2.getTime() > 1080) and timerStarted2:
            continueRoutine = False #quit every routine once the main timer goes over 18 minutes
            
        if firstLoop2:
            keys = []
            event.clearEvents()
        
        if currCondition=='SC':
            if Reading_key_resp.keys == 'space':
                continueRoutine = False
            
            if '1' in keys:
                opacityImage2 = 1
                TimeAbs = mainTimer2.getTime()
                TimeSinceLast = probeTimer2.getTime()
                keys = []
                event.clearEvents()
        
            if (opacityImage2 == 1) and ('u' in keys or 'i' in keys):
                opacityImage2 = 0
                time2 = mainTimer2.getTime() - TimeAbs
                resp2 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1
        
            if printNow == 1:
                thisExp.addData('probe_appeared', TimeAbs) #log the time that the SC probe appeared (user pressed '1' key)
                thisExp.addData('time_since_last_probe', TimeSinceLast) #log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time2) #log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp2) #log the key response to the probe
                thisExp.addData('condition', currCondition) #save the current condition
                thisExp.nextEntry() #if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
                probeTimer2.reset(0) 
                time1=0 
                time2=0
                resp1=0
                resp2=0
                printNow = 0
        
        
        if currCondition=='PC':
            if Reading_key_resp.keys == 'space':
                continueRoutine = False
            
            if opacityImage1 != 1 and (len(probe2) > myCount2) and probeTimer2.getTime() >= probe2[myCount2]:
                opacityImage1=1
                TimeAbs = mainTimer2.getTime()
                TimeSinceLast = probeTimer2.getTime() #get the time since the last probe popped up
                
            if opacityImage1 == 1 and ('0' in keys or 'i' in keys or 'u' in keys):
                opacityImage1 = 0
                time1 = mainTimer2.getTime() - TimeAbs
                resp1 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1
        
            if printNow == 1:
                printNow = 0
                thisExp.addData('probe_appeared', TimeAbs) #log the time that the PC probe appeared
                thisExp.addData('time_since_last_probe', TimeSinceLast) #log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time1) #log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp1) #log the key response to the probe
                thisExp.addData('condition', currCondition) #save the current condition
                thisExp.nextEntry() #if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
                probeTimer2.reset(0)
                time1=0
                time2=0
                resp1=0
                resp2=0
                myCount2 = myCount2 + 1
                
        firstLoop2 = False
        
        # *Reading_key_resp* updates
        waitOnFlip = False
        if Reading_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Reading_key_resp.frameNStart = frameN  # exact frame index
            Reading_key_resp.tStart = t  # local t and not account for scr refresh
            Reading_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Reading_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Reading_key_resp.started')
            Reading_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Reading_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Reading_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Reading_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Reading_key_resp.getKeys(keyList=['space',], waitRelease=False)
            _Reading_key_resp_allKeys.extend(theseKeys)
            if len(_Reading_key_resp_allKeys):
                Reading_key_resp.keys = _Reading_key_resp_allKeys[-1].name  # just the last key pressed
                Reading_key_resp.rt = _Reading_key_resp_allKeys[-1].rt
        
        # *imagePages* updates
        if imagePages.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePages.frameNStart = frameN  # exact frame index
            imagePages.tStart = t  # local t and not account for scr refresh
            imagePages.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePages, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePages.started')
            imagePages.setAutoDraw(True)
        
        # *PCProbe* updates
        if PCProbe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PCProbe.frameNStart = frameN  # exact frame index
            PCProbe.tStart = t  # local t and not account for scr refresh
            PCProbe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PCProbe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PCProbe.started')
            PCProbe.setAutoDraw(True)
        if PCProbe.status == STARTED:  # only update if drawing
            PCProbe.setOpacity(opacityImage1, log=False)
        
        # *SCProbe* updates
        if SCProbe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SCProbe.frameNStart = frameN  # exact frame index
            SCProbe.tStart = t  # local t and not account for scr refresh
            SCProbe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SCProbe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SCProbe.started')
            SCProbe.setAutoDraw(True)
        if SCProbe.status == STARTED:  # only update if drawing
            SCProbe.setOpacity(opacityImage2, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Reading" ---
    for thisComponent in ReadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Reading_key_resp.keys in ['', [], None]:  # No response was made
        Reading_key_resp.keys = None
    ReadingLoop.addData('Reading_key_resp.keys',Reading_key_resp.keys)
    if Reading_key_resp.keys != None:  # we had a response
        ReadingLoop.addData('Reading_key_resp.rt', Reading_key_resp.rt)
    # the Routine "Reading" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ReadingLoop'


# --- Prepare to start Routine "EYE_RECORD_STOP" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EYE_RECORD_STOPComponents = [EYE_Record_STOP]
for thisComponent in EYE_RECORD_STOPComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EYE_RECORD_STOP" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *EYE_Record_STOP* updates
    if EYE_Record_STOP.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EYE_Record_STOP.frameNStart = frameN  # exact frame index
        EYE_Record_STOP.tStart = t  # local t and not account for scr refresh
        EYE_Record_STOP.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EYE_Record_STOP, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('EYE_Record_STOP.started', t)
        EYE_Record_STOP.status = STARTED
    if EYE_Record_STOP.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EYE_Record_STOP.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            EYE_Record_STOP.tStop = t  # not accounting for scr refresh
            EYE_Record_STOP.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('EYE_Record_STOP.stopped', t)
            EYE_Record_STOP.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EYE_RECORD_STOPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EYE_RECORD_STOP" ---
for thisComponent in EYE_RECORD_STOPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if EYE_Record_STOP.status != FINISHED:
    EYE_Record_STOP.status = FINISHED

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
QuizLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(quizFile),
    seed=None, name='QuizLoop')
thisExp.addLoop(QuizLoop)  # add the loop to the experiment
thisQuizLoop = QuizLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuizLoop.rgb)
if thisQuizLoop != None:
    for paramName in thisQuizLoop:
        exec('{} = thisQuizLoop[paramName]'.format(paramName))

for thisQuizLoop in QuizLoop:
    currentLoop = QuizLoop
    # abbreviate parameter names if possible (e.g. rgb = thisQuizLoop.rgb)
    if thisQuizLoop != None:
        for paramName in thisQuizLoop:
            exec('{} = thisQuizLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Quiz" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    QuizQuestion.setImage(chQs)
    Quiz_key_resp.keys = []
    Quiz_key_resp.rt = []
    _Quiz_key_resp_allKeys = []
    # keep track of which components have finished
    QuizComponents = [QuizQuestion, Quiz_key_resp]
    for thisComponent in QuizComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Quiz" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *QuizQuestion* updates
        if QuizQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QuizQuestion.frameNStart = frameN  # exact frame index
            QuizQuestion.tStart = t  # local t and not account for scr refresh
            QuizQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuizQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'QuizQuestion.started')
            QuizQuestion.setAutoDraw(True)
        
        # *Quiz_key_resp* updates
        waitOnFlip = False
        if Quiz_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quiz_key_resp.frameNStart = frameN  # exact frame index
            Quiz_key_resp.tStart = t  # local t and not account for scr refresh
            Quiz_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quiz_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Quiz_key_resp.started')
            Quiz_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Quiz_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Quiz_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Quiz_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Quiz_key_resp.getKeys(keyList=['a','b','c','d'], waitRelease=False)
            _Quiz_key_resp_allKeys.extend(theseKeys)
            if len(_Quiz_key_resp_allKeys):
                Quiz_key_resp.keys = _Quiz_key_resp_allKeys[-1].name  # just the last key pressed
                Quiz_key_resp.rt = _Quiz_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QuizComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Quiz" ---
    for thisComponent in QuizComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Quiz_key_resp.keys in ['', [], None]:  # No response was made
        Quiz_key_resp.keys = None
    QuizLoop.addData('Quiz_key_resp.keys',Quiz_key_resp.keys)
    if Quiz_key_resp.keys != None:  # we had a response
        QuizLoop.addData('Quiz_key_resp.rt', Quiz_key_resp.rt)
    # the Routine "Quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'QuizLoop'


# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "InterestingQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InterestingQ_key_resp.keys = []
InterestingQ_key_resp.rt = []
_InterestingQ_key_resp_allKeys = []
# keep track of which components have finished
InterestingQComponents = [interestingImage, InterestingQ_key_resp]
for thisComponent in InterestingQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "InterestingQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interestingImage* updates
    if interestingImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interestingImage.frameNStart = frameN  # exact frame index
        interestingImage.tStart = t  # local t and not account for scr refresh
        interestingImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interestingImage, 'tStartRefresh')  # time at next scr refresh
        interestingImage.setAutoDraw(True)
    
    # *InterestingQ_key_resp* updates
    waitOnFlip = False
    if InterestingQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InterestingQ_key_resp.frameNStart = frameN  # exact frame index
        InterestingQ_key_resp.tStart = t  # local t and not account for scr refresh
        InterestingQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InterestingQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'InterestingQ_key_resp.started')
        InterestingQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InterestingQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InterestingQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InterestingQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = InterestingQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _InterestingQ_key_resp_allKeys.extend(theseKeys)
        if len(_InterestingQ_key_resp_allKeys):
            InterestingQ_key_resp.keys = [key.name for key in _InterestingQ_key_resp_allKeys]  # storing all keys
            InterestingQ_key_resp.rt = [key.rt for key in _InterestingQ_key_resp_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterestingQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InterestingQ" ---
for thisComponent in InterestingQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InterestingQ_key_resp.keys in ['', [], None]:  # No response was made
    InterestingQ_key_resp.keys = None
thisExp.addData('InterestingQ_key_resp.keys',InterestingQ_key_resp.keys)
if InterestingQ_key_resp.keys != None:  # we had a response
    thisExp.addData('InterestingQ_key_resp.rt', InterestingQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "InterestingQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DifficultyQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
DifficultyQ_key_resp.keys = []
DifficultyQ_key_resp.rt = []
_DifficultyQ_key_resp_allKeys = []
# keep track of which components have finished
DifficultyQComponents = [difficultyImage, DifficultyQ_key_resp]
for thisComponent in DifficultyQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "DifficultyQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *difficultyImage* updates
    if difficultyImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        difficultyImage.frameNStart = frameN  # exact frame index
        difficultyImage.tStart = t  # local t and not account for scr refresh
        difficultyImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(difficultyImage, 'tStartRefresh')  # time at next scr refresh
        difficultyImage.setAutoDraw(True)
    
    # *DifficultyQ_key_resp* updates
    waitOnFlip = False
    if DifficultyQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DifficultyQ_key_resp.frameNStart = frameN  # exact frame index
        DifficultyQ_key_resp.tStart = t  # local t and not account for scr refresh
        DifficultyQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DifficultyQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'DifficultyQ_key_resp.started')
        DifficultyQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(DifficultyQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(DifficultyQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if DifficultyQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = DifficultyQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _DifficultyQ_key_resp_allKeys.extend(theseKeys)
        if len(_DifficultyQ_key_resp_allKeys):
            DifficultyQ_key_resp.keys = _DifficultyQ_key_resp_allKeys[0].name  # just the first key pressed
            DifficultyQ_key_resp.rt = _DifficultyQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DifficultyQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DifficultyQ" ---
for thisComponent in DifficultyQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if DifficultyQ_key_resp.keys in ['', [], None]:  # No response was made
    DifficultyQ_key_resp.keys = None
thisExp.addData('DifficultyQ_key_resp.keys',DifficultyQ_key_resp.keys)
if DifficultyQ_key_resp.keys != None:  # we had a response
    thisExp.addData('DifficultyQ_key_resp.rt', DifficultyQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "DifficultyQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Likert_Mot" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
MW_motQ_key_resp.keys = []
MW_motQ_key_resp.rt = []
_MW_motQ_key_resp_allKeys = []
# keep track of which components have finished
Likert_MotComponents = [MW_mot, MW_motQ_key_resp]
for thisComponent in Likert_MotComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Likert_Mot" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MW_mot* updates
    if MW_mot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MW_mot.frameNStart = frameN  # exact frame index
        MW_mot.tStart = t  # local t and not account for scr refresh
        MW_mot.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MW_mot, 'tStartRefresh')  # time at next scr refresh
        MW_mot.setAutoDraw(True)
    
    # *MW_motQ_key_resp* updates
    waitOnFlip = False
    if MW_motQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MW_motQ_key_resp.frameNStart = frameN  # exact frame index
        MW_motQ_key_resp.tStart = t  # local t and not account for scr refresh
        MW_motQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MW_motQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MW_motQ_key_resp.started')
        MW_motQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(MW_motQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(MW_motQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if MW_motQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = MW_motQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _MW_motQ_key_resp_allKeys.extend(theseKeys)
        if len(_MW_motQ_key_resp_allKeys):
            MW_motQ_key_resp.keys = _MW_motQ_key_resp_allKeys[0].name  # just the first key pressed
            MW_motQ_key_resp.rt = _MW_motQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Likert_MotComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Likert_Mot" ---
for thisComponent in Likert_MotComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if MW_motQ_key_resp.keys in ['', [], None]:  # No response was made
    MW_motQ_key_resp.keys = None
thisExp.addData('MW_motQ_key_resp.keys',MW_motQ_key_resp.keys)
if MW_motQ_key_resp.keys != None:  # we had a response
    thisExp.addData('MW_motQ_key_resp.rt', MW_motQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "Likert_Mot" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "unIntMWcapture" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
unintMWkey_resp_2.keys = []
unintMWkey_resp_2.rt = []
_unintMWkey_resp_2_allKeys = []
# keep track of which components have finished
unIntMWcaptureComponents = [MWunint, unintMWkey_resp_2]
for thisComponent in unIntMWcaptureComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "unIntMWcapture" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MWunint* updates
    if MWunint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MWunint.frameNStart = frameN  # exact frame index
        MWunint.tStart = t  # local t and not account for scr refresh
        MWunint.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MWunint, 'tStartRefresh')  # time at next scr refresh
        MWunint.setAutoDraw(True)
    
    # *unintMWkey_resp_2* updates
    waitOnFlip = False
    if unintMWkey_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unintMWkey_resp_2.frameNStart = frameN  # exact frame index
        unintMWkey_resp_2.tStart = t  # local t and not account for scr refresh
        unintMWkey_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unintMWkey_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'unintMWkey_resp_2.started')
        unintMWkey_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(unintMWkey_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(unintMWkey_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if unintMWkey_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = unintMWkey_resp_2.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _unintMWkey_resp_2_allKeys.extend(theseKeys)
        if len(_unintMWkey_resp_2_allKeys):
            unintMWkey_resp_2.keys = _unintMWkey_resp_2_allKeys[0].name  # just the first key pressed
            unintMWkey_resp_2.rt = _unintMWkey_resp_2_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in unIntMWcaptureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "unIntMWcapture" ---
for thisComponent in unIntMWcaptureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if unintMWkey_resp_2.keys in ['', [], None]:  # No response was made
    unintMWkey_resp_2.keys = None
thisExp.addData('unintMWkey_resp_2.keys',unintMWkey_resp_2.keys)
if unintMWkey_resp_2.keys != None:  # we had a response
    thisExp.addData('unintMWkey_resp_2.rt', unintMWkey_resp_2.rt)
thisExp.nextEntry()
# the Routine "unIntMWcapture" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intMWcaptureQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intMWcaptureQ_key_resp.keys = []
intMWcaptureQ_key_resp.rt = []
_intMWcaptureQ_key_resp_allKeys = []
# keep track of which components have finished
intMWcaptureQComponents = [MWcaptureImage, intMWcaptureQ_key_resp]
for thisComponent in intMWcaptureQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intMWcaptureQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MWcaptureImage* updates
    if MWcaptureImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MWcaptureImage.frameNStart = frameN  # exact frame index
        MWcaptureImage.tStart = t  # local t and not account for scr refresh
        MWcaptureImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MWcaptureImage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MWcaptureImage.started')
        MWcaptureImage.setAutoDraw(True)
    
    # *intMWcaptureQ_key_resp* updates
    waitOnFlip = False
    if intMWcaptureQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intMWcaptureQ_key_resp.frameNStart = frameN  # exact frame index
        intMWcaptureQ_key_resp.tStart = t  # local t and not account for scr refresh
        intMWcaptureQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intMWcaptureQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intMWcaptureQ_key_resp.started')
        intMWcaptureQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intMWcaptureQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intMWcaptureQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intMWcaptureQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intMWcaptureQ_key_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intMWcaptureQ_key_resp_allKeys.extend(theseKeys)
        if len(_intMWcaptureQ_key_resp_allKeys):
            intMWcaptureQ_key_resp.keys = _intMWcaptureQ_key_resp_allKeys[0].name  # just the first key pressed
            intMWcaptureQ_key_resp.rt = _intMWcaptureQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intMWcaptureQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intMWcaptureQ" ---
for thisComponent in intMWcaptureQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intMWcaptureQ_key_resp.keys in ['', [], None]:  # No response was made
    intMWcaptureQ_key_resp.keys = None
thisExp.addData('intMWcaptureQ_key_resp.keys',intMWcaptureQ_key_resp.keys)
if intMWcaptureQ_key_resp.keys != None:  # we had a response
    thisExp.addData('intMWcaptureQ_key_resp.rt', intMWcaptureQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "intMWcaptureQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "Halfway" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
HalfwayResp.keys = []
HalfwayResp.rt = []
_HalfwayResp_allKeys = []
# Run 'Begin Routine' code from halfway_code
if currCondition == 'SC':
    currCondition = 'PC'
else:
    currCondition = 'SC'

if currConditionP == 'Life':
    currConditionP ='Tropo'
else:
    currConditionP ='Life'
# keep track of which components have finished
HalfwayComponents = [HalfwayText, HalfwayResp]
for thisComponent in HalfwayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Halfway" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *HalfwayText* updates
    if HalfwayText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HalfwayText.frameNStart = frameN  # exact frame index
        HalfwayText.tStart = t  # local t and not account for scr refresh
        HalfwayText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HalfwayText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'HalfwayText.started')
        HalfwayText.setAutoDraw(True)
    
    # *HalfwayResp* updates
    if HalfwayResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HalfwayResp.frameNStart = frameN  # exact frame index
        HalfwayResp.tStart = t  # local t and not account for scr refresh
        HalfwayResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HalfwayResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('HalfwayResp.started', t)
        HalfwayResp.status = STARTED
        # keyboard checking is just starting
        HalfwayResp.clock.reset()  # now t=0
    if HalfwayResp.status == STARTED:
        theseKeys = HalfwayResp.getKeys(keyList=['space'], waitRelease=False)
        _HalfwayResp_allKeys.extend(theseKeys)
        if len(_HalfwayResp_allKeys):
            HalfwayResp.keys = _HalfwayResp_allKeys[-1].name  # just the last key pressed
            HalfwayResp.rt = _HalfwayResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HalfwayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Halfway" ---
for thisComponent in HalfwayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Halfway" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MWDefinitions2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(InstrFile2),
    seed=None, name='MWDefinitions2')
thisExp.addLoop(MWDefinitions2)  # add the loop to the experiment
thisMWDefinitions2 = MWDefinitions2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMWDefinitions2.rgb)
if thisMWDefinitions2 != None:
    for paramName in thisMWDefinitions2:
        exec('{} = thisMWDefinitions2[paramName]'.format(paramName))

for thisMWDefinitions2 in MWDefinitions2:
    currentLoop = MWDefinitions2
    # abbreviate parameter names if possible (e.g. rgb = thisMWDefinitions2.rgb)
    if thisMWDefinitions2 != None:
        for paramName in thisMWDefinitions2:
            exec('{} = thisMWDefinitions2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MW_def2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    MWdef_image.setImage(chInstrSlide)
    MW_def2_key_resp.keys = []
    MW_def2_key_resp.rt = []
    _MW_def2_key_resp_allKeys = []
    # keep track of which components have finished
    MW_def2Components = [MWdef_image, MW_def2_key_resp]
    for thisComponent in MW_def2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "MW_def2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MWdef_image* updates
        if MWdef_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MWdef_image.frameNStart = frameN  # exact frame index
            MWdef_image.tStart = t  # local t and not account for scr refresh
            MWdef_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MWdef_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MWdef_image.started')
            MWdef_image.setAutoDraw(True)
        
        # *MW_def2_key_resp* updates
        waitOnFlip = False
        if MW_def2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MW_def2_key_resp.frameNStart = frameN  # exact frame index
            MW_def2_key_resp.tStart = t  # local t and not account for scr refresh
            MW_def2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MW_def2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MW_def2_key_resp.started')
            MW_def2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MW_def2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MW_def2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MW_def2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = MW_def2_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _MW_def2_key_resp_allKeys.extend(theseKeys)
            if len(_MW_def2_key_resp_allKeys):
                MW_def2_key_resp.keys = _MW_def2_key_resp_allKeys[-1].name  # just the last key pressed
                MW_def2_key_resp.rt = _MW_def2_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MW_def2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MW_def2" ---
    for thisComponent in MW_def2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if MW_def2_key_resp.keys in ['', [], None]:  # No response was made
        MW_def2_key_resp.keys = None
    MWDefinitions2.addData('MW_def2_key_resp.keys',MW_def2_key_resp.keys)
    if MW_def2_key_resp.keys != None:  # we had a response
        MWDefinitions2.addData('MW_def2_key_resp.rt', MW_def2_key_resp.rt)
    # the Routine "MW_def2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'MWDefinitions2'


# --- Prepare to start Routine "IntroExp2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IntroExp2_key_resp.keys = []
IntroExp2_key_resp.rt = []
_IntroExp2_key_resp_allKeys = []
# keep track of which components have finished
IntroExp2Components = [probe_message, IntroExp2_key_resp]
for thisComponent in IntroExp2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IntroExp2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *probe_message* updates
    if probe_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        probe_message.frameNStart = frameN  # exact frame index
        probe_message.tStart = t  # local t and not account for scr refresh
        probe_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(probe_message, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'probe_message.started')
        probe_message.setAutoDraw(True)
    
    # *IntroExp2_key_resp* updates
    waitOnFlip = False
    if IntroExp2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroExp2_key_resp.frameNStart = frameN  # exact frame index
        IntroExp2_key_resp.tStart = t  # local t and not account for scr refresh
        IntroExp2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroExp2_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IntroExp2_key_resp.started')
        IntroExp2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IntroExp2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IntroExp2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IntroExp2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = IntroExp2_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _IntroExp2_key_resp_allKeys.extend(theseKeys)
        if len(_IntroExp2_key_resp_allKeys):
            IntroExp2_key_resp.keys = _IntroExp2_key_resp_allKeys[-1].name  # just the last key pressed
            IntroExp2_key_resp.rt = _IntroExp2_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroExp2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IntroExp2" ---
for thisComponent in IntroExp2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IntroExp2_key_resp.keys in ['', [], None]:  # No response was made
    IntroExp2_key_resp.keys = None
thisExp.addData('IntroExp2_key_resp.keys',IntroExp2_key_resp.keys)
if IntroExp2_key_resp.keys != None:  # we had a response
    thisExp.addData('IntroExp2_key_resp.rt', IntroExp2_key_resp.rt)
thisExp.nextEntry()
# the Routine "IntroExp2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EYE_RECORD_START" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EYE_RECORD_STARTComponents = [etRecord_START]
for thisComponent in EYE_RECORD_STARTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EYE_RECORD_START" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *etRecord_START* updates
    if etRecord_START.status == NOT_STARTED and t >= 1-frameTolerance:
        # keep track of start time/frame for later
        etRecord_START.frameNStart = frameN  # exact frame index
        etRecord_START.tStart = t  # local t and not account for scr refresh
        etRecord_START.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etRecord_START, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('etRecord_START.started', t)
        etRecord_START.status = STARTED
    if etRecord_START.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etRecord_START.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            etRecord_START.tStop = t  # not accounting for scr refresh
            etRecord_START.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('etRecord_START.stopped', t)
            etRecord_START.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EYE_RECORD_STARTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EYE_RECORD_START" ---
for thisComponent in EYE_RECORD_STARTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if etRecord_START.status != FINISHED:
    etRecord_START.status = FINISHED
# the Routine "EYE_RECORD_START" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ReadingLoop2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(stimFile2),
    seed=None, name='ReadingLoop2')
thisExp.addLoop(ReadingLoop2)  # add the loop to the experiment
thisReadingLoop2 = ReadingLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReadingLoop2.rgb)
if thisReadingLoop2 != None:
    for paramName in thisReadingLoop2:
        exec('{} = thisReadingLoop2[paramName]'.format(paramName))

for thisReadingLoop2 in ReadingLoop2:
    currentLoop = ReadingLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisReadingLoop2.rgb)
    if thisReadingLoop2 != None:
        for paramName in thisReadingLoop2:
            exec('{} = thisReadingLoop2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Reading2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Reading2_key_resp.keys = []
    Reading2_key_resp.rt = []
    _Reading2_key_resp_allKeys = []
    imagePages2.setImage(ChPage)
    # Run 'Begin Routine' code from code_2
    if firstRoutine4:
        opacityImage1 = 0
        opacityImage2 = 0
        time1=0
        time2=0
        resp1=0
        resp2=0
        printNow = 0
        keys = ""
        firstRoutine4 = False
        mainTimer4.reset(0)
        probeTimer4.reset(0)
        timerStarted4 = True
    # keep track of which components have finished
    Reading2Components = [Reading2_key_resp, imagePages2, PCProbe2, SCProbe2]
    for thisComponent in Reading2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Reading2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Reading2_key_resp* updates
        waitOnFlip = False
        if Reading2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Reading2_key_resp.frameNStart = frameN  # exact frame index
            Reading2_key_resp.tStart = t  # local t and not account for scr refresh
            Reading2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Reading2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Reading2_key_resp.started')
            Reading2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Reading2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Reading2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Reading2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Reading2_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Reading2_key_resp_allKeys.extend(theseKeys)
            if len(_Reading2_key_resp_allKeys):
                Reading2_key_resp.keys = _Reading2_key_resp_allKeys[-1].name  # just the last key pressed
                Reading2_key_resp.rt = _Reading2_key_resp_allKeys[-1].rt
        
        # *imagePages2* updates
        if imagePages2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePages2.frameNStart = frameN  # exact frame index
            imagePages2.tStart = t  # local t and not account for scr refresh
            imagePages2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePages2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePages2.started')
            imagePages2.setAutoDraw(True)
        
        # *PCProbe2* updates
        if PCProbe2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PCProbe2.frameNStart = frameN  # exact frame index
            PCProbe2.tStart = t  # local t and not account for scr refresh
            PCProbe2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PCProbe2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PCProbe2.started')
            PCProbe2.setAutoDraw(True)
        if PCProbe2.status == STARTED:  # only update if drawing
            PCProbe2.setOpacity(opacityImage1, log=False)
        
        # *SCProbe2* updates
        if SCProbe2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SCProbe2.frameNStart = frameN  # exact frame index
            SCProbe2.tStart = t  # local t and not account for scr refresh
            SCProbe2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SCProbe2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SCProbe2.started')
            SCProbe2.setAutoDraw(True)
        if SCProbe2.status == STARTED:  # only update if drawing
            SCProbe2.setOpacity(opacityImage2, log=False)
        # Run 'Each Frame' code from code_2
        keys = event.getKeys()
        
        if (mainTimer4.getTime() > 1080) and timerStarted4:
            continueRoutine = False
            
        if firstLoop4:
            keys = []
            event.clearEvents()
        
        #this is the self-caught condition but we check if we're in PC because this is run 2
        if currCondition=='SC':
            
            if Reading2_key_resp.keys == 'space':
                continueRoutine = False
            
            if '1' in keys:
                opacityImage2 = 1
                TimeAbs = mainTimer4.getTime()
                TimeSinceLast = probeTimer4.getTime()
                keys = []
                event.clearEvents()
        
            if (opacityImage2 == 1) and ('u' in keys or 'i' in keys):
                opacityImage2 = 0
                time2 = mainTimer4.getTime() - TimeAbs
                resp2 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1
        
            if printNow == 1:
                thisExp.addData('probe_appeared', TimeAbs) #log the time that the SC probe appeared (user pressed '1' key)
                thisExp.addData('time_since_last_probe', TimeSinceLast) #log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time2) #log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp2) #log the key response to the probe
                thisExp.addData('condition', currCondition) #save the current condition
                thisExp.nextEntry() #if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
                probeTimer4.reset(0)
                time1=0
                time2=0
                resp1=0
                resp2=0
                printNow = 0
        
        #this is the probe-caught condition but we check if we're in SC because this is the second run
        if currCondition=='PC': 
            
            if Reading2_key_resp.keys == 'space':
                continueRoutine = False
            
            if opacityImage1 != 1 and (len(probe4) > myCount4) and probeTimer4.getTime() >= probe4[myCount4]:
                opacityImage1=1
                TimeAbs = mainTimer4.getTime()
                TimeSinceLast = probeTimer4.getTime() #get the time since the last probe went away
                
            if opacityImage1 == 1 and ('0' in keys or 'i' in keys or 'u' in keys):
                opacityImage1 = 0
                time1 = mainTimer4.getTime() - TimeAbs
                resp1 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1
        
            if printNow == 1:
                thisExp.addData('probe_appeared', TimeAbs) #log the time that the PC probe appeared
                thisExp.addData('time_since_last_probe', TimeSinceLast) #log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time1) #log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp1) #log the key response to the probe
                thisExp.addData('condition', currCondition) #save the current condition
                thisExp.nextEntry() #if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
                probeTimer4.reset(0)
                time1=0
                time2=0
                resp1=0
                resp2=0
                myCount4 = myCount4 + 1
                printNow = 0
                
        firstLoop4 = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reading2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Reading2" ---
    for thisComponent in Reading2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Reading2_key_resp.keys in ['', [], None]:  # No response was made
        Reading2_key_resp.keys = None
    ReadingLoop2.addData('Reading2_key_resp.keys',Reading2_key_resp.keys)
    if Reading2_key_resp.keys != None:  # we had a response
        ReadingLoop2.addData('Reading2_key_resp.rt', Reading2_key_resp.rt)
    # the Routine "Reading2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ReadingLoop2'


# --- Prepare to start Routine "EYE_RECORD_STOP" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EYE_RECORD_STOPComponents = [EYE_Record_STOP]
for thisComponent in EYE_RECORD_STOPComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EYE_RECORD_STOP" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *EYE_Record_STOP* updates
    if EYE_Record_STOP.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EYE_Record_STOP.frameNStart = frameN  # exact frame index
        EYE_Record_STOP.tStart = t  # local t and not account for scr refresh
        EYE_Record_STOP.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EYE_Record_STOP, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('EYE_Record_STOP.started', t)
        EYE_Record_STOP.status = STARTED
    if EYE_Record_STOP.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EYE_Record_STOP.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            EYE_Record_STOP.tStop = t  # not accounting for scr refresh
            EYE_Record_STOP.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('EYE_Record_STOP.stopped', t)
            EYE_Record_STOP.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EYE_RECORD_STOPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EYE_RECORD_STOP" ---
for thisComponent in EYE_RECORD_STOPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if EYE_Record_STOP.status != FINISHED:
    EYE_Record_STOP.status = FINISHED
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
QuizLoop2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(quizFile2),
    seed=None, name='QuizLoop2')
thisExp.addLoop(QuizLoop2)  # add the loop to the experiment
thisQuizLoop2 = QuizLoop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuizLoop2.rgb)
if thisQuizLoop2 != None:
    for paramName in thisQuizLoop2:
        exec('{} = thisQuizLoop2[paramName]'.format(paramName))

for thisQuizLoop2 in QuizLoop2:
    currentLoop = QuizLoop2
    # abbreviate parameter names if possible (e.g. rgb = thisQuizLoop2.rgb)
    if thisQuizLoop2 != None:
        for paramName in thisQuizLoop2:
            exec('{} = thisQuizLoop2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Quiz2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    QuizQuestion2.setImage(chQs)
    Quiz2_key_resp.keys = []
    Quiz2_key_resp.rt = []
    _Quiz2_key_resp_allKeys = []
    # keep track of which components have finished
    Quiz2Components = [QuizQuestion2, Quiz2_key_resp]
    for thisComponent in Quiz2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Quiz2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *QuizQuestion2* updates
        if QuizQuestion2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QuizQuestion2.frameNStart = frameN  # exact frame index
            QuizQuestion2.tStart = t  # local t and not account for scr refresh
            QuizQuestion2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuizQuestion2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'QuizQuestion2.started')
            QuizQuestion2.setAutoDraw(True)
        
        # *Quiz2_key_resp* updates
        waitOnFlip = False
        if Quiz2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Quiz2_key_resp.frameNStart = frameN  # exact frame index
            Quiz2_key_resp.tStart = t  # local t and not account for scr refresh
            Quiz2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Quiz2_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Quiz2_key_resp.started')
            Quiz2_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Quiz2_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Quiz2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Quiz2_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Quiz2_key_resp.getKeys(keyList=['a','b','c','d'], waitRelease=False)
            _Quiz2_key_resp_allKeys.extend(theseKeys)
            if len(_Quiz2_key_resp_allKeys):
                Quiz2_key_resp.keys = _Quiz2_key_resp_allKeys[-1].name  # just the last key pressed
                Quiz2_key_resp.rt = _Quiz2_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Quiz2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Quiz2" ---
    for thisComponent in Quiz2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Quiz2_key_resp.keys in ['', [], None]:  # No response was made
        Quiz2_key_resp.keys = None
    QuizLoop2.addData('Quiz2_key_resp.keys',Quiz2_key_resp.keys)
    if Quiz2_key_resp.keys != None:  # we had a response
        QuizLoop2.addData('Quiz2_key_resp.rt', Quiz2_key_resp.rt)
    # the Routine "Quiz2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'QuizLoop2'


# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "InterestingQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
InterestingQ_key_resp.keys = []
InterestingQ_key_resp.rt = []
_InterestingQ_key_resp_allKeys = []
# keep track of which components have finished
InterestingQComponents = [interestingImage, InterestingQ_key_resp]
for thisComponent in InterestingQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "InterestingQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *interestingImage* updates
    if interestingImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interestingImage.frameNStart = frameN  # exact frame index
        interestingImage.tStart = t  # local t and not account for scr refresh
        interestingImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interestingImage, 'tStartRefresh')  # time at next scr refresh
        interestingImage.setAutoDraw(True)
    
    # *InterestingQ_key_resp* updates
    waitOnFlip = False
    if InterestingQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InterestingQ_key_resp.frameNStart = frameN  # exact frame index
        InterestingQ_key_resp.tStart = t  # local t and not account for scr refresh
        InterestingQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InterestingQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'InterestingQ_key_resp.started')
        InterestingQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InterestingQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InterestingQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InterestingQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = InterestingQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _InterestingQ_key_resp_allKeys.extend(theseKeys)
        if len(_InterestingQ_key_resp_allKeys):
            InterestingQ_key_resp.keys = [key.name for key in _InterestingQ_key_resp_allKeys]  # storing all keys
            InterestingQ_key_resp.rt = [key.rt for key in _InterestingQ_key_resp_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterestingQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InterestingQ" ---
for thisComponent in InterestingQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if InterestingQ_key_resp.keys in ['', [], None]:  # No response was made
    InterestingQ_key_resp.keys = None
thisExp.addData('InterestingQ_key_resp.keys',InterestingQ_key_resp.keys)
if InterestingQ_key_resp.keys != None:  # we had a response
    thisExp.addData('InterestingQ_key_resp.rt', InterestingQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "InterestingQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DifficultyQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
DifficultyQ_key_resp.keys = []
DifficultyQ_key_resp.rt = []
_DifficultyQ_key_resp_allKeys = []
# keep track of which components have finished
DifficultyQComponents = [difficultyImage, DifficultyQ_key_resp]
for thisComponent in DifficultyQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "DifficultyQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *difficultyImage* updates
    if difficultyImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        difficultyImage.frameNStart = frameN  # exact frame index
        difficultyImage.tStart = t  # local t and not account for scr refresh
        difficultyImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(difficultyImage, 'tStartRefresh')  # time at next scr refresh
        difficultyImage.setAutoDraw(True)
    
    # *DifficultyQ_key_resp* updates
    waitOnFlip = False
    if DifficultyQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DifficultyQ_key_resp.frameNStart = frameN  # exact frame index
        DifficultyQ_key_resp.tStart = t  # local t and not account for scr refresh
        DifficultyQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DifficultyQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'DifficultyQ_key_resp.started')
        DifficultyQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(DifficultyQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(DifficultyQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if DifficultyQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = DifficultyQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _DifficultyQ_key_resp_allKeys.extend(theseKeys)
        if len(_DifficultyQ_key_resp_allKeys):
            DifficultyQ_key_resp.keys = _DifficultyQ_key_resp_allKeys[0].name  # just the first key pressed
            DifficultyQ_key_resp.rt = _DifficultyQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DifficultyQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DifficultyQ" ---
for thisComponent in DifficultyQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if DifficultyQ_key_resp.keys in ['', [], None]:  # No response was made
    DifficultyQ_key_resp.keys = None
thisExp.addData('DifficultyQ_key_resp.keys',DifficultyQ_key_resp.keys)
if DifficultyQ_key_resp.keys != None:  # we had a response
    thisExp.addData('DifficultyQ_key_resp.rt', DifficultyQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "DifficultyQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Likert_Mot" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
MW_motQ_key_resp.keys = []
MW_motQ_key_resp.rt = []
_MW_motQ_key_resp_allKeys = []
# keep track of which components have finished
Likert_MotComponents = [MW_mot, MW_motQ_key_resp]
for thisComponent in Likert_MotComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Likert_Mot" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MW_mot* updates
    if MW_mot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MW_mot.frameNStart = frameN  # exact frame index
        MW_mot.tStart = t  # local t and not account for scr refresh
        MW_mot.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MW_mot, 'tStartRefresh')  # time at next scr refresh
        MW_mot.setAutoDraw(True)
    
    # *MW_motQ_key_resp* updates
    waitOnFlip = False
    if MW_motQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MW_motQ_key_resp.frameNStart = frameN  # exact frame index
        MW_motQ_key_resp.tStart = t  # local t and not account for scr refresh
        MW_motQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MW_motQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MW_motQ_key_resp.started')
        MW_motQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(MW_motQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(MW_motQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if MW_motQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = MW_motQ_key_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _MW_motQ_key_resp_allKeys.extend(theseKeys)
        if len(_MW_motQ_key_resp_allKeys):
            MW_motQ_key_resp.keys = _MW_motQ_key_resp_allKeys[0].name  # just the first key pressed
            MW_motQ_key_resp.rt = _MW_motQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Likert_MotComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Likert_Mot" ---
for thisComponent in Likert_MotComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if MW_motQ_key_resp.keys in ['', [], None]:  # No response was made
    MW_motQ_key_resp.keys = None
thisExp.addData('MW_motQ_key_resp.keys',MW_motQ_key_resp.keys)
if MW_motQ_key_resp.keys != None:  # we had a response
    thisExp.addData('MW_motQ_key_resp.rt', MW_motQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "Likert_Mot" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "unIntMWcapture" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
unintMWkey_resp_2.keys = []
unintMWkey_resp_2.rt = []
_unintMWkey_resp_2_allKeys = []
# keep track of which components have finished
unIntMWcaptureComponents = [MWunint, unintMWkey_resp_2]
for thisComponent in unIntMWcaptureComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "unIntMWcapture" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MWunint* updates
    if MWunint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MWunint.frameNStart = frameN  # exact frame index
        MWunint.tStart = t  # local t and not account for scr refresh
        MWunint.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MWunint, 'tStartRefresh')  # time at next scr refresh
        MWunint.setAutoDraw(True)
    
    # *unintMWkey_resp_2* updates
    waitOnFlip = False
    if unintMWkey_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unintMWkey_resp_2.frameNStart = frameN  # exact frame index
        unintMWkey_resp_2.tStart = t  # local t and not account for scr refresh
        unintMWkey_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unintMWkey_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'unintMWkey_resp_2.started')
        unintMWkey_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(unintMWkey_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(unintMWkey_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if unintMWkey_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = unintMWkey_resp_2.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _unintMWkey_resp_2_allKeys.extend(theseKeys)
        if len(_unintMWkey_resp_2_allKeys):
            unintMWkey_resp_2.keys = _unintMWkey_resp_2_allKeys[0].name  # just the first key pressed
            unintMWkey_resp_2.rt = _unintMWkey_resp_2_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in unIntMWcaptureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "unIntMWcapture" ---
for thisComponent in unIntMWcaptureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if unintMWkey_resp_2.keys in ['', [], None]:  # No response was made
    unintMWkey_resp_2.keys = None
thisExp.addData('unintMWkey_resp_2.keys',unintMWkey_resp_2.keys)
if unintMWkey_resp_2.keys != None:  # we had a response
    thisExp.addData('unintMWkey_resp_2.rt', unintMWkey_resp_2.rt)
thisExp.nextEntry()
# the Routine "unIntMWcapture" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intMWcaptureQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intMWcaptureQ_key_resp.keys = []
intMWcaptureQ_key_resp.rt = []
_intMWcaptureQ_key_resp_allKeys = []
# keep track of which components have finished
intMWcaptureQComponents = [MWcaptureImage, intMWcaptureQ_key_resp]
for thisComponent in intMWcaptureQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intMWcaptureQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MWcaptureImage* updates
    if MWcaptureImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MWcaptureImage.frameNStart = frameN  # exact frame index
        MWcaptureImage.tStart = t  # local t and not account for scr refresh
        MWcaptureImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MWcaptureImage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'MWcaptureImage.started')
        MWcaptureImage.setAutoDraw(True)
    
    # *intMWcaptureQ_key_resp* updates
    waitOnFlip = False
    if intMWcaptureQ_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intMWcaptureQ_key_resp.frameNStart = frameN  # exact frame index
        intMWcaptureQ_key_resp.tStart = t  # local t and not account for scr refresh
        intMWcaptureQ_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intMWcaptureQ_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intMWcaptureQ_key_resp.started')
        intMWcaptureQ_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intMWcaptureQ_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intMWcaptureQ_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intMWcaptureQ_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intMWcaptureQ_key_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intMWcaptureQ_key_resp_allKeys.extend(theseKeys)
        if len(_intMWcaptureQ_key_resp_allKeys):
            intMWcaptureQ_key_resp.keys = _intMWcaptureQ_key_resp_allKeys[0].name  # just the first key pressed
            intMWcaptureQ_key_resp.rt = _intMWcaptureQ_key_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intMWcaptureQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intMWcaptureQ" ---
for thisComponent in intMWcaptureQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intMWcaptureQ_key_resp.keys in ['', [], None]:  # No response was made
    intMWcaptureQ_key_resp.keys = None
thisExp.addData('intMWcaptureQ_key_resp.keys',intMWcaptureQ_key_resp.keys)
if intMWcaptureQ_key_resp.keys != None:  # we had a response
    thisExp.addData('intMWcaptureQ_key_resp.rt', intMWcaptureQ_key_resp.rt)
thisExp.nextEntry()
# the Routine "intMWcaptureQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [textInterval]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterval* updates
    if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInterval.frameNStart = frameN  # exact frame index
        textInterval.tStart = t  # local t and not account for scr refresh
        textInterval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInterval.started')
        textInterval.setAutoDraw(True)
    if textInterval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textInterval.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            textInterval.tStop = t  # not accounting for scr refresh
            textInterval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.stopped')
            textInterval.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank" ---
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "EndText" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
EndTextComponents = [EndExpText, key_resp]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndText" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndExpText* updates
    if EndExpText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndExpText.frameNStart = frameN  # exact frame index
        EndExpText.tStart = t  # local t and not account for scr refresh
        EndExpText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndExpText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndExpText.started')
        EndExpText.setAutoDraw(True)
    if EndExpText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndExpText.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            EndExpText.tStop = t  # not accounting for scr refresh
            EndExpText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndExpText.stopped')
            EndExpText.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndText" ---
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "EndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
