# -*- coding: utf-8 -*-

import names

def handleDialogOpenedEvent(dialog):
    test.log("Dialog opened: '%s'" % (dialog.windowTitle))
    
def handleQMouseEvent(obj):
    test.log("Mouse event occurred on: '%s'" % (obj.objectName))
    
def handleCheckBox2MouseEvent(obj):
    test.log("Mouse event on checkbox2 occurred: '%s'" % (obj.objectName))

def main():
    startApplication("App_test_synchronization_section7")
    
    installEventHandler("DialogOpened", "handleDialogOpenedEvent")
    installEventHandler("QCheckBox", "QMouseEvent",  "handleQMouseEvent")
    
    checkBox2 = waitForObject(names.mainWindow_checkBox2_QCheckBox)
    installEventHandler(checkBox2, "QMouseEvent",  "handleCheckBox2MouseEvent")
    
    clickButton(waitForObject(names.mainWindow_openDialogBtn_QPushButton))
    clickButton(waitForObject(names.dialog_closeDialogBtn_QPushButton))
    clickButton(waitForObject(names.mainWindow_checkBox1_QCheckBox))
    clickButton(waitForObject(names.mainWindow_checkBox2_QCheckBox))
    snooze(1)
