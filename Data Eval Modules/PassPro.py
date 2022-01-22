from DataImport import DATA
from DataImport import opponent
from DataImport import field
from Functions import efilter
from Functions import freqsort


print('Pass Pro Evaluation', end='\n\n')

def prounpack(play):    #Split pass pro id into component parts.
    prolist=[x for x in play[field['PROTECTION (D)']]]
    prodict={'num':prolist[0]}
    if prolist[1].isalpha():
        prodict['toa']=prolist[1]
        prodict['tech']=prolist[2]
        prodict['fob']=prolist[3]
    else:
        if prolist[-1]=='N': prodict['man']=True
        else:
            prodict['tech']=prolist[1]
            prodict['fob']=prolist[2]
    if prolist[-1] not in ['F', 'B', 'N']:
        prodict['tag']=prolist[-1]
    return prodict


def fprint(tup):    #Print format for eventual outputs
    (datalist,datastr)=tup
    reps=len(datalist)
    dataset=set(datalist)
    freq=[(datalist.count(x),x) for x in dataset]
    freqs=sorted(freq,reverse=True)
    if (len(datastr)+len(str(reps)))<7: print('%s:%s' %(datastr,reps), end='\t\t')
    else: print('%s:%s' %(datastr,len(datalist)), end='\t')
    for (a,b) in freqs:
        print('%s: %.1f%%' %(b,((100*a)/len(datalist))), end='\t')
    print()

def profunc(data):  #Processes and prints pass pro eval for given data set
    keylist=(numlist,toalist,techlist,foblist,taglist)=([],[],[],[],[])
    manlist=0
    keystr=('Count','T/A Back','To Tech','FLD/BND','Tag')
    keyzip=list(zip(keylist,keystr))
    def prolist(*,num,toa=None,tech=None,fob=None,man=False,tag=None):
        nonlocal numlist,toalist,techlist,foblist,manlist,taglist
        numlist+=num
        if toa: toalist+=toa
        if tech: techlist+=tech
        if fob: foblist+=fob
        if man: manlist+=1
        if tag: taglist+=tag
    for play in data:
        prodict=prounpack(play)
        prolist(**prodict)
    for tup in keyzip:
        fprint(tup)
    print('Man:',manlist,end='\n\n')

def evalby(fstring): #Runs profunc by each observation in a given field
    freq=freqsort(dbp,fstring)
    for tup in freq:
        (freq,datastr)=tup
        if freq>5:
            print('%s %s:' % (fstring,datastr))
            plays=efilter(dbp,(fstring,datastr))
            profunc(plays)

print('All DBP:')
dbp=[play for play in DATA if play[field['OFF PLAY']] in ['5 STEP', '4 STEP', '3 STEP']]
profunc(dbp)
evalby('FORM CODE')
evalby('DEF FRONT')




    
        
