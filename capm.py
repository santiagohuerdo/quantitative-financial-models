# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:07:45 2021

@author: Santiago Huerdo
"""

import importlib
import file_classes
importlib.reload(file_classes)
import file_functions
importlib.reload(file_functions)

#----------------------------------------------------------

# inputs
benchmark = 'SPY' # variable x
security = 'GOOGL' # variable y

#----------------------------------------------------------

# compute and plot
capm = file_classes.capm_manager(benchmark, security)
capm.load_timeseries()
capm.plot_timeseries()
capm.compute()
capm.plot_linear_regression()
print(capm)