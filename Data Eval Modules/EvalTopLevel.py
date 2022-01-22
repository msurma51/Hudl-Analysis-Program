'''
Requires modules DataImport, Functions and FZGenerator.
Modules return print functions that write to a .txt output.
'''

from DataImport import opponent
output = r'D:\Python\Data Eval Outputs\%s Eval.txt' % opponent
import sys
sys.stdout = open(output, 'a')

#Eval Modules:
import PersonnelF
import FieldZoneF
import ConvDownF
import TypeSelectionF
#import PassPro
import Efficiency

sys.stdout.close()
