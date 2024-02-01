# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appApp_test_synchronization_sections_2_to_6")
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup ready")
    
    mouseClick(names.test_Sync_Example_Open_Button)
    
    obj = waitForObjectExists(names.test_Sync_Example_Text)
    if waitFor("str(obj.text) == 'Popup opened'", 5000):
        mouseClick(names.test_Sync_Example_Click_to_close_Button)
    else:
        test.log("waitFor() timeout reached")
    
    test.compare(str(findObject(names.test_Sync_Example_Text).text), "Popup closed")
