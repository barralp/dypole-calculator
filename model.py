# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:40:00 2021

@author: Dypole
"""
import numpy as np

class Model():
    def __init__(self):
        self.power = 0 # in W
        self.beamwaist = 0 # in um
        self.detuning = 0 # in GHz
        
        self.trapFrequency = 0  # in kHz
        self.trapDepth = 0  # in kHz
        self.add_aoh = 0    # no units
        self.scattering = 0 # in s-1
        
        self.initConstants()
    
    def initConstants(self):
        self.kappa_red = (1/2)*(1+1/153)
        self.hbar = 1.0545718*10**-34
        self.c = 2.99792458*10**8
        self.polarizability_0 = 1.64877727*10**(-41)
        self.m = 163.929*1.66053906660*10**(-27)
        self.epsilon_0 = 8.85418782*10**(-12)
        self.k_B = 1.38064852*10**(-23)
        self.a_0 = 5.29177210903*10**(-11)
        self.mu_B = 9.274009994*10**(-24)
        self.Gamma_741 = 2*np.pi*1.78*10**3   # in Hz
        self.omega_741 = 2*np.pi*self.c/(741*10**(-9))
        self.Gamma_421 = 2*np.pi*32.2*10**6
        self.omega_421 = 2*np.pi*self.c/(421.172*10**(-9))
        self.delta_421 = self.omega_421 - self.omega_741
        self.omega_405 = 2*np.pi*self.c/(404.597*10**(-9))
        self.omega_419 = 2*np.pi*self.c/(418.682*10**(-9))
        self.omega_419_bis = 2*np.pi*self.c/(419.484*10**(-9))
        self.Gamma_405 = 1.92*10**8
        self.Gamma_419 = 1.26*10**8
        self.Gamma_419_bis = 8.8*10**7
        self.kappa_blue = (1/2)*((1+1/153)+(1/9)*(self.Gamma_419/self.Gamma_421)**2
                                 *(self.omega_421/self.omega_419)**6
                                 +(1/9)*(self.Gamma_419_bis/self.Gamma_421)**2
                                 *(self.omega_421/self.omega_419_bis)**6
                                 +(15/17)*(self.Gamma_405/self.Gamma_421)**2
                                 *(self.omega_421/self.omega_405)**6)
        self.polarizability_prefactor = 3*np.pi*self.kappa_red*self.epsilon_0*self.c**3*self.Gamma_741/(self.omega_741**3)
        self.add =self.m/2 * (1/(self.epsilon_0*self.c**2))/(4*np.pi)*(10*self.mu_B/self.hbar)**2
        self.gamma_blue_prefactor = 3*self.kappa_blue*self.c**2*self.Gamma_421**2/(self.hbar*self.delta_421**2*self.omega_421**3)*(421/741)**3
        self.gamma_red_prefactor = 3*self.kappa_red*self.c**2*self.Gamma_741**2/(self.hbar*self.omega_741**3)
    def updateCalculations(self):
        self.updateTrapFrequency()
        self.updateTrapDepth()
        self.updateAdd_aoh()
        self.updateScattering()
    
    def updateTrapFrequency(self):
        self.polarizability = 220*self.polarizability_0-self.polarizability_prefactor/self.detuning
        omega_z = np.sqrt(np.abs(32*np.pi*self.polarizability*self.power/((741*10**(-9))**2*self.beamwaist**2*self.epsilon_0*self.c*self.m)))
        self.trapFrequency = omega_z/(2*np.pi*10**3)
    
    def updateTrapDepth(self):
        omega_z = self.trapFrequency*(2*np.pi*10**3)
        self.trapDepth = self.m**2*omega_z**2/(self.hbar**2*(self.omega_741/self.c)**4)
    
    def updateAdd_aoh(self):
        omega_z = self.trapFrequency*(2*np.pi*10**3)
        oscillator_length = np.sqrt(self.hbar/(self.m/2*omega_z))
        self.add_aoh = self.add/oscillator_length
    
    def updateScattering(self):
        gamma_blue = self.gamma_blue_prefactor*self.power/self.beamwaist**2
        gamma_red = self.gamma_red_prefactor/(self.detuning**2)*self.power/self.beamwaist**2
        self.scattering = gamma_blue + gamma_red