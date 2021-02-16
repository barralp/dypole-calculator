# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:40:00 2021

@author: Dypole
"""
#####WX IMPORTS#####
import wx

class DypoleCalculatorUI(wx.Frame):
    def __init__(self, parent, title):
        self.app = wx.App()
        super(DypoleCalculatorUI, self).__init__(parent, title = title, size=(500, 500))
        self.start()
        
    def start(self):
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self, id = -1, size = (1,1))
        # self.SetIcon(wx.Icon('./icons/wxwin.ico', wx.BITMAP_TYPE_ICO))
        self.mainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.configurationBox = wx.StaticBox(self.panel, label = "Laser parameters")
        self.configurationBoxSizer = wx.StaticBoxSizer(self.configurationBox, wx.VERTICAL)
        self.setConfigurationBox()
        self.calculationBox = wx.StaticBox(self.panel, label = "Calculation results")
        self.calculationBoxSizer = wx.StaticBoxSizer(self.calculationBox, wx.VERTICAL)
        self.setCalculationBox()
        self.mainBoxSizer.Add(self.configurationBoxSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.mainBoxSizer.Add(self.calculationBoxSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.mainBoxSizer)
    
    def setConfigurationBox(self):
        self.powerBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.powerText = wx.StaticText(self.panel, label = "Laser power   ")
        self.powerBox = wx.TextCtrl(self.panel, value = "0")
        self.powerTextUnit = wx.StaticText(self.panel, label = " W (of linear light on -8 state)")
        self.powerBoxLine.Add(self.powerText)
        self.powerBoxLine.Add(self.powerBox)
        self.powerBoxLine.Add(self.powerTextUnit)
        self.configurationBoxSizer.Add(self.powerBoxLine, wx.ALL)
        
        self.beamwaistBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.beamwaistText = wx.StaticText(self.panel, label = "Beamwaist   ")
        self.beamwaistBox = wx.TextCtrl(self.panel, value = "0")
        self.beamwaistTextUnit = wx.StaticText(self.panel, label = " um")
        self.beamwaistBoxLine.Add(self.beamwaistText)
        self.beamwaistBoxLine.Add(self.beamwaistBox)
        self.beamwaistBoxLine.Add(self.beamwaistTextUnit)
        self.configurationBoxSizer.Add(self.beamwaistBoxLine, wx.ALL)
        
        self.detuningBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.detuningText = wx.StaticText(self.panel, label = "Detuning   ")
        self.detuningBox = wx.TextCtrl(self.panel, value = "0")
        self.detuningTextUnit = wx.StaticText(self.panel, label = r" (2\pi) GHz")
        self.detuningBoxLine.Add(self.detuningText)
        self.detuningBoxLine.Add(self.detuningBox)
        self.detuningBoxLine.Add(self.detuningTextUnit)
        self.configurationBoxSizer.Add(self.detuningBoxLine, wx.ALL)
        
    def setCalculationBox(self):
        self.trapFrequencyBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.trapFrequencyText = wx.StaticText(self.panel, label = "Trap frequency   ")
        self.trapFrequencyBox = wx.TextCtrl(self.panel, value = "0")
        self.trapFrequencyTextUnit = wx.StaticText(self.panel, label = " (2pi) kHz")
        self.trapFrequencyBoxLine.Add(self.trapFrequencyText)
        self.trapFrequencyBoxLine.Add(self.trapFrequencyBox)
        self.trapFrequencyBoxLine.Add(self.trapFrequencyTextUnit)
        self.calculationBoxSizer.Add(self.trapFrequencyBoxLine, wx.ALL)
        
        self.trapDepthBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.trapDepthText = wx.StaticText(self.panel, label = "Trap depth   ")
        self.trapDepthBox = wx.TextCtrl(self.panel, value = "0")
        self.trapDepthTextUnit = wx.StaticText(self.panel, label = " (2pi) kHz")
        self.trapDepthBoxLine.Add(self.trapDepthText)
        self.trapDepthBoxLine.Add(self.trapDepthBox)
        self.trapDepthBoxLine.Add(self.trapDepthTextUnit)
        self.calculationBoxSizer.Add(self.trapDepthBoxLine, wx.ALL)
        
        self.add_oscillatorLengthBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.add_oscillatorLengthText = wx.StaticText(self.panel, label = "a_dd / a_oh   ")
        self.add_oscillatorLengthBox = wx.TextCtrl(self.panel, value = "0")
        self.add_oscillatorLengthTextUnit = wx.StaticText(self.panel, label = " (transition when > 0.34) \n check the weirdiness with m/2")
        self.add_oscillatorLengthBoxLine.Add(self.add_oscillatorLengthText)
        self.add_oscillatorLengthBoxLine.Add(self.add_oscillatorLengthBox)
        self.add_oscillatorLengthBoxLine.Add(self.add_oscillatorLengthTextUnit)
        self.calculationBoxSizer.Add(self.add_oscillatorLengthBoxLine, wx.ALL)
        
        self.scatteringBoxLine = wx.BoxSizer(wx.HORIZONTAL)
        self.scatteringText = wx.StaticText(self.panel, label = "Scattering (as red)   ")
        self.scatteringBox = wx.TextCtrl(self.panel, value = "0")
        self.scatteringTextUnit = wx.StaticText(self.panel, label = r" s^{-1}")
        self.scatteringBoxLine.Add(self.scatteringText)
        self.scatteringBoxLine.Add(self.scatteringBox)
        self.scatteringBoxLine.Add(self.scatteringTextUnit)
        self.calculationBoxSizer.Add(self.scatteringBoxLine, wx.ALL)

if __name__ == '__main__':
    ui = ImageUI(None, title='Lattice Calculator')
    ui.app.MainLoop()