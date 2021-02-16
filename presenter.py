# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:40:00 2021

@author: Dypole
"""
#####WX IMPORTS#####
import wx
import numpy as np

class Presenter():
    def __init__(self, userInterface, model):
        self.model = model
        self.userInterface = userInterface
        self.makeLinks()
        self.setInitialValues()
    
    def makeLinks(self):
        self.userInterface.powerBox.Bind(wx.EVT_TEXT, self.setPower)
        self.userInterface.beamwaistBox.Bind(wx.EVT_TEXT, self.setBeamwaist)
        self.userInterface.detuningBox.Bind(wx.EVT_TEXT, self.setDetuning)

    def setPower(self, event):
        try:    # prevents quite q few errors when a value is temporarily set to 0
            power = float(event.GetEventObject().GetValue())
            self.model.power = power
            self.model.updateCalculations()
            self.updateUserInterface()
        except:
            pass
        
    def setBeamwaist(self, event):
        try:
            beamwaist = float(event.GetEventObject().GetValue())
            self.model.beamwaist = beamwaist*(10**(-6))
            self.model.updateCalculations()
            self.updateUserInterface()
        except:
            pass
    def setDetuning(self, event):
        try:
            detuning = float(event.GetEventObject().GetValue())
            self.model.detuning = detuning*(2*np.pi*10**9)
            self.model.updateCalculations()
            self.updateUserInterface()
        except:
            pass
    def updateUserInterface(self):
        self.userInterface.trapFrequencyBox.SetValue(str(round(self.model.trapFrequency,2)))
        self.userInterface.trapDepthBox.SetValue(str(round(self.model.trapDepth,2)))
        self.userInterface.add_oscillatorLengthBox.SetValue(str(round(self.model.add_aoh,2)))
        self.userInterface.scatteringBox.SetValue(str(round(self.model.scattering,2)))
        
    def setInitialValues(self):
        self.model.power = 0.1
        self.model.beamwaist = 61.9
        self.model.detuning = 10
        self.userInterface.powerBox.SetValue(str(self.model.power))
        self.userInterface.beamwaistBox.SetValue(str(self.model.beamwaist))
        self.userInterface.detuningBox.SetValue(str(self.model.detuning))
        self.updateUserInterface()