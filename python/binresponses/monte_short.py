from time import clock
from math import *
from Numeric import *
from presto import *
from miscutils import *
from Statistics import *
from cPickle import *
import Pgplot

# Some admin variables
showplots = 0         # True or false
showsumplots = 0      # True or false
debugout = 0          # True or false
outfiledir = '/home/ransom'
outfilenm = 'cpickle'
pmass = 1.35                                 # Pulsar mass in solar masses
cmass = {'WD': 0.3, 'NS': 1.35, 'BH': 10.0}  # Companion masses to use
ecc = {'WD': 0.0, 'NS': 0.6, 'BH': 0.6}      # Eccentricities to use
orbsperpt = {'WD': 20, 'NS': 20, 'BH': 20}   # # of orbits to avg per pt
ppsr = [0.002, 0.02, 0.2, 2.0]               # Pulsar periods to test

# Simulation parameters
ctype = 'WD'             # The type of binary companion: 'WD', 'NS', or 'BH'
Pb = 7200.0              # Orbital period in seconds
dt = 0.0001              # The duration of each data sample (s)
searchtype = 'short'     # One of 'ffdot', 'sideband', 'short'
Tfft = 60.0              # Length of FFTs in seconds (must evenly divide Pb)
numbetween = 2

##################################################
# You shouldn't need to edit anyting below here. #
##################################################

outfilenm = (outfiledir+'/'+outfilenm+
             '_'+searchtype+`Tfft`+'_'+ctype+'.out')

def psrparams_from_list(pplist):
    psr = psrparams()
    psr.p = pplist[0]
    psr.orb.p = pplist[1]
    psr.orb.x = pplist[2]
    psr.orb.e = pplist[3]
    psr.orb.w = pplist[4]
    psr.orb.t = pplist[5]
    return psr

####################################################################

# Open a file to save each orbit calculation
file = open(outfilenm,'w')

numffts = int(Pb / Tfft)
TbyPb = (arange(numffts, typecode='d')+1.0)/numffts
xb = asini_c(Pb, mass_funct2(pmass, cmass[ctype], pi / 3.0))

for pp in ppsr:
    pows = zeros(orbsperpt[ctype], 'd')
    stim = clock()
    numbins = 0
    for ct in range(orbsperpt[ctype]):
        wb = ct * 180.0 / orbsperpt[ctype]
        psr = psrparams_from_list([pp, Pb, xb, ecc[ctype], wb, 0.0])
        tmpnumbins = 2 * numbetween * bin_resp_halfwidth(psr.p, Pb, psr.orb)
        if tmpnumbins > numbins:  numbins = tmpnumbins
    # Powers averaged over orb.t as a function of orb.w
    pwrs_w = zeros((orbsperpt[ctype], numbins), Float32)
    # Powers averaged over orb.w as a function of orb.t
    pwrs_t = zeros((numffts, numbins), Float32)
    for ct in range(orbsperpt[ctype]):
        wb = ct * 180.0 / orbsperpt[ctype]
        if debugout:  print 'wb = '+`wb`
        psr = psrparams_from_list([pp, Pb, xb, ecc[ctype], wb, 0.0])
        for i in range(numffts):
            psr.orb.t = i * Tfft
            tmppwrs = spectralpower(gen_bin_response(0.0, numbetween,
                                                     psr.p, Tfft,
                                                     psr.orb, numbins))
            if debugout:  print '     tb = '+`psr.orb.t`+'  Max pow = '+\
               `max(tmppwrs)`
            if showplots:
                Pgplot.plotxy(tmppwrs)
                Pgplot.closeplot()
            pwrs_w[ct] = pwrs_w[ct] + tmppwrs
            pwrs_t[i] = pwrs_t[i] + tmppwrs
        if showsumplots:
            Pgplot.plotxy(pwrs_w[ct], title='power(w) averaged over orb.t')
            Pgplot.closeplot()
    for i in range(numffts):
        if showsumplots:
            Pgplot.plotxy(pwrs_t[i], title='power(t) averaged over orb.w')
            Pgplot.closeplot()
    pwrs_w = pwrs_w / numffts
    pwrs_t = pwrs_t / orbsperpt[ctype]
    if showsumplots:
        Pgplot.plotxy(add.reduce(pwrs_w), title='power(w) averaged over orb.t')
        Pgplot.closeplot()
        Pgplot.plotxy(add.reduce(pwrs_t), title='power(t) averaged over orb.w')
        Pgplot.closeplot()
    tim = clock() - stim
    if debugout:
        print 'Time for this point was ',tim, ' s.'
    dump(pwrs_w, file)
    dump(pwrs_t, file)
file.close()