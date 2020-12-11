import torch
import numpy as np

##############################################
##Stochastic differential equation functions##
##############################################

def arrhenius_temp_dep(parameter, temp, Ea, temp_ref):
    '''
    For a parameter with Arrhenius temperature dependence, returns the transformed parameter value.
    0.008314 is the gas constant. Temperatures are in K.
    '''
    decayed_parameter = parameter * np.exp(-Ea / 0.008314 * (1 / temp - 1 / temp_ref))
    return decayed_parameter

def linear_temp_dep(parameter, temp, Q, temp_ref):
    '''
    For a parameter with linear temperature dependence, returns the transformed parameter value.
    Q is the slope of the temperature dependence.
    Temperatures are in K.
    '''
    modified_parameter = parameter - Q * (temp - temp_ref)
    return modified_parameter

def litter_input_vector(I_S, I_D, SDE_system):
    '''
    Returns vector representing carbon (C) input from decomposing plant litter into SCON or SAWB soil systems.
    I_S is the litter input into the system soil organic C (SOC) pool.
    I_D is the litter input into the system dissolved organic C (DOC) pool.
    Only SCON or SAWB system supported at this point.
    '''
    SDE_system = upper(SDE_system)
    if SDE_system == 'SCON':
        state_var = 3
        return li = torch.reshape(torch.FloatTensor([I_S, I_D, 0]), [state_var, 1])
    elif SDE_system == 'SAWB':
        state_var = 4
        return li = torch.reshape(torch.FloatTensor[I_S, I_D, 0, 0], [state_var, 1])
    else:
        raise Exception('No eligible model provided. "SCON" and "SAWB" only for now.')