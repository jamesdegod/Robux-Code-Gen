import random
def getCode():
	r = ""
	for i in range(0, 3):
        	r+=str(random.randint(0, 10))
	return r

with open("robux.txt", "a") as file:
	while True:
		r = ""
		for x in range(0, 3):
			r+=getCode() + "-"
		print(r[:-1])
		file.write(r[:-1] + "\n");
def getCode():
	r = ""
	for i in range(0, 3):
        	r+=str(random.randint(0, 10))
	return r
while True:
	r = ""
	for x in range(0, 4):
		r+=getCode() + "-"
	print(r[:-1])