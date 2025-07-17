# Be aware of the input data type
# Since input data is string, we need to transform the data to integer
# if needed
# while a list item index is -1, it means it is the last item in the list
amount = int(input())
for i in range(amount):
	word = input()
	if len(word) <= 10:
		print(word)
	else:
		count = len(word) - 1
		c = len(word) - 2
		print(word[0] + str(c)+word[-1])

