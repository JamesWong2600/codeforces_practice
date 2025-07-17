setting = input()
result = input()
setting_list = []
result_list = []
pass_result_list = []
for word in setting.split(" "):
	setting_list.append(word)
for word in result.split(" "):
	result_list.append(word)
for i in range(int(setting_list[0])):
	if (int(result_list[i]) >= int(result_list[int(setting_list[1])-1])) and (int(result_list[i]) != 0):
		pass_result_list.append(result_list[i])
g = len(pass_result_list)	
print(g)
