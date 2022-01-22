from DataImport import DATA
from DataImport import opponent
from DataImport import OF
from DataImport import field
from Functions import *


print('Run/Pass by D&D by Personnel (Open Field)')

freqs = freqsort(OF,'PERSONNEL')
for tup in freqs:
    (x,y)=tup
    print('\n%s Personnel: %sx\t%.1F%%\n' % (y,x,100*(x/len(OF))))
    per=efilter(OF,('PERSONNEL',y))
    per0 = efilter(per,('DN','0'))
    per1 = efilter(per,('DN','1'))
    per2 = efilter(per,('DN','2'))
    fdprint('P',ptcount(per0),effunc(per0))
    fdprint('1st',ptcount(per1),effunc(per1))
    ranges=[(1,3),(4,6),(7,9),(10,12)]
    for tup in ranges:
        per2r=rfilter(per2,'DIST',tup)
        rdprint('2nd',ptcount(per2r),tup,effunc(per2r))
    per2top = gefilter(per2,'DIST',13)
    geprint('2nd',ptcount(per2top),13,effunc(per2top))
    ovrprint(ptcount(per0+per1+per2),effunc(per0+per1+per2))


print('\n')


        
    
        
