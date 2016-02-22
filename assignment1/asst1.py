import collections

def swapchars(s):
	c = collections.Counter()
	for x in s:
		if x.isalpha():
			c[x.lower()] += 1 

	lowval = 10000
	highval = 0
	for key, val in c.iteritems():
		if val > highval:
			highch = key
			highval = val
		if val < lowval:
			lowch = key
			lowval = val
	res = ""
	for x in s:
		if x.isalpha():
			if x.lower() == highch:
				if x == x.upper():
					res += lowch.upper()
				else:
					res += lowch
			elif x.lower() == lowch:
				if x == x.upper():
					res += highch.upper()
				else:
					res += highch
			else:
				res += x
		else:
			res += x
	return res

#print swapchars('I\'m just a chi-town coder with a nice flow.')

def sortcat(*args):
	n = args[0]
	a = []
	for x in range(1, len(args)):
		a.append(args[x]);
	a.sort(key=len, reverse = True)
	res = ""
	if n == -1:
		for x in a:
			res += x
	else:
		for x in range(0,n):
			res += a[x]
	return res

#sortcat(2, 'bc', 'c', 'abc')


abbrev = {}
state = {}

with open("states.txt", "r") as ins:
    array = []
    for line in ins:
        s = ""
        a = ""
        flag = False
        for x in line:
        	if x == '\n':
        		continue
        	if x == ',':
        		flag = True
        	elif flag == False:
        		s += x
        	else:
        		a += x
        abbrev[a] = s
        state[s] = a

def getState(ab):
	return state[ab]
def getAbbrev(st):
	return abbrev[st]

print getState("California")
print getAbbrev("CA")

