

class Beam():
	def __init__(self, beam):
		beam = beam.split()
		self.Num = int(beam[0])
		self.Start = int(beam[1]) -1
		self.End = int(beam[2]) -1

	def __repr__(self):
		printVal = ''
		printVal += ('Beam number = {}\n'.format(self.Num))
		printVal += ('Starting joint = {}\n'.format(self.Start + 1))
		printVal += ('Ending joint = {}\n'.format(self.End + 1))
		return(printVal)