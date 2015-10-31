

class Joint():
	def __init__(self, joint):
		joint = joint.split()
		self.Num = float(joint[0])
		self.X = float(joint[1])
		self.Y = float(joint[2])
		self.Fx = float(joint[3])
		self.Fy = float(joint[4])
		self.zeroDisp = int(joint[5])

	def __repr__(self):
		printVal = ''
		printVal += ('Joint number = {}\n'.format(self.Num))
		printVal += ('X-coordinate = {}\n'.format(self.X))
		printVal += ('Y-coordinate = {}\n'.format(self.Y))
		printVal += ('Force in X-direction = {}\n'.format(self.Fx))
		printVal += ('Force in Y-direction = {}\n'.format(self.Fy))
		printVal += ('Zero Displacement? {}\n'.format(self.zeroDisp))
		return(printVal)