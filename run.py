# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:23:24 2021

@author: Dypole
"""

import userInterface
import presenter
import model

theUI = userInterface.DypoleCalculatorUI(None, title='Lattice Calculator')
theModel = model.Model()
presenter = presenter.Presenter(theUI, theModel)
theUI.app.MainLoop()