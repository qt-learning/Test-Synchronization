# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appApp_test_synchronization_sections_2_to_6")
    test.compare(str(waitForObject(names.test_Sync_Example_Text, 1000).text), "Popup ready")
    
    mouseClick(waitForObject(names.test_Sync_Example_Open_Button, 1000))
    mouseClick(waitForObject(names.test_Sync_Example_Click_to_close_Button, 2000))
    
    test.compare(str(waitForObject(names.test_Sync_Example_Text, 1000).text), "Popup closed")
