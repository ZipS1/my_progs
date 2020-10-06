def sort(i):
	return i[1]

with open('4p88_in.txt', 'r') as f:
	words = f.readlines()

each = []
counting = []

for i in words:
	if i not in each:
		each.append(i)
		arr = [i, words.count(i)]
		counting.append(arr)

counting.sort(key=sort, reverse = True)

with open('4p88_out.txt', 'w', encoding='utf-8') as f:
	for el in counting:
		for i in range(el[1]):
			f.write(el[0])  

