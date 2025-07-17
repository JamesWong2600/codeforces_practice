indexs = int(input())
correct_count = 0
for _ in range(indexs):
	choice = input()
	charlist = list(choice)
	charlist_count = 0
	for i in charlist:
		if i == "1":
			charlist_count = charlist_count + 1
	if charlist_count >= 2:
		correct_count = correct_count + 1
print(correct_count)