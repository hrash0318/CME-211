import numpy as np
from beam import Beam
from joint import Joint
import matplotlib.pyplot as plt
import matplotlib.pylab

class Truss():
	def __init__(self, jointFile, beamFile):
		self.__joints = self.constructJoints(jointFile)
		self.__beams = self.constructBeams(beamFile)

	def constructJoints(self, jointFile):
		f = open(jointFile,'r')
		tempjoint = []
		next(f)
		for line in f:
			tempjoint.append(Joint(line))
		f.close()
		return tempjoint

	def constructBeams(self, beamFile):
		f = open(beamFile,'r')
		tempbeam = []
		next(f)
		for line in f:
			tempbeam.append(Beam(line))
		f.close()
		return tempbeam

	def PlotGeometry(self, plotFile):
	 	for b in self.__beams:
	 		tempX = np.array([self.__joints[b.Start].X, self.__joints[b.End].X])
	 		tempY = np.array([self.__joints[b.Start].Y, self.__joints[b.End].Y])
	 		plt.plot(tempX,tempY, color = '.5', linewidth = 5.0)
		maxX = 1
		maxY = 1
		for j in self.__joints:
			if j.zeroDisp == 1:
				plt.plot(j.X,j.Y,'ro', markersize = 10)
			else:
				plt.plot(j.X,j.Y,'go', markersize = 10)
			if j.X > maxX:
				maxX = j.X
			if j.Y > maxY:
				maxY = j.Y
		size = max(maxX,maxY)
	 	plt.axis([-.5,size+.5,-.5,size+.5])
	 	plt.savefig(plotFile)
	 	plt.show()

	#def FindStress(self):


	def __repr__(self):
		printVal = ''
		printVal += str(self.__joints)
		printVal += str(self.__beams)
		return printVal