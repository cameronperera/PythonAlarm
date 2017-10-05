#!/usr/bin/python3
from datetime import datetime
import time
import os
import random
import sys
import numpy
import json
from tkinter import *
import winsound


punch = []
saturday = 5

music = 'Various-04.wav'
windowText = 'Punch!'
windowImage = 'vader_business.gif'

def alarmWindow():
    root = Tk()
    root.title('Alarm Clock')
    root.geometry('920x640')
    app = Frame(root)
    app.grid()
    filename = PhotoImage(file = windowImage)
    background_label = Label(app, image=filename)
    background_label.grid()
    winsound.PlaySound(music, winsound.SND_ALIAS | winsound.SND_ASYNC)
    text = Canvas(app, width=150, height=75)
    text.create_text(75, 35, font='Times 32 bold', text= windowText)
    text.grid(row=0, column=0, sticky='nw')

    root.mainloop()

def convertToList(punch):
    intPunch = punch.split(':')
    intList = list(map(int, intPunch))
    return intList

def currentTimeArray():
    currentTimeHour = datetime.now().hour
    currentTimeMinute = datetime.now().minute
    currentTimeArray = [currentTimeHour, currentTimeMinute]
    return currentTimeArray

def substractPunchFromCurrent(currentTime, punchTime):
    currentTime = numpy.array(currentTime)
    punchTime = numpy.array(punchTime)
    subtractedTime = punchTime - currentTime
    if subtractedTime[0] <= 0:
        subtractedTime = subtractedTime + 24
    return subtractedTime

def secondsToSleep(subtractedTime):
    secondsSleep = (subtractedTime[0]*3600 + subtractedTime[1]*60)
    convertSleepToInt = int(secondsSleep)
    return convertSleepToInt

def convertPMTimeTo24Format(punch):
    punch[0] = punch[0] + 12
    return punch

def checkIfFileExist():
    if os.path.isfile('punchTimes.txt'):
        with open('punchTimes.txt') as jsonFile:
            data = json.load(jsonFile)
        return data
    else:
        noFile = 'No stored punch times, please create new punch times.'
        return noFile

def removeTimeChar(inputPunch, char):
    for i in char:
        inputPunch = inputPunch.replace(i, '')
    return inputPunch

def amPunchConversion(amPunch):
    amPunch = removeTimeChar(amPunch, ' am')
    amPunch = convertToList(amPunch)
    return amPunch

def pmPunchConversion(pmPunch):
    pmPunch = removeTimeChar(pmPunch, ' pm')
    pmPunch = convertToList(pmPunch)
    return pmPunch

def noonConversion(noon):
    noonPunch = noon
    if noonPunch == '12:00pm':
        noonPunch = removeTimeChar(noonPunch, ' pm')
        noonPunch = convertToList(noonPunch)
    return noonPunch

def collectNewPunchTimes(punches):
    inputPunchStr = punches
    if 'am' in inputPunchStr:
        inputPunch = amPunchConversion(inputPunchStr)
        punch.append(inputPunch)
    elif 'pm' in inputPunchStr:
        if '12' in inputPunchStr:
            inputPunch = noonConversion(inputPunchStr)
        else:
            inputPunch = pmPunchConversion(inputPunchStr)
            inputPunch = convertPMTimeTo24Format(inputPunch)
        punch.append(inputPunch)

def putProgramToSleep(secondsToSleep):
    time.sleep(2)
    return True

def getStoredPunches():
    fileData = openAndReadFile('punchTimes.txt')
    return fileData

def openAndReadFile(fileName):
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
    return data

def writeToFile(fileName, punchTimes):
    with open(fileName, 'w') as jsonfile:
        json.dump(punchTimes, jsonfile)

def start():
    whileVar = True
    global punch
    while whileVar == True:
        fileCheck = input('Would you like to enter "new" punch times or use "stored"? ')
        if fileCheck == 'new':
            while whileVar == True:
                inputPunchStr = input('Please enter one punch time (ex. 8:30am or 5:00pm) or end to stop: ')
                if inputPunchStr == 'end':
                    whileVar = False
                    return whileVar
                else:
                    collectNewPunchTimes(inputPunchStr)

                writeToFile('punchTimes.txt', punch)
            punch = getStoredPunches()
            # return punch
        elif fileCheck == 'stored':
            punch = getStoredPunches()
            # return punch
            whileVar = False
            return whileVar
        else:
            print('Plese enter "new" or "stored".')

def selectPunchTime(punch):
    currentTime = currentTimeArray()
    punchInitial = punch
    for b in punchInitial:
        if currentTime < b:
            selectedPunch = b
            break
        else:
            selectedPunch = punchInitial[0]
    return selectedPunch

def noonConversion(noon):
    noonPunch = noon
    noonPunch = removeTimeChar(noonPunch, ' pm')
    noonPunch = convertToList(noonPunch)
    return noonPunch
