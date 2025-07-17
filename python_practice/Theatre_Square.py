# https://codeforces.com/problemset/problem/1/A
# if we want to get the max integer of x over y we can use x // y
v = input()
list = []
for word in v.split(" "):
	list.append(word)
x_amount = int(list[0]) / int(list[2])
x_amount_then = int(list[0]) // int(list[2])
if not x_amount == x_amount_then:
	x_amount = x_amount_then + 1
y_amount = int(list[1]) / int(list[2])
y_amount_then = int(list[1]) // int(list[2])
if not y_amount == y_amount_then:
	y_amount = y_amount_then + 1
print(int(x_amount) * int(y_amount))