import pynmea2

f = open('/dev/ttyAMA0', 'r')

while True:
	line = f.readline()
	if len(line) == 1:
		continue
	print(len(line))
	
	#print(f.readline())
