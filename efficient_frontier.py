# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:55:01 2021

@author: Santiago Huerdo
"""

# import our own files and reload
import importlib
import file_classes
importlib.reload(file_classes)
import file_functions
importlib.reload(file_functions)

#----------------------------------------------------------

# rics = ['BARC.L','BBVA.MC','BNP.PA','CBK.DE','CSGN.SW','DBK.DE',\
#         'GLE.PA','HSBA.L','SAN.MC','UBSG.SW']
rics = ['BP.L','ENI.MI','RDSa.AS','RDSa.L','EQNR.OL','REP.MC','XOP']
# rics = ['SGRE.MC','VWS.CO','ORSTED.CO','FSLR','NEE']
# rics = ['XLF','XLK', 'XLY', 'MCD','BABA', 'WFC']
# rics = ['^FTSE','^GDAXI','^FCHI','^STOXX50E']

#----------------------------------------------------------

# input params
notional = 300 # mnUSD
target_return = 0.015 # 0.01 0.04 0.36 0.6 0.05 0.015
include_min_variance=False

#----------------------------------------------------------

# efficient frontier
dict_portfolios = file_functions.compute_efficient_frontier(rics, notional, target_return, include_min_variance)

