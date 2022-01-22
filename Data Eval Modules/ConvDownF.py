from DataImport import DATA
from DataImport import opponent
from DataImport import field
from FZGenerator import *
from Functions import *

print('3rd Down Run/Pass by Distance and Field Zone', end='\n\n')

third = efilter(DATA,('DN','3'))
thirdranges = [(1,2),(3,3),(4,6),(7,9),(10,12),(13,15)]
fourth = efilter(DATA,('DN','4'))


def convdown():
    for tup in thirdranges:
        thirdr=rfilter(third,'DIST',tup)
        rdprint('3rd',ptcount(thirdr),tup,effunc(thirdr))
    thirdtop = gefilter(third,'DIST',16)
    geprint('3rd',ptcount(thirdtop),16,effunc(thirdtop))
    fourthr=rfilter(fourth,'DIST',(1,2))
    rdprint('4th',ptcount(fourthr),(1,2),effunc(fourthr))
    fourthtop=gefilter(fourth,'DIST',3)
    geprint('4th',ptcount(fourthtop),3,effunc(fourthtop))
convdown()

for fz in FZ:
    print('\n%s:\n' % fz)
    third = efilter(fzdict[fz],('DN','3'))
    fourth = efilter(fzdict[fz],('DN','4'))
    convdown()

print('\n')


        
    
        
