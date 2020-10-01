string = input("Enter sting: ")
for symbol in string:
	if string.count(symbol) > 1:
		string = string[:string.index(symbol) + 1] + \
		string[string.index(symbol) + 1:].replace(symbol, '')
print(string)