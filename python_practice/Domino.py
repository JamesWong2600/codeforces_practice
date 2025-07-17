area = input()
area = area.split(" ")
square_x = 2
square_y = 1
mode = 0
area = [int(area[0]), int(area[1])]
if (area[0] % 2 == 0) and (area[1] % 2 == 0):
	mode = 0
elif (area[0] % 2 == 1) and (area[1] % 2 == 1):
	mode = 1
elif (area[0] % 2 == 0) and (area[1] % 2 == 1): 
	mode = 2
elif (area[0] % 2 == 1) and (area[1] % 2 == 0):
	mode = 3

if mode == 0:
	print(int((area[0] / square_x) * (area[1] / square_y)))
if mode == 1:
	if area[0] == 1:
		v = (area[0] / square_x) * (area[1] % square_y) + (area[0] // square_y) * square_x		
	elif area[1] == 1:
		v = (area[0] % square_x) * (area[1] / square_y) + (area[0] // square_x) * square_y
	elif area[1] > area[0]:
		v = (area[0] // square_x) * (area[1] / square_y) + (area[0] // square_x) * square_y
	elif area[1] == area[0]:
		v = (area[0] // square_x) * (area[1] // square_y) + (area[0] // square_x) * square_y
	elif area[1] < area[0]:
		v = (area[0] / square_x) * (area[1] // square_y) + (area[0] // square_y) * square_y
	print(int(v))
if mode == 2:
	if area[0] == 1:
		v = ((area[0] % square_x) * (area[1] / square_y))
	elif area[1] >  area[0]:
		v = ((area[0] // square_x) * (area[1] / square_y))		
	print(int(v))
if mode == 3:
	if area[0] == 1:
		v = ((area[0] % square_y) * (area[1] / square_x))
	elif area[1] >  area[0]:
		v = ((area[0] // square_y) * (area[1] / square_x))
	print(int(v))