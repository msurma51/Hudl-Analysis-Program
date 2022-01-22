from DataImport import DATA
from DataImport import OF
from DataImport import opponent
from DataImport import field
from Functions import *

print('Run/Pass after Inefficient 1st Down Play or Explosive Play (Open Field)', end='\n\n')

Run=efilter(OF,('PLAY TYPE','Run'))
Pass=efilter(OF,('PLAY TYPE','Pass'))
fdr=rfilter(Run,'DN',(0,1))
fdp=rfilter(Pass,'DN',(0,1))
afr=npcount(DATA,fdr,'GN/LS',le,3)
aer=npcount(DATA,Run,'GN/LS',ge,10)
afp=npcount(DATA,fdp,'RESULT',contains,['Incomplete','Sack','Scramble'])
aiep=npcount(DATA,fdp,'GN/LS',le,3)
aep=npcount(DATA,Pass,'GN/LS',ge,15)

sitprint('After failed run',(afr))
sitprint('After failed pass',(afp))
sitprint('After inefficient pass',(aiep))
print()
sitprint('After explosive run',(aer))
sitprint('After explosive pass',(aep))

teams = list({play[field['ï»¿OPP TEAM']] for play in DATA[1:]})
exr = gefilter(Run,'GN/LS',10)
exp = gefilter(Pass,'GN/LS',15)

print('\nExplosive Runs:\n')
for team in teams: 
    tstring = '%s:' % team
    exrt=efilter(exr,('ï»¿OPP TEAM',team))
    if exrt!=[]:
        for play in exrt:
            tstring += ' %s,' % play[field['PLAY #']]
        tstring = tstring[:-1]
        print(tstring)
print('\nExplosive Passes:\n')
for team in teams: 
    tstring = '%s:' % team
    expt=efilter(exp,('ï»¿OPP TEAM',team))
    if expt!=[]:
        for play in expt:
            tstring += ' %s,' % play[field['PLAY #']]
        tstring = tstring[:-1]
        print(tstring)
 
print('\n')


        
    
        
