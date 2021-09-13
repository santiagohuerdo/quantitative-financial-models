# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:39:52 2021

@author: Santiago Huerdo
"""

import importlib
import file_classes
importlib.reload(file_classes)
import file_functions
importlib.reload(file_functions)

#----------------------------------------------------------

# inputs
inputs = file_classes.hedge_input()
inputs.benchmark = 'SPY'
inputs.security = 'AAPL'
inputs.hedge_securities =  ['MCD','KO','PG','WFC']
inputs.delta_portfolio = 10 # mn USD

#----------------------------------------------------------

# computations
hedge = file_classes.hedge_manager(inputs)
hedge.load_betas() # get the betas for portfolio and hedges
hedge.compute(regularisation=0.1) # numerical solution
hedge_delta = hedge.hedge_delta
hedge_beta_usd = hedge.hedge_beta_usd