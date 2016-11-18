expDict = { 
'+':'plus',
'-':'minus',
'*':'mulitiply',
'/':'division',
';':'semicolon',
'=':'equal',
':=':'assign',
'<':'less than',
'>':'greater than',
'(':'opening bracket',
')':'closing bracket'

}
reserverdDict  = {
'if':'if',
'then':'then',
'else':'else',
'end':'end',
'repeat':'repeat',
'until':'until',
'write':'write',
'read':'read'
}


def openFile():
	with open('tiny.txt', 'r') as f:
		read_data = f.readlines()
		return read_data

def readAll():
	lines = openFile()
	global comment
	comment =[]
	for index,line in enumerate(lines):
		print 'line #',index+1
		expType(line)	

def readLine(line):
	global comment
	newLine='';
	for car in line:
		if car == '{' or len(comment) > 0:
			if car != '}':
				comment.append(car)
			else:
				comment = []
		else:
			newLine += car
	return newLine

def lineSapceSplit(line):
	words = readLine(line).split() 
	return words

def lineArr(line):
	exparray =[] 
	for bit in lineSapceSplit(line):
	 	newbit = bit
	 	for exp in expDict:
	 		if exp in bit:
	 			if exp == '=' and bit[bit.find('=')-1]==':':
					pass
				else:
					newbit = newbit.replace(exp,' '+exp+' ')
		exparray.append(newbit)	
	return exparray 	

def FinalLine(line):
	exprelst = []
	for x in lineArr(line):
		l =  x.split()
		exprelst+=l
	return exprelst	

def expType(line):
	for exp in FinalLine(line):
		try:
			Type = expDict[exp] 
		except:
			try: 
				Type = reserverdDict[exp]		
			except:
				digitOrWord(exp)
			else:
				print (exp,Type)	
			
		else:
			print (exp,Type)	

def digitOrWord(exp):
	try:
		int(exp)
	except:
		print (exp,'identifier')
	else:
		print (exp,'number')	

readAll()
