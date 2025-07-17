area = input()
area = area.split(" ")
area = [int(area[0]), int(area[1])]
if (area[0] % 1 == 1) and (area[1] % 1 == 1):
	print(int(area[0] * area[1] // 2))
else:
	print(int(area[0] * area[1] / 2))
