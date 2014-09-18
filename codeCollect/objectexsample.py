class Human:
	def __init__(self):
		self.__name = ""
		self.__sex = ""

	def setName(self,name):
	    self.__name = name

	def getName(self):
		return self.__name

	def setSex(self,sex):
		self.__sex = sex

	def getSex(self):
		return self.__sex

	name = property(getName,setName)
	sex = property(getSex, setSex)

lilei = Human()
lilei.sex = 'male';
lilei.name = 'lilei';
ps1 = "%s %s appear" % (lilei.name, lilei.sex)
print(ps1)

hunmeimei = Human()
hunmeimei.sex = "female";
hunmeimei.name = "hanmeimei";
print("%s %s appear" % (hunmeimei.name, hunmeimei.sex))

#pee function
def doPee(self, how):
	print("%s %s %s pee" % (self.name, self.sex, how))

#dynamic bind function
Human.doPee = doPee

lilei.doPee("stand")
hunmeimei.doPee("sitdown")

#function for study
def study(self,learn):
	print("%s %s" % (self.name, learn))

#dynamic bind function
Human.dolearning = study

lilei.dolearning("How are you?")
hunmeimei.dolearning("I'm fine, thank you!")
