'''
import DataImport
import Functions
import FZGenerator
'''
from DataImport import opponent
output = r'D:\Python\Data Eval Outputs\%s Test Eval.txt' % opponent
import sys
sys.stdout = open(output, 'a')

import TypeSelectionF
import PassProTest

sys.stdout.close()
