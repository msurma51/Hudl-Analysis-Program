from DataImport import DATA
from DataImport import opponent
from DataImport import field
from FZGenerator import *
from Functions import *

print('Run/Pass by D&D by Field Zone')

for zone in FZ:
    print('\n%s:\n' % zone)
    fz = efilter(fzdict[zone],('SIT',''))
    fz0 = efilter(fz,('DN','0'))
    fz1 = efilter(fz,('DN','1'))
    fz2 = efilter(fz,('DN','2'))
    fdprint('P',ptcount(fz0),effunc(fz0))
    fdprint('1st',ptcount(fz1),effunc(fz1))
    ranges=((1,3),(4,6),(7,9),(10,12))
    for tup in ranges:
        fz2r=rfilter(fz2,'DIST',tup)
        rdprint('2nd',ptcount(fz2r),tup,effunc(fz2r))
    fz2top = gefilter(fz2,'DIST',13)
    geprint('2nd',ptcount(fz2top),13,effunc(fz2top))
    ovrprint(ptcount(fz0+fz1+fz2),effunc(fz0+fz1+fz2))

print('\n')

        
    
        
