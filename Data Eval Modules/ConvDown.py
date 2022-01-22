from DataImport import DATA
from DataImport import opponent
from DataImport import field
output = r'D:\Python\Data Eval Outputs\%s Eval.txt' % opponent
import sys
sys.stdout = open(output, 'a')
print('3rd Down Run/Pass by Distance and Field Zone', end='\n\n')
reset = (0,)
reset*=14
(rs,ps,r3,p3,rm,pm,rl,pl,rxl,pxl,r2x,p2x,rDs,pDs)=reset
third = [play for play in DATA if play[field['DN']]=='3']
fourth = [play for play in DATA if play[field['DN']]=='4']
FZ = ('BACKED UP', 'UPFIELD', 'GREEN ZONE', 'RED ZONE', 'GOALLINE')

for play in third:  
    if int(play[field['DIST']])<3:
        if play[field['PLAY TYPE']]=='Run': rs+=1
        elif play[field['PLAY TYPE']]=='Pass': ps+=1
        else: pass
    if int(play[field['DIST']])==3:
        if play[field['PLAY TYPE']]=='Run': r3+=1
        elif play[field['PLAY TYPE']]=='Pass': p3+=1
        else: pass
    if int(play[field['DIST']]) in list(range(4,7)):
        if play[field['PLAY TYPE']]=='Run': rm+=1
        elif play[field['PLAY TYPE']]=='Pass': pm+=1
        else: pass
    if int(play[field['DIST']]) in list(range(7,10)):
        if play[field['PLAY TYPE']]=='Run': rl+=1
        elif play[field['PLAY TYPE']]=='Pass': pl+=1
        else: pass
    if int(play[field['DIST']]) in list(range(10,13)):
        if play[field['PLAY TYPE']]=='Run': rxl+=1
        elif play[field['PLAY TYPE']]=='Pass': pxl+=1
        else: pass
    if int(play[field['DIST']]) in list(range(13,15)):
        if play[field['PLAY TYPE']]=='Run': r2x+=1
        elif play[field['PLAY TYPE']]=='Pass': p2x+=1
        else: pass
    if int(play[field['DIST']])>15:
        if play[field['PLAY TYPE']]=='Run': rDs+=1
        elif play[field['PLAY TYPE']]=='Pass': pDs+=1
    

if rs!=0 or ps!=0:
    if rs>=ps: print('3rd&1-2\t\t%.2F%% Run' %(100*(rs/(rs+ps))),end='\t')
    else: print('3rd&1-2\t\t%.2F%% Pass' %(100*(ps/(rs+ps))),end='\t')
    print(r'%s Run / %s Pass' %(rs,ps))
if r3!=0 or p3!=0:
    if r3>=p3: print('3rd&3\t\t%.2F%% Run' %(100*(r3/(r3+p3))),end='\t')
    else: print('3rd&3\t\t%.2F%% Pass' %(100*(p3/(r3+p3))),end='\t')
    print(r'%s Run / %s Pass' %(r3,p3))
if rm!=0 or pm!=0:
    if rm>=pm: print('3rd&4-6\t\t%.2F%% Run' %(100*(rm/(rm+pm))),end='\t')
    else: print('3rd&4-6\t\t%.2F%% Pass' %(100*(pm/(rm+pm))),end='\t')
    print(r'%s Run / %s Pass' %(rm,pm))
if rl!=0 or pl!=0:
    if rl>=pl: print('3rd&7-9\t\t%.2F%% Run' %(100*(rl/(rl+pl))),end='\t')
    else: print('3rd&7-9\t\t%.2F%% Pass' %(100*(pl/(rl+pl))),end='\t')
    print(r'%s Run / %s Pass' %(rl,pl))
if rxl!=0 or pxl!=0:
    if rxl>=pxl: print('3rd&10-12\t%.2F%% Run' %(100*(rxl/(rxl+pxl))),end='\t')
    else: print('3rd&10-12\t%.2F%% Pass' %(100*(pxl/(rxl+pxl))),end='\t')
    print(r'%s Run / %s Pass' %(rxl,pxl))
