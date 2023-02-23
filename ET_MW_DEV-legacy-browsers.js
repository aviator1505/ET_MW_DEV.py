/****************** 
 * Et_Mw_Dev Test *
 ******************/


// store info about the experiment session:
let expName = 'ET_MW_DEV';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Calibration_InstructionsRoutineBegin());
flowScheduler.add(Calibration_InstructionsRoutineEachFrame());
flowScheduler.add(Calibration_InstructionsRoutineEnd());
flowScheduler.add(LaunchRoutineBegin());
flowScheduler.add(LaunchRoutineEachFrame());
flowScheduler.add(LaunchRoutineEnd());
const MWdefinitionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(MWdefinitionsLoopBegin(MWdefinitionsLoopScheduler));
flowScheduler.add(MWdefinitionsLoopScheduler);
flowScheduler.add(MWdefinitionsLoopEnd);
flowScheduler.add(IntroExpRoutineBegin());
flowScheduler.add(IntroExpRoutineEachFrame());
flowScheduler.add(IntroExpRoutineEnd());
flowScheduler.add(PageSkippingRoutineBegin());
flowScheduler.add(PageSkippingRoutineEachFrame());
flowScheduler.add(PageSkippingRoutineEnd());
const ReadingLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ReadingLoopLoopBegin(ReadingLoopLoopScheduler));
flowScheduler.add(ReadingLoopLoopScheduler);
flowScheduler.add(ReadingLoopLoopEnd);
flowScheduler.add(EYE_RECORD_STOPRoutineBegin());
flowScheduler.add(EYE_RECORD_STOPRoutineEachFrame());
flowScheduler.add(EYE_RECORD_STOPRoutineEnd());
flowScheduler.add(blankRoutineBegin());
flowScheduler.add(blankRoutineEachFrame());
flowScheduler.add(blankRoutineEnd());
flowScheduler.add(EndTextRoutineBegin());
flowScheduler.add(EndTextRoutineEachFrame());
flowScheduler.add(EndTextRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'images/SC_v2.png', 'path': 'images/SC_v2.png'},
    {'name': 'images/PC_v2.png', 'path': 'images/PC_v2.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Calibration_Instructions"
  Calibration_InstructionsClock = new util.Clock();
  Cal_Instruct1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cal_Instruct1',
    text: "EYETRACKER CALIBRATION\n\nNow that you're fitted with the eyetracker, there will be some calibration points shown on the screen. Please follow the center of the targets with your eyes while keeping your head still. \n\nThe researcher may then need to make adjustments to the eyetracker. Please let them know if you're uncomfortable.\n\n(press spacebar to continue)",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  Calibration_text_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Launch"
  LaunchClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  import * as random from 'random';
  import * as xlrd from 'xlrd';
  import * as time from 'time';
  var currCondition, currConditionP, rand, randP;
  random.seed(time.clock());
  rand = random.randint(1, 2);
  randP = random.randint(3, 4);
  if ((rand === 1)) {
      currCondition = "PC";
  } else {
      if ((rand === 2)) {
          currCondition = "SC";
      }
  }
  if ((randP === 3)) {
      currConditionP = "Tropo";
  } else {
      if ((randP === 4)) {
          currConditionP = "Life";
      }
  }
  currCondition = "PC";
  
  // Initialize components for Routine "MW_def"
  MW_defClock = new util.Clock();
  MWdefInstr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'MWdefInstr', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 0.8],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  MWdefInstr_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "IntroExp"
  IntroExpClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: probeMessage,
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  IntroExp_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PageSkipping"
  PageSkippingClock = new util.Clock();
  NoSkipping = new visual.TextStim({
    win: psychoJS.window,
    name: 'NoSkipping',
    text: 'Please read at your normal pace and do not skip pages.\n\n\n(press spacebar to continue)',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_Skip = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Reading"
  ReadingClock = new util.Clock();
  // Run 'Begin Experiment' code from code_3
  import * as random from 'random';
  import * as copy from 'copy';
  import {randint} from 'random';
  import {*} from 'decimal';
  import * as csv from 'csv';
  import {*} from 'numpy';
  import {core} from 'psychopy';
  var isPaused, mainTimer, myCount, opacityImage1, opacityImage2, opacityRestart, printNow, printX, probe, probeTimer, resp1, resp2, time1, time2, timeThru;
  opacityImage1 = 0;
  opacityImage2 = 0;
  opacityRestart = 0;
  isPaused = 0;
  time1 = 0;
  time2 = 0;
  resp1 = 0;
  resp2 = 0;
  timeThru = 0;
  printNow = 0;
  printX = 0;
  mainTimer = new core.Clock();
  probeTimer = new core.Clock();
  myCount = 1;
  probe = [0, 8, 10, 15];
  
  Reading_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  imagePages = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagePages', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.85, 0.85],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  PCProbe = new visual.ImageStim({
    win : psychoJS.window,
    name : 'PCProbe', units : undefined, 
    image : 'images/PC_v2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 0.85],
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  SCProbe = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SCProbe', units : undefined, 
    image : 'images/SC_v2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.85],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "EYE_RECORD_STOP"
  EYE_RECORD_STOPClock = new util.Clock();
  // Initialize components for Routine "blank"
  blankClock = new util.Clock();
  textInterval = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInterval',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "EndText"
  EndTextClock = new util.Clock();
  EndExpText = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndExpText',
    text: "Thank you for participating in this experiment!\n\nPlease let the research assistant know if you would like to be debriefed.\n\nThank you!\n\n(Press 'space' to continue)",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function Calibration_InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Calibration_Instructions' ---
    t = 0;
    Calibration_InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Calibration_text_resp.keys = undefined;
    Calibration_text_resp.rt = undefined;
    _Calibration_text_resp_allKeys = [];
    // keep track of which components have finished
    Calibration_InstructionsComponents = [];
    Calibration_InstructionsComponents.push(Cal_Instruct1);
    Calibration_InstructionsComponents.push(Calibration_text_resp);
    
    Calibration_InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Calibration_InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Calibration_Instructions' ---
    // get current time
    t = Calibration_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Cal_Instruct1* updates
    if (t >= 0.0 && Cal_Instruct1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cal_Instruct1.tStart = t;  // (not accounting for frame time here)
      Cal_Instruct1.frameNStart = frameN;  // exact frame index
      
      Cal_Instruct1.setAutoDraw(true);
    }

    
    // *Calibration_text_resp* updates
    if (t >= 0.0 && Calibration_text_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Calibration_text_resp.tStart = t;  // (not accounting for frame time here)
      Calibration_text_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Calibration_text_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Calibration_text_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Calibration_text_resp.clearEvents(); });
    }

    if (Calibration_text_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Calibration_text_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Calibration_text_resp_allKeys = _Calibration_text_resp_allKeys.concat(theseKeys);
      if (_Calibration_text_resp_allKeys.length > 0) {
        Calibration_text_resp.keys = _Calibration_text_resp_allKeys[_Calibration_text_resp_allKeys.length - 1].name;  // just the last key pressed
        Calibration_text_resp.rt = _Calibration_text_resp_allKeys[_Calibration_text_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Calibration_InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Calibration_InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Calibration_Instructions' ---
    Calibration_InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Calibration_text_resp.corr, level);
    }
    psychoJS.experiment.addData('Calibration_text_resp.keys', Calibration_text_resp.keys);
    if (typeof Calibration_text_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Calibration_text_resp.rt', Calibration_text_resp.rt);
        routineTimer.reset();
        }
    
    Calibration_text_resp.stop();
    // the Routine "Calibration_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function LaunchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Launch' ---
    t = 0;
    LaunchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    LaunchComponents = [];
    
    LaunchComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function LaunchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Launch' ---
    // get current time
    t = LaunchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LaunchComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function LaunchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Launch' ---
    LaunchComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Launch" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function MWdefinitionsLoopBegin(MWdefinitionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    MWdefinitions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: InstrFile,
      seed: undefined, name: 'MWdefinitions'
    });
    psychoJS.experiment.addLoop(MWdefinitions); // add the loop to the experiment
    currentLoop = MWdefinitions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    MWdefinitions.forEach(function() {
      snapshot = MWdefinitions.getSnapshot();
    
      MWdefinitionsLoopScheduler.add(importConditions(snapshot));
      MWdefinitionsLoopScheduler.add(MW_defRoutineBegin(snapshot));
      MWdefinitionsLoopScheduler.add(MW_defRoutineEachFrame());
      MWdefinitionsLoopScheduler.add(MW_defRoutineEnd(snapshot));
      MWdefinitionsLoopScheduler.add(MWdefinitionsLoopEndIteration(MWdefinitionsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function MWdefinitionsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(MWdefinitions);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function MWdefinitionsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function ReadingLoopLoopBegin(ReadingLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ReadingLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: stimFile,
      seed: undefined, name: 'ReadingLoop'
    });
    psychoJS.experiment.addLoop(ReadingLoop); // add the loop to the experiment
    currentLoop = ReadingLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    ReadingLoop.forEach(function() {
      snapshot = ReadingLoop.getSnapshot();
    
      ReadingLoopLoopScheduler.add(importConditions(snapshot));
      ReadingLoopLoopScheduler.add(ReadingRoutineBegin(snapshot));
      ReadingLoopLoopScheduler.add(ReadingRoutineEachFrame());
      ReadingLoopLoopScheduler.add(ReadingRoutineEnd(snapshot));
      ReadingLoopLoopScheduler.add(ReadingLoopLoopEndIteration(ReadingLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function ReadingLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ReadingLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function ReadingLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function MW_defRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'MW_def' ---
    t = 0;
    MW_defClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MWdefInstr.setImage(chInstrSlide);
    MWdefInstr_key_resp.keys = undefined;
    MWdefInstr_key_resp.rt = undefined;
    _MWdefInstr_key_resp_allKeys = [];
    // keep track of which components have finished
    MW_defComponents = [];
    MW_defComponents.push(MWdefInstr);
    MW_defComponents.push(MWdefInstr_key_resp);
    
    MW_defComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function MW_defRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'MW_def' ---
    // get current time
    t = MW_defClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MWdefInstr* updates
    if (t >= 0.0 && MWdefInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MWdefInstr.tStart = t;  // (not accounting for frame time here)
      MWdefInstr.frameNStart = frameN;  // exact frame index
      
      MWdefInstr.setAutoDraw(true);
    }

    
    // *MWdefInstr_key_resp* updates
    if (t >= 0.0 && MWdefInstr_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MWdefInstr_key_resp.tStart = t;  // (not accounting for frame time here)
      MWdefInstr_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      MWdefInstr_key_resp.clock.reset();
      MWdefInstr_key_resp.start();
    }

    if (MWdefInstr_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = MWdefInstr_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _MWdefInstr_key_resp_allKeys = _MWdefInstr_key_resp_allKeys.concat(theseKeys);
      if (_MWdefInstr_key_resp_allKeys.length > 0) {
        MWdefInstr_key_resp.keys = _MWdefInstr_key_resp_allKeys[_MWdefInstr_key_resp_allKeys.length - 1].name;  // just the last key pressed
        MWdefInstr_key_resp.rt = _MWdefInstr_key_resp_allKeys[_MWdefInstr_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MW_defComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function MW_defRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'MW_def' ---
    MW_defComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    MWdefInstr_key_resp.stop();
    // the Routine "MW_def" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function IntroExpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'IntroExp' ---
    t = 0;
    IntroExpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    IntroExp_key_resp.keys = undefined;
    IntroExp_key_resp.rt = undefined;
    _IntroExp_key_resp_allKeys = [];
    // keep track of which components have finished
    IntroExpComponents = [];
    IntroExpComponents.push(text);
    IntroExpComponents.push(IntroExp_key_resp);
    
    IntroExpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function IntroExpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'IntroExp' ---
    // get current time
    t = IntroExpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *IntroExp_key_resp* updates
    if (t >= 0.0 && IntroExp_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      IntroExp_key_resp.tStart = t;  // (not accounting for frame time here)
      IntroExp_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { IntroExp_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { IntroExp_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { IntroExp_key_resp.clearEvents(); });
    }

    if (IntroExp_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = IntroExp_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _IntroExp_key_resp_allKeys = _IntroExp_key_resp_allKeys.concat(theseKeys);
      if (_IntroExp_key_resp_allKeys.length > 0) {
        IntroExp_key_resp.keys = _IntroExp_key_resp_allKeys[_IntroExp_key_resp_allKeys.length - 1].name;  // just the last key pressed
        IntroExp_key_resp.rt = _IntroExp_key_resp_allKeys[_IntroExp_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    IntroExpComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function IntroExpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'IntroExp' ---
    IntroExpComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(IntroExp_key_resp.corr, level);
    }
    psychoJS.experiment.addData('IntroExp_key_resp.keys', IntroExp_key_resp.keys);
    if (typeof IntroExp_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('IntroExp_key_resp.rt', IntroExp_key_resp.rt);
        routineTimer.reset();
        }
    
    IntroExp_key_resp.stop();
    // the Routine "IntroExp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function PageSkippingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PageSkipping' ---
    t = 0;
    PageSkippingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_Skip.keys = undefined;
    key_Skip.rt = undefined;
    _key_Skip_allKeys = [];
    // keep track of which components have finished
    PageSkippingComponents = [];
    PageSkippingComponents.push(NoSkipping);
    PageSkippingComponents.push(key_Skip);
    
    PageSkippingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function PageSkippingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PageSkipping' ---
    // get current time
    t = PageSkippingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NoSkipping* updates
    if (t >= 0.0 && NoSkipping.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NoSkipping.tStart = t;  // (not accounting for frame time here)
      NoSkipping.frameNStart = frameN;  // exact frame index
      
      NoSkipping.setAutoDraw(true);
    }

    
    // *key_Skip* updates
    if (t >= 0.0 && key_Skip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_Skip.tStart = t;  // (not accounting for frame time here)
      key_Skip.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_Skip.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_Skip.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_Skip.clearEvents(); });
    }

    if (key_Skip.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_Skip.getKeys({keyList: ['space'], waitRelease: false});
      _key_Skip_allKeys = _key_Skip_allKeys.concat(theseKeys);
      if (_key_Skip_allKeys.length > 0) {
        key_Skip.keys = _key_Skip_allKeys[_key_Skip_allKeys.length - 1].name;  // just the last key pressed
        key_Skip.rt = _key_Skip_allKeys[_key_Skip_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PageSkippingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PageSkippingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PageSkipping' ---
    PageSkippingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_Skip.corr, level);
    }
    psychoJS.experiment.addData('key_Skip.keys', key_Skip.keys);
    if (typeof key_Skip.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_Skip.rt', key_Skip.rt);
        routineTimer.reset();
        }
    
    key_Skip.stop();
    // the Routine "PageSkipping" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ReadingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Reading' ---
    t = 0;
    ReadingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Reading_key_resp.keys = undefined;
    Reading_key_resp.rt = undefined;
    _Reading_key_resp_allKeys = [];
    imagePages.setImage(ChPage);
    // keep track of which components have finished
    ReadingComponents = [];
    ReadingComponents.push(Reading_key_resp);
    ReadingComponents.push(imagePages);
    ReadingComponents.push(PCProbe);
    ReadingComponents.push(SCProbe);
    
    ReadingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function ReadingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Reading' ---
    // get current time
    t = ReadingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_3
    /* Syntax Error: Fix Python code */
    
    // *Reading_key_resp* updates
    if (t >= 0.0 && Reading_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Reading_key_resp.tStart = t;  // (not accounting for frame time here)
      Reading_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Reading_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Reading_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Reading_key_resp.clearEvents(); });
    }

    if (Reading_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Reading_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Reading_key_resp_allKeys = _Reading_key_resp_allKeys.concat(theseKeys);
      if (_Reading_key_resp_allKeys.length > 0) {
        Reading_key_resp.keys = _Reading_key_resp_allKeys[_Reading_key_resp_allKeys.length - 1].name;  // just the last key pressed
        Reading_key_resp.rt = _Reading_key_resp_allKeys[_Reading_key_resp_allKeys.length - 1].rt;
      }
    }
    
    
    // *imagePages* updates
    if (t >= 0.0 && imagePages.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagePages.tStart = t;  // (not accounting for frame time here)
      imagePages.frameNStart = frameN;  // exact frame index
      
      imagePages.setAutoDraw(true);
    }

    
    // *PCProbe* updates
    if (t >= 0.0 && PCProbe.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PCProbe.tStart = t;  // (not accounting for frame time here)
      PCProbe.frameNStart = frameN;  // exact frame index
      
      PCProbe.setAutoDraw(true);
    }

    
    if (PCProbe.status === PsychoJS.Status.STARTED){ // only update if being drawn
      PCProbe.setOpacity(opacityImage1, false);
    }
    
    // *SCProbe* updates
    if (t >= 0.0 && SCProbe.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SCProbe.tStart = t;  // (not accounting for frame time here)
      SCProbe.frameNStart = frameN;  // exact frame index
      
      SCProbe.setAutoDraw(true);
    }

    
    if (SCProbe.status === PsychoJS.Status.STARTED){ // only update if being drawn
      SCProbe.setOpacity(opacityImage2, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ReadingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ReadingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Reading' ---
    ReadingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Reading_key_resp.corr, level);
    }
    psychoJS.experiment.addData('Reading_key_resp.keys', Reading_key_resp.keys);
    if (typeof Reading_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Reading_key_resp.rt', Reading_key_resp.rt);
        }
    
    Reading_key_resp.stop();
    // the Routine "Reading" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function EYE_RECORD_STOPRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EYE_RECORD_STOP' ---
    t = 0;
    EYE_RECORD_STOPClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    EYE_RECORD_STOPComponents = [];
    
    EYE_RECORD_STOPComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function EYE_RECORD_STOPRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EYE_RECORD_STOP' ---
    // get current time
    t = EYE_RECORD_STOPClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EYE_RECORD_STOPComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EYE_RECORD_STOPRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EYE_RECORD_STOP' ---
    EYE_RECORD_STOPComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "EYE_RECORD_STOP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function blankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank' ---
    t = 0;
    blankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    blankComponents = [];
    blankComponents.push(textInterval);
    
    blankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function blankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank' ---
    // get current time
    t = blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textInterval* updates
    if (t >= 0.0 && textInterval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInterval.tStart = t;  // (not accounting for frame time here)
      textInterval.frameNStart = frameN;  // exact frame index
      
      textInterval.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textInterval.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textInterval.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    blankComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function blankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank' ---
    blankComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function EndTextRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndText' ---
    t = 0;
    EndTextClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    EndTextComponents = [];
    EndTextComponents.push(EndExpText);
    EndTextComponents.push(key_resp);
    
    EndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function EndTextRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndText' ---
    // get current time
    t = EndTextClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndExpText* updates
    if (t >= 0.0 && EndExpText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndExpText.tStart = t;  // (not accounting for frame time here)
      EndExpText.frameNStart = frameN;  // exact frame index
      
      EndExpText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (EndExpText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      EndExpText.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndTextComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndTextRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndText' ---
    EndTextComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "EndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
