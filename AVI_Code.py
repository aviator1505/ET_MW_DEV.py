# Import all dependencies and packages
from __future__ import division
from __future__ import print_function

import psychopy
# From Eyelink

from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import pylink
import os
import platform
import random
import time
import sys
from psychopy import visual, core, event, monitors, gui, hardware
from PIL import Image  # for preparing the Host backdrop image
from string import ascii_letters, digits

# From PsychoPy
from psychopy.visual import TextStim
from psychopy.visual import Window
from psychopy.hardware.keyboard import Keyboard


# Call all the important functions..... INITIALIZE.
win = visual.Window(size=[1920, 1080], fullscr=False, screen=0,winType='pyglet', allowStencil=False, monitor='testMonitor',
                    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', blendMode='avg', useFBO=True, units='norm')

clock = core.Clock()
kb = Keyboard()


