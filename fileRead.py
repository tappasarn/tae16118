f = open('/dev/ttyAMA0', 'r')
while True:
	print(f.readline())
