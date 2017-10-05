#!/usr/bin/python3
import alarm_test
from colorama import init, Fore, Style
import unittest
import numpy
init(autoreset=True)

punch1 = "8:30"
punch2 = "11:30"
punch3 = "12:0"
punch4 = "17:0"

punch = [[8, 30], [11, 0], [11, 30], [17, 0]]


class TestAlarm(unittest.TestCase):


    def test_start(self):
        start = alarm_test.start()
        self.assertEqual(start, False)

    def test_convertList(self):
        intPunch = alarm_test.convertToList(punch1)
        self.assertIsInstance(intPunch, list)
        return intPunch

    def test_CurrentTimeArray(self):
        currentTime = alarm_test.currentTimeArray()
        self.assertIsInstance(currentTime, list)
        return currentTime

    def test_SubtractPunchTimeFromCurrentTime(self):
        subtractedTime = alarm_test.substractPunchFromCurrent(
            TestAlarm.test_CurrentTimeArray(self),
            TestAlarm.test_selectPunchTime(self))
        self.assertIsInstance(subtractedTime, numpy.ndarray)
        return subtractedTime

    def test_secondsToSleep(self):
        sleepSeconds = alarm_test.secondsToSleep(
            TestAlarm.test_SubtractPunchTimeFromCurrentTime(self))
        self.assertIsInstance(sleepSeconds, int)
        return sleepSeconds

    def test_convertPMTimeTo24Format(self):
        militaryFormat = alarm_test.convertPMTimeTo24Format(
            TestAlarm.test_convertList(self))
        self.assertEqual(militaryFormat[0], 20)

    def test_selectPunchTime(self):
        selectedPunch = alarm_test.selectPunchTime(punch)
        self.assertEqual(selectedPunch, punch[1])
        return selectedPunch

    def test_checkIfFileExist(self):
        fileExistance = alarm_test.checkIfFileExist()
        self.assertIsInstance(fileExistance, list)

    def test_putProgramToSleep(self):
        goToSleep = alarm_test.putProgramToSleep(TestAlarm.test_secondsToSleep(self))
        self.assertEqual(goToSleep, True)

    def test_openAlarmWindow(self):
        window = alarm_test.alarmWindow()

    def test_noonConversion(self):
        noon = alarm_test.noonConversion('12:26pm')
        self.assertEqual(noon, [12, 26])



if __name__ == '__main__':
    unittest.main()
