# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appApp_test_synchronization_sections_2_to_6")
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup ready")
    
    mouseClick(waitForOcrText("Open"))
    mouseClick(waitForOcrText("Click to close"))
    
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup closed")
