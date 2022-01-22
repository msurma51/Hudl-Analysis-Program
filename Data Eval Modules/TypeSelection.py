from DataImport import DATA
from DataImport import OF
from DataImport import opponent
from DataImport import field
output = r'D:\Python\Data Eval Outputs\%s Eval.txt' % opponent
import sys
sys.stdout = open(output, 'a')
print('Run/Pass after Inefficient or Explosive Play (Open Field)', end='\n\n')
reset = (0,)
reset*=8
(rafr,pafr,raer,paer,rafp,pafp,raep,paep)=reset

for i in range(len(OF)):
    if OF[i][field['DN']]!='2' and OF[i][field['PLAY TYPE']]=='Run':
        if int(OF[i][field['GN/LS']])<4:
            if OF[i+1][field['PLAY TYPE']]=='Run': rafr+=1
            elif OF[i+1][field['PLAY TYPE']]=='Pass': pafr+=1
            else: pass
        if int(OF[i][field['GN/LS']])>9:
            if OF[i+1][field['PLAY TYPE']]=='Run': raer+=1
            elif OF[i+1][field['PLAY TYPE']]=='Pass': paer+=1
            else: pass
    if OF[i][field['DN']]!='2' and OF[i][field['PLAY TYPE']]=='Pass':
        if OF[i][field['RESULT']] in ("Incomplete", "Sack", "Scramble"):
            if OF[i+1][field['PLAY TYPE']]=='Run': rafp+=1
            elif OF[i+1][field['PLAY TYPE']]=='Pass': pafp+=1
            else: pass
        if int(OF[i][field['GN/LS']])>14:
            if OF[i+1][field['PLAY TYPE']]=='Run': raep+=1
            elif OF[i+1][field['PLAY TYPE']]=='Pass': paep+=1
            else: pass

if rafr!=0 or pafr!=0:
    if rafr>=pafr: print('After failed run: %.2F%% Run' %(100*(rafr/(rafr+pafr))),end='\t\t')
    else: print('After failed run: %.2F%% Pass' %(100*(pafr/(rafr+pafr))),end='\t\t')
    print(r'%s Run / %s Pass' %(rafr,pafr))
if raer!=0 or paer!=0:
    if raer>=paer: print('After explosive run: %.2F%% Run' %(100*(raer/(raer+paer))),end='\t')
    else: print('After explosive run: %.2F%% Pass' %(100*(paer/(raer+paer))),end='\t')
    print(r'%s Run / %s Pass' %(raer,paer))
if rafp!=0 or pafp!=0:
    if rafp>=pafp: print('After failed pass: %.2F%% Run' %(100*(rafp/(rafp+pafp))),end='\t\t')
    else: print('After failed pass: %.2F%% Pass' %(100*(paer/(rafp+pafp))),end='\t\t')
    print(r'%s Run / %s Pass' %(rafp,pafp))
if raep!=0 or paep!=0:
    if raep>=paep: print('After explosive pass: %.2F%% Run' %(100*(raep/(raep+paep))),end='\t')
    else: print('After explosive pass: %.2F%% Pass' %(100*(paep/(raep+paep))),end='\t')
    print(r'%s Run / %s Pass' %(raep,paep))


sys.stdout.close()

        
    
        
