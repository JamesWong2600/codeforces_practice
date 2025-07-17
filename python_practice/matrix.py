x_coord = 0
y_coord = 0
for i in range(5):
	row = input() 
	if "1" in row:
		y_coord = i
		row = row.split(" ")
		for j in range(5):
			if row[j] == "1":
				x_coord = j

result = abs(x_coord - 2) + abs(y_coord - 2)
print(result)