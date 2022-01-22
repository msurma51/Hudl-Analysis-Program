from DataImport import DATA
from DataImport import opponent
from DataImport import field

FZ=('BACKED UP', 'UPFIELD', 'MIDFIELD', 'GREEN ZONE', 'RED ZONE', 'GOALLINE')
(backedup,upfield,midfield,greenzone,redzone,goalline)=([],[],[],[],[],[])
fzdata=(backedup,upfield,midfield,greenzone,redzone,goalline)
fzdict=dict(zip(FZ,fzdata))


for play in DATA[1:]:
	if int(play[field['YARD LN']]) in [0-i for i in range(1,20)]: backedup.append(play)
	elif int(play[field['YARD LN']]) in [0-i for i in range(20,40)]: upfield.append(play)
	elif int(play[field['YARD LN']]) in ([0-i for i in range(40,50)]+list(range(40,51))): midfield.append(play)
	elif int(play[field['YARD LN']]) in list(range(26,40)): greenzone.append(play)
	elif int(play[field['YARD LN']]) in list(range(6,26)): redzone.append(play)
	elif int(play[field['YARD LN']]) in list(range(1,6)): goalline.append(play)

