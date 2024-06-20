#!/usr/bin/env python3
import numpy as np

for state in ['Reference', 'Solution']:
    print('=== {} ==='.format(state))

    for conc, Nmolecules in zip(['0.00','2.00','6.00'], [0,378,1472]):
        if state == 'Solution':
            V = np.loadtxt('PEG36mer/'+conc+'/Solute/output.dat', usecols=(4), skiprows=1, unpack=True)
        elif state == 'Reference':
            V = np.loadtxt('References/'+conc+'/output.dat', usecols=(4), skiprows=1, unpack=True)
        Na = 6.02214076*1e23 # [1/mol]
        nm3_to_l = 1e-24
        molarity = Nmolecules / (V.mean() * Na * nm3_to_l)
    
        print('The urea concentration is: {:.2f} given {} urea molecules'.format(molarity, Nmolecules))
    print('')