if r2x!=0 or p2x!=0:
    if r2x>=p2x: print('3rd&13-15\t%.2F%% Run' %(100*(r2x/(r2x+p2x))),end='\t')
    else: print('3rd&13-15\t%.2F%% Pass' %(100*(p2x/(r2x+p2x))),end='\t')
    print(r'%s Run / %s Pass' %(r2x,p2x))
if rDs!=0 or pDs!=0:
    if rDs>=pDs: print('3rd&16+\t\t%.2F%% Run' %(100*(rDs/(rDs+pDs))),end='\t')
    else: print('3rd&16+\t\t%.2F%% Pass' %(100*(pDs/(rDs+pDs))),end='\t')
    print(r'%s Run / %s Pass' %(rDs,pDs))


for zone in FZ:
    (rs,ps,r3,p3,rm,pm,rl,pl,rxl,pxl,r2x,p2x,rDs,pDs)=reset
    fz = [play for play in third if play[field['FZ']]==zone]
    print('\n%s:' % zone)
    for play in fz:
        if int(play[field['DIST']])<3:
            if play[field['PLAY TYPE']]=='Run': rs+=1
            elif play[field['PLAY TYPE']]=='Pass': ps+=1
            else: pass
        if int(play[field['DIST']])==3:
            if play[field['PLAY TYPE']]=='Run': r3+=1
            elif play[field['PLAY TYPE']]=='Pass': p3+=1
            else: pass
        if int(play[field['DIST']]) in list(range(4,7)):
            if play[field['PLAY TYPE']]=='Run': rm+=1
            elif play[field['PLAY TYPE']]=='Pass': pm+=1
            else: pass
        if int(play[field['DIST']]) in list(range(7,10)):
            if play[field['PLAY TYPE']]=='Run': rl+=1
            elif play[field['PLAY TYPE']]=='Pass': pl+=1
            else: pass
        if int(play[field['DIST']]) in list(range(10,13)):
            if play[field['PLAY TYPE']]=='Run': rxl+=1
            elif play[field['PLAY TYPE']]=='Pass': pxl+=1
            else: pass
        if int(play[field['DIST']]) in list(range(13,15)):
            if play[field['PLAY TYPE']]=='Run': r2x+=1
            elif play[field['PLAY TYPE']]=='Pass': p2x+=1
            else: pass
        if int(play[field['DIST']])>15:
            if play[field['PLAY TYPE']]=='Run': rDs+=1
            elif play[field['PLAY TYPE']]=='Pass': pDs+=1
        

    if rs!=0 or ps!=0:
        if rs>=ps: print('3rd&1-2\t\t%.2F%% Run' %(100*(rs/(rs+ps))),end='\t')
        else: print('3rd&1-2\t\t%.2F%% Pass' %(100*(ps/(rs+ps))),end='\t')
        print(r'%s Run / %s Pass' %(rs,ps))
    if r3!=0 or p3!=0:
        if r3>=p3: print('3rd&3\t\t%.2F%% Run' %(100*(r3/(r3+p3))),end='\t')
        else: print('3rd&3\t\t%.2F%% Pass' %(100*(p3/(r3+p3))),end='\t')
        print(r'%s Run / %s Pass' %(r3,p3))
    if rm!=0 or pm!=0:
        if rm>=pm: print('3rd&4-6\t\t%.2F%% Run' %(100*(rm/(rm+pm))),end='\t')
        else: print('3rd&4-6\t\t%.2F%% Pass' %(100*(pm/(rm+pm))),end='\t')
        print(r'%s Run / %s Pass' %(rm,pm))
    if rl!=0 or pl!=0:
        if rl>=pl: print('3rd&7-9\t\t%.2F%% Run' %(100*(rl/(rl+pl))),end='\t')
        else: print('3rd&7-9\t\t%.2F%% Pass' %(100*(pl/(rl+pl))),end='\t')
        print(r'%s Run / %s Pass' %(rl,pl))
    if rxl!=0 or pxl!=0:
        if rxl>=pxl: print('3rd&10-12\t%.2F%% Run' %(100*(rxl/(rxl+pxl))),end='\t')
        else: print('3rd&10-12\t%.2F%% Pass' %(100*(pxl/(rxl+pxl))),end='\t')
        print(r'%s Run / %s Pass' %(rxl,pxl))
    if r2x!=0 or p2x!=0:
        if r2x>=p2x: print('3rd&13-15\t%.2F%% Run' %(100*(r2x/(r2x+p2x))),end='\t')
        else: print('3rd&13-15\t%.2F%% Pass' %(100*(p2x/(r2x+p2x))),end='\t')
        print(r'%s Run / %s Pass' %(r2x,p2x))
    if rDs!=0 or pDs!=0:
        if rDs>=pDs: print('3rd&16+\t\t%.2F%% Run' %(100*(rDs/(rDs+pDs))),end='\t')
        else: print('3rd&16+\t\t%.2F%% Pass' %(100*(pDs/(rDs+pDs))),end='\t')
        print(r'%s Run / %s Pass' %(rDs,pDs))

