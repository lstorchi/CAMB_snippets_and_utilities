import sys, platform, os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import camb
from camb import model, initialpower


if __name__ == "__main__":
    print('Python version: %s\n' % sys.version)
    print('CAMB version: %s\n' % camb.__version__)
    print('Using CAMB installed at %s\n' % os.path.dirname(camb.__file__))
    print('Using matplotlib version: %s\n' % matplotlib.__version__)
    print('Using numpy version: %s\n' % np.__version__)
    print('Using platform: %s\n' % platform.platform())
    print('Using Python version: %s\n' % platform.python_version())
    #print(dir(camb))

    pars = camb.read_ini('high_acc.ini')
    camb.write_ini(pars, "ttest.ini")
    exit()


    #Set up a new set of parameters for CAMB
    #The defaults give one massive neutrino and helium set using BBN consistency
    pars = camb.set_params(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,  
                           As=2e-9, ns=0.965, halofit_version='mead2020', lmax=11000)

    pars.set_accuracy(AccuracyBoost=2, lSampleBoost=2.0, lAccuracyBoost=2.0, DoLateRadTruncation=False) 

    pars.set_matter_power(kmax=10.0, k_per_logint=130, nonlinear=True)

    pars.set_for_lmax(11000, lens_potential_accuracy=8, lens_margin=2050)

    #Non-Linear spectra (Halofit)
    pars.NonLinear = model.NonLinear_both

    camb.write_ini(pars, "ttest.ini")

    # get results and compute 
    results = camb.get_results(pars)
    results.calc_power_spectra(pars)

    # parameters can also be read from text .ini files, for example this sets up a best-fit 
    # Planck 2018 LCDM cosmology (base_plikHM_TTTEEE_lowl_lowE_lensing). 
    # [Use planck_2018_acc.ini if you need high-ell and/or accurate BB and CMB lensng spectra at beyond-Planck accuracy]
    #pars = camb.read_ini('high_acc.ini')

    # view parameter objects using print(), or use pickle or repr to save and restore
    #print(pars)
