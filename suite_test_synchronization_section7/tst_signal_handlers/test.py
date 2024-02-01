# -*- coding: utf-8 -*-

import names

def handleStateChangedSignal(obj, state):
    test.log("State changed signal occurred on: '%s'" % (obj.objectName))
    test.log("State changed to: '%s'" % (state))
    
def handleCustomSignal(obj, message):
    test.log("Custom signal occurred, message received: '%s'" % message)

def main():
    startApplication("App_test_synchronization_section7")
    
    checkBox2 = waitForObject(names.mainWindow_checkBox2_QCheckBox)
    installSignalHandler(checkBox2, "stateChanged(int)", "handleStateChangedSignal")
    
    mainWindow = waitForObject(names.mainWindow_MainWindow)
    installSignalHandler(mainWindow, "customSignal(QString)", "handleCustomSignal")
    
    clickButton(waitForObject(names.mainWindow_checkBox1_QCheckBox))
    clickButton(waitForObject(names.mainWindow_checkBox2_QCheckBox))
    snooze(1)
