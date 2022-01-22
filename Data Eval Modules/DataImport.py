opponent = input('Which slapdick operation you got this week?')
fname = r'D:\Python\Full Scout Exports\%s.csv' % opponent
file = open(fname)
DATA = [play.rstrip().split(',') for play in file]
keybuilder = list(enumerate(DATA[0]))
field = {y:x for (x,y) in keybuilder}
OF = [play for play in DATA if (play[field['DN']] in ['0','1','2']) and (play[field['FZ']] in ['UPFIELD','GREEN ZONE']) and play[field['SIT']]=='']


