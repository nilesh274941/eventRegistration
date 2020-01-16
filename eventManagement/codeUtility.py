class CodeUtility():
	@staticmethod
	def getMemberCode():
		fileName="c:/123/django/project/eventManagement/memberCodeFile.txt"
		f=open(fileName,"r")
		line=f.read()
		print("LINE : "+line)
		code=int(line)
		f.close()
		code=code+1
		f=open(fileName,"w")
		f.write(str(code))
		f.close()
		return code
	@staticmethod
	def getEventCode():
		fileName="c:/123/django/project/eventManagement/eventCodeFile.txt"
		f=open(fileName,"r")
		code=int(f.readline())
		f.close()
		code=code+1
		f=open(fileName,"w")
		f.write(str(code))
		f.close()
		return code