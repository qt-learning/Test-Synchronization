# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appApp_test_synchronization_sections_2_to_6")
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup ready")
    
    mouseClick(waitForImage("OpenButton",{ "tolerant": True, "threshold": 99.999 },waitForObjectExists(names.test_Sync_Example_QQuickWindowQmlImpl)))
    mouseClick(waitForImage("CloseButton",{ "tolerant": True, "threshold": 99.999 },waitForObjectExists(names.test_Sync_Example_QQuickWindowQmlImpl)))
    
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup closed")
