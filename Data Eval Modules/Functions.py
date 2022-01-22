from DataImport import DATA
from DataImport import field
import operator
from operator import le, ge, eq, contains



def ptcount(data):       #counting run/pass within a given situation
    playtype=[play[field['PLAY TYPE']] for play in data]
    rnum=playtype.count('Run')
    pnum=playtype.count('Pass')
    return (rnum,pnum)

def npcount(data,subdata,fstring,opfunc,ref):  #counting run/pass the play after a given event
    subdata=efilter(subdata,('SERIES END',''))
    if opfunc==contains:
        plays=[play for play in subdata if opfunc(ref, play[field[fstring]])]
    elif isinstance(ref, int):
        plays=[play for play in subdata if opfunc(int(play[field[fstring]]),ref)]
    else:
        plays=[play for play in subdata if opfunc(play[field[fstring]],ref)]
    pindex=(data.index(play) for play in plays)
    nextdata=[data[i+1] for i in pindex]
    (rnum,pnum)=ptcount(nextdata)
    return (rnum,pnum)


def efilter(data,*critlist): #critlist is a list of tupled pairs, i.e. [('DN','2'),('DIST','5')]
    playlist=[]
    for play in data:
        for (x,y) in critlist:
            if play[field[x]]==y: continue
            else: break
        else: playlist.append(play)
    return playlist

def rfilter(data,numfield,rangetup):
    (start,stop)=rangetup
    playlist=[play for play in data
              if int(play[field[numfield]]) in list(range(start,stop+1))]
    return playlist


def gefilter(data,numfield,rangemin):
    playlist=[play for play in data
              if int(play[field[numfield]]) >= rangemin]
    return playlist

def lefilter(data,numfield,rangemin):
    playlist=[play for play in data
              if int(play[field[numfield]]) <= rangemin]
    return playlist

def confilter(data,fieldstr,substr):
    playlist=[play for play in data
              if substr in play[field[fieldstr]]]
    return playlist

def freqsort(data,fstring): #Returns an ordered tuple of object frequency in a given field
    flist=[play[field[fstring]] for play in data]
    fset=set(flist)
    freq=[(flist.count(x),x) for x in fset]
    freqs=sorted(freq,reverse=True)
    return freqs

def effunc(data):
    (eff,ineff)=(0,0)
    for play in data:
        if play[field['DN']] in ['0','1']:
            if int(play[field['GN/LS']])>3: eff+=1
            else: ineff+=1
        elif play[field['DN']]=='2':
            if int(play[field['GN/LS']])>=(int(play[field['DIST']])/2):eff+=1
            else: ineff+=1
        elif play[field['DN']] in ['3','4']:
            if int(play[field['GN/LS']])>=int(play[field['DIST']]):eff+=1
            else:ineff+=1
    return (eff,ineff)

def ptepf(pttuple,efftup):
    print(r'%s Run / %s Pass' %(pttuple),end='\t')
    (eff,ineff)=efftup
    if len('%s Run / %s Pass' %(pttuple))>=16:
        print('%.lF%% Efficient' % (100*(eff/(eff+ineff))))
    else: print('\t%.lF%% Efficient' % (100*(eff/(eff+ineff))))
    

def fdprint(downstring,pttuple,efftup):
    if pttuple !=(0,0):
        (rnum,pnum)=pttuple
        if rnum>=pnum: print('%s&10\t\t%.2F%% Run' %(downstring,100*(rnum/(rnum+pnum))),end='\t')
        else: print('%s&10\t\t%.2F%% Pass' %(downstring,100*(pnum/(rnum+pnum))),end='\t')
        ptepf(pttuple,efftup)
    else: pass
    return None

def rdprint(downstring,pttuple,rangetup,efftup):
    if pttuple !=(0,0):
        (rnum,pnum)=pttuple
        (start,stop)=rangetup
        if len(str(start))>1:
            if rnum>=pnum: print('%s&%s-%s\t%.2F%% Run' %(downstring,start,stop,100*(rnum/(rnum+pnum))),end='\t')
            else: print('%s&%s-%s\t%.2F%% Pass' %(downstring,start,stop,100*(pnum/(rnum+pnum))),end='\t')
        elif start!=stop:
            if rnum>=pnum: print('%s&%s-%s\t\t%.2F%% Run' %(downstring,start,stop,100*(rnum/(rnum+pnum))),end='\t')
            else: print('%s&%s-%s\t\t%.2F%% Pass' %(downstring,start,stop,100*(pnum/(rnum+pnum))),end='\t')
        elif start==stop:
            if rnum>=pnum: print('%s&%s\t\t%.2F%% Run' %(downstring,start,100*(rnum/(rnum+pnum))),end='\t')
            else: print('%s&%s\t\t%.2F%% Pass' %(downstring,start,100*(pnum/(rnum+pnum))),end='\t')
        ptepf(pttuple,efftup)
    else: pass
    return None

def geprint(downstring,pttuple,rangemin,efftup):
    if pttuple !=(0,0):
        (rnum,pnum)=pttuple
        if rnum>=pnum: print('%s&%s+\t\t%.2F%% Run' %(downstring,rangemin,100*(rnum/(rnum+pnum))),end='\t')
        else: print('%s&%s+\t\t%.2F%% Pass' %(downstring,rangemin,100*(pnum/(rnum+pnum))),end='\t')
        ptepf(pttuple,efftup)   
    else: pass
    return None

def ovrprint(pttuple,efftup):
    (rov,pov)=pttuple
    if (rov,pov)!=(0,0):
        if rov>=pov: print('Overall\t\t%.2F%% Run' %(100*(rov/(rov+pov))),end='\t')
        else: print('Overall\t\t%.2F%% Pass' %(100*(pov/(rov+pov))),end='\t')
        ptepf(pttuple,efftup)
    else: pass
    return None

def sitprint(sitstring,ptcountsit):  
    if ptcountsit !=(0,0):
        (rnum,pnum)=ptcountsit
        if rnum>=pnum: print('%s:\t%.2F%% Run' %(sitstring,(100*(rnum/(rnum+pnum)))),end='\t\t')
        else: print('%s:\t%.2F%% Pass' %(sitstring,(100*(pnum/(rnum+pnum)))),end='\t\t')
        print(r'%s Run / %s Pass' %(rnum,pnum))
    
        
