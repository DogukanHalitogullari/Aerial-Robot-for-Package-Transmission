#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 23:54:43 2022

@author: dogukan
"""

import tkinter as tk
from tkintermapview import TkinterMapView
import time
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

def createWindow():
    window = tk.Tk()
    window.title("Drone Resc");
    frame = tk.Frame(master=window, width=1280, height=719, bg=rgb_hack((30, 30, 30)))
    frame.pack()
    return frame, window

def setMap(frame):
    # create map widget

    current_map = TkinterMapView(frame, width=320, height=240, corner_radius=0)
    current_map.pack(fill="both", expand=True)
    current_map.set_position(41.21621503633734, 29.02960847941508)
    current_map.set_zoom(16)
    current_map.set_marker(41.21621503633734, 29.02960847941508, text="Current Location")
    current_map.place(x=840, y=80)
    
    requested_map = TkinterMapView(frame, width=320, height=240, corner_radius=0)
    requested_map.pack(fill="both", expand=True)
    requested_map.set_position(41.21621503633734, 29.02960847941508)
    requested_map.set_zoom(16)
    requested_map.set_marker(41.21621503633734, 29.02960847941508, text="SOS Location")
    requested_map.place(x=840, y=400)

def setMissionLabel(frame):
    requestedLabel = tk.Label(master=frame, 
                              text="Requested Package Type: ", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 20 bold",)
    requestedLabel.place(x=80, y=70)
    
    requestedLabel2 = tk.Label(master=frame, 
                              text="First Aid Kit", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 0, 0)),
                              font = "Verdana 20",)
    requestedLabel2.place(x=370, y=70)
    
    step = tk.Label(master=frame, 
                              text="STEP", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 20 bold",)
    step.place(x=120, y=140)
    
    situation = tk.Label(master=frame, 
                              text="SITUATION", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 20 bold",)
    situation.place(x=480, y=140)
    
def setStepLabel(frame, situationArray):
    #STEP 1
    num1 = tk.Label(master=frame, 
                              text="1.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num1.place(x=80, y=180)
    
    takeOff = tk.Label(master=frame, 
                              text="Take OFF", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    takeOff.place(x=120, y=180)
    
    takeOffSituation = tk.Label(master=frame, 
                              text=situationArray[0], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    takeOffSituation.place(x=480, y=180)

    
    #STEP 2
    num2 = tk.Label(master=frame, 
                              text="2.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num2.place(x=80, y=210)
    
    goToPackageCenter = tk.Label(master=frame, 
                              text="Go To Package Center", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToPackageCenter.place(x=120, y=210)
    
    goToPackageCenterSituation = tk.Label(master=frame, 
                              text=situationArray[1], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToPackageCenterSituation.place(x=480, y=210)
    
    #STEP 3
    num3 = tk.Label(master=frame, 
                              text="3.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num3.place(x=80, y=240)
    
    loadingPackage = tk.Label(master=frame, 
                              text="Loading Package", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    loadingPackage.place(x=120, y=240)
    
    loadingPackageSituation = tk.Label(master=frame, 
                              text=situationArray[2], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    loadingPackageSituation.place(x=480, y=240)
    
    #STEP 4
    num2 = tk.Label(master=frame, 
                              text="4.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num2.place(x=80, y=270)
    
    goToDestination = tk.Label(master=frame, 
                              text="Go To Destination", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToDestination.place(x=120, y=270)
    
    goToDestinationSituation = tk.Label(master=frame, 
                              text=situationArray[3], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToDestinationSituation.place(x=480, y=270)
    
    #STEP 5
    num5= tk.Label(master=frame, 
                              text="5.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num5.place(x=80, y=300)
    
    deliveryPackage = tk.Label(master=frame, 
                              text="Delivery Package", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    deliveryPackage.place(x=120, y=300)
    
    deliveryPackageSituation = tk.Label(master=frame, 
                              text=situationArray[4], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    deliveryPackageSituation.place(x=480, y=300)

    #STEP 6
    num6 = tk.Label(master=frame, 
                              text="6.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num6.place(x=80, y=330)
    
    goToHome = tk.Label(master=frame, 
                              text="Go To Home", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToHome.place(x=120, y=330)
    
    goToHomeSituation = tk.Label(master=frame, 
                              text=situationArray[5], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    goToHomeSituation.place(x=480, y=330)
    
    #STEP 7
    num7 = tk.Label(master=frame, 
                              text="7.", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16 bold",)
    num7.place(x=80, y=360)
    
    land = tk.Label(master=frame, 
                              text="Land", 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    land.place(x=120, y=360)
    
    landSituation = tk.Label(master=frame, 
                              text=situationArray[6], 
                              bg=rgb_hack((30, 30, 30)), 
                              fg=rgb_hack((255, 255, 255)),
                              font = "Verdana 16",)
    landSituation.place(x=480, y=360)
    
    stepSituationArray = [takeOffSituation, goToPackageCenterSituation, loadingPackageSituation, 
                          goToDestinationSituation, deliveryPackageSituation, goToHomeSituation, landSituation]
    return stepSituationArray
    
def updateLabel(stepSituationArray, situatıonArray):
    for i in range(6):
        stepSituationArray[i].config(text = situatıonArray[i])

def main(situatıonArray, stepSituationArray, countSituation):
    print("ok****")
    situatıonArray[countSituation] = "COMPLETED"
    countSituation += 1
    situatıonArray[countSituation] = "IN PROGRESS"
    updateLabel(stepSituationArray, situatıonArray)
    
        
situatıonArray = ["WAITING", "WAITING", "WAITING", "WAITING", "WAITING", "WAITING", "WAITING"]   
countSituation = 0  
frame, window = createWindow()
setMap(frame)
setMissionLabel(frame)
stepSituationArray = setStepLabel(frame, situatıonArray)
window.mainloop()