print('\n4th Down Run/Pass by Distance and Field Zone', end='\n\n')
(r4s,p4s,r4l,p4l)=(0,0,0,0)
for play in fourth:  
    if int(play[field['DIST']])<3:
        if play[field['PLAY TYPE']]=='Run': r4s+=1
        elif play[field['PLAY TYPE']]=='Pass': p4s+=1
        else: pass
    if int(play[field['DIST']])==3:
        if play[field['PLAY TYPE']]=='Run': r4l+=1
        elif play[field['PLAY TYPE']]=='Pass': p4l+=1
        else: pass
if r4s!=0 or p4s!=0:
        if r4s>=p4s: print('4th&1-2\t\t%.2F%% Run' %(100*(r4s/(r4s+p4s))),end='\t')
        else: print('4th&1-2\t\t%.2F%% Pass' %(100*(p4s/(r4s+p4s))),end='\t')
        print(r'%s Run / %s Pass' %(r4s,p4s))
if r4l!=0 or p4l!=0:
        if r4l>=p4l: print('4th&3+\t\t%.2F%% Run' %(100*(r4l/(r4l+p4l))),end='\t')
        else: print('4th&3+\t\t%.2F%% Pass' %(100*(pl/(r4l+p4l))),end='\t')
        print(r'%s Run / %s Pass' %(r4l,p4l))

for zone in FZ:
    (r4s,p4s,r4l,p4l)=(0,0,0,0)
    fz = [play for play in fourth if play[field['FZ']]==zone]
    print('\n%s:' % zone)
    for play in fz:
        if int(play[field['DIST']])<3:
            if play[field['PLAY TYPE']]=='Run': r4s+=1
            elif play[field['PLAY TYPE']]=='Pass': p4s+=1
            else: pass
        if int(play[field['DIST']])==3:
            if play[field['PLAY TYPE']]=='Run': r4l+=1
            elif play[field['PLAY TYPE']]=='Pass': p4l+=1
            else: pass
    if r4s!=0 or p4s!=0:
            if r4s>=p4s: print('4th&1-2\t\t%.2F%% Run' %(100*(r4s/(r4s+p4s))),end='\t')
            else: print('4th&1-2\t\t%.2F%% Pass' %(100*(p4s/(r4s+p4s))),end='\t')
            print(r'%s Run / %s Pass' %(r4s,p4s))
    if r4l!=0 or p4l!=0:
            if r4l>=p4l: print('4th&3+\t\t%.2F%% Run' %(100*(r4l/(r4l+p4l))),end='\t')
            else: print('4th&3+\t\t%.2F%% Pass' %(100*(pl/(r4l+p4l))),end='\t')
            print(r'%s Run / %s Pass' %(r4l,p4l))

print('\n')
sys.stdout.close()

        
    
        
