from DataImport import DATA, OF, opponent, field
from Functions import *
from statistics import mean

print('Run/Pass Average and Efficiency', end='\n\n')

def cleanprint(playstr,freq,ppa,eff,ineff):
    L=list(range(1,6))
    if playstr=='': playstr='No value'
    for x in L:
        if (len(playstr)+1)>=(8*x): continue
        else: tab=x; break
    ppastr=len('%.1f Avg ' % ppa)
    if ppastr>=9:
        print('%s:%s%sx\t%.1f Avg\t%.1f%% Efficient' % (playstr,('\t'*(4-tab)),freq,ppa,(100*(eff/(eff+ineff)))))
    else:
        print('%s:%s%sx\t%.1f Avg\t\t%.1f%% Efficient' % (playstr,('\t'*(4-tab)),freq,ppa,(100*(eff/(eff+ineff)))))

def efficiency(data,fstring,header): 
    print(header,':')
    freqs = freqsort(data,fstring)
    for tup in freqs:
        (freq,playstr)=tup
        plays=efilter(data,(fstring,playstr))
        gnls=[int(play[field['GN/LS']]) for play in plays]
        ppa=mean(gnls)
        (eff,ineff)=effunc(plays)
        if freq>5:
            cleanprint(playstr,freq,ppa,eff,ineff)
    print()



Run=efilter(DATA,('PLAY TYPE','Run'))
Pass=efilter(DATA,('PLAY TYPE', 'Pass'))
rpo=efilter(DATA, ('PLAY TYPE 2', 'RPO'))
iztags=efilter(DATA,('OFF PLAY','IZ'))


efficiency(Run,'OFF PLAY','Run Play')
efficiency(Pass,'ROUTE CONCEPT','Route Concept')
if len(rpo)>5: efficiency(rpo, 'OFF PLAY', 'RPO')
if len(iztags)>5: efficiency(iztags, 'RUN TAG', 'IZ TAG')


