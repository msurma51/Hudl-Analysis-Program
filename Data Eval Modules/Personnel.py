from DataImport import DATA
from DataImport import opponent
from DataImport import OF
from DataImport import field
output = r'D:\Python\Data Eval Outputs\%s Eval.txt' % opponent
import sys
sys.stdout = open(output, 'a')
print('Run/Pass by D&D by Personnel', end='\n\n')
perlist=[play[field['PERSONNEL']] for play in OF]
perset=set(perlist)
freq=[(perlist.count(x),x) for x in perset]
freq.reverse()
reset = (0,)
reset*=12
for (x,y) in freq:
    ppl=[play for play in OF if play[field['PERSONNEL']]==y]
    (r0,p0,r1,p1,r2s,p2s,r2m,p2m,r2l,p2l,r2xl,p2xl)=reset
    for play in ppl:
        if play[field['DN']]=='0':
            if play[field['PLAY TYPE']]=='Run': r0+=1
            elif play[field['PLAY TYPE']]=='Pass': p0+=1
            else: pass
        elif play[field['DN']]=='1':
            if play[field['PLAY TYPE']]=='Run': r1+=1
            elif play[field['PLAY TYPE']]=='Pass': p1+=1
            else: pass
        elif play[field['DN']]=='2':
            if int(play[field['DIST']])<4:
                if play[field['PLAY TYPE']]=='Run': r2s+=1
                elif play[field['PLAY TYPE']]=='Pass': p2s+=1
                else: pass
            elif int(play[field['DIST']]) in list(range(4,7)):
                if play[field['PLAY TYPE']]=='Run': r2m+=1
                elif play[field['PLAY TYPE']]=='Pass': p2m+=1
                else: pass
            elif int(play[field['DIST']]) in list(range(7,10)):
                if play[field['PLAY TYPE']]=='Run': r2l+=1
                elif play[field['PLAY TYPE']]=='Pass': p2l+=1
                else: pass
            elif int(play[field['DIST']])>9:
                if play[field['PLAY TYPE']]=='Run': r2xl+=1
                elif play[field['PLAY TYPE']]=='Pass': p2xl+=1
                else: pass
    print('%s Personnel:' % y)
    if r0!=0 or p0!=0:
        if r0>=p0: print('P&10\t\t%.2F%% Run' %(100*(r0/(r0+p0))),end='\t')
        else: print('P&10\t\t%.2F%% Pass' %(100*(p0/(r0+p0))),end='\t')
        print(r'%s Run / %s Pass' %(r0,p0))
    if r1!=0 or p1!=0:
        if r1>=p1: print('1st&10\t\t%.2F%% Run' %(100*(r1/(r1+p1))),end='\t')
        else: print('1st&10\t\t%.2F%% Pass' %(100*(p1/(r1+p1))),end='\t')
        print(r'%s Run / %s Pass' %(r1,p1))
    if r2s!=0 or p2s!=0:
        if r2s>=p2s: print('2nd&1-3\t\t%.2F%% Run' %(100*(r2s/(r2s+p2s))),end='\t')
        else: print('2nd&1-3\t\t%.2F%% Pass' %(100*(p2s/(r2s+p2s))),end='\t')
        print(r'%s Run / %s Pass' %(r2s,p2s))
    if r2m!=0 or p2m!=0:
        if r2m>=p2m: print('2nd&4-6\t\t%.2F%% Run' %(100*(r2m/(r2m+p2m))),end='\t')
        else: print('2nd&4-6\t\t%.2F%% Pass' %(100*(p2m/(r2m+p2m))),end='\t')
        print(r'%s Run / %s Pass' %(r2m,p2m))
    if r2l!=0 or p2l!=0:
        if r2l>=p2l: print('2nd&7-9\t\t%.2F%% Run' %(100*(r2l/(r2l+p2l))),end='\t')
        else: print('2nd&7-9\t\t%.2F%% Pass' %(100*(p2l/(r2l+p2l))),end='\t')
        print(r'%s Run / %s Pass' %(r2l,p2l))
    if r2xl!=0 or p2xl!=0:
        if r2xl>=p2xl: print('2nd&10+\t\t%.2F%% Run' %(100*(r2xl/(r2xl+p2xl))),end='\t')
        else: print('2nd&10+\t\t%.2F%% Pass' %(100*(p2xl/(r2xl+p2xl))),end='\t')
        print(r'%s Run / %s Pass' %(r2xl,p2xl))
    rov=sum((r0,r1,r2s,r2m,r2l,r2xl))
    pov=sum((p0,p1,p2s,p2m,p2l,p2xl))
    if rov!=0 or pov!=0:
        if rov>=pov: print('Overall\t\t%.2F%% Run' %(100*(rov/(rov+pov))),end='\t')
        else: print('Overall\t\t%.2F%% Pass' %(100*(pov/(rov+pov))),end='\t')
        print(r'%s Run / %s Pass' %(rov,pov))

print('\n')
sys.stdout.close()

        
    
        
