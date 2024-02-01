# -*- coding: utf-8 -*-

import names

def waitUntilObjectReady(obj):
    test.log("Object ready: '%s'" % (obj.text))
    highlightObject(obj, 500)

def main():
    startApplication("appApp_test_synchronization_sections_2_to_6")
    test.compare(str(waitForObject(names.test_Sync_Example_Text).text), "Popup ready")
    
    mouseClick(waitForObject(names.test_Sync_Example_Open_Button, 1000))
    mouseClick(waitForObject(names.test_Sync_Example_Click_to_close_Button, 1000))
    
    test.compare(str(waitForObject(names.test_Sync_Example_Text).text), "Popup closed")

