# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:42:34 2021

@author: Santiago Huerdo
"""

import importlib
import file_classes
importlib.reload(file_classes)
import file_functions
importlib.reload(file_functions)

#----------------------------------------------------------

inputs = file_classes.distribution_input()

# inputs
inputs.data_type = 'real'       #   real or simulation
inputs.variable_name = 'SPY'   #   ticker name or simulation: normal | student | exponential | chi-square | uniform
inputs.degrees_freedom = 9      #   only for chi-square
inputs.nb_sims = 10**6          #   number of simulations

#----------------------------------------------------------

# compute and plot
dm = file_classes.distribution_manager(inputs)   #   initialise constructor
dm.load_timeseries()                             #   get the timeseries
dm.compute()                                     #   compute returns and all different risk metrics
dm.plot_histogram()                              #   plot histogram
print(dm)                                        #   write all data in console