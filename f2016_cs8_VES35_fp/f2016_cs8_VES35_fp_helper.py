""" Helper file containing classes """
class Marathon:
	def __init__(self, n, d=0):
		self.name = n
		self.distance = d
		self.runs = 1

	def __str__(self):
		# rjust right justifies with the specified width
		return "Name : " + self.name.rjust(20) + ". Distance run : " + str(self.getDistance()).rjust(9) + ". Runs : " + str(self.getRuns()).rjust(4)

	def addDistance(self, d):
		self.distance += d 

	def addDistances(self, ld):
		for d in ld:
			self.distance += d

	def getName(self):
		return self.name

	def addRuns(self):
		self.runs += 1

	def getRuns(self):
		return self.runs

	def getDistance(self):
		return self.distance
	