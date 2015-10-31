import sys
import truss
from truss import Truss
import matplotlib.pyplot as plt

if len(sys.argv) < 3 or len(sys.argv) > 4:
	print('Usage:')
	print('python main.py [joints file] [beams file] [optional plot output file]')
	exit()

t = Truss(sys.argv[1],sys.argv[2])



if len(sys.argv) == 4:
	t.PlotGeometry(sys.argv[3])

