s = input("Enter string: ")
symbols = ('(', ')', '[', ']', '{', '}')

for i in s:
	if i not in symbols:
		print("Строка введена неверно!")
		exit()

while True:
	if s.find("()") != -1:
		s = s.replace('()', '')
	elif s.find("[]") != -1:
		s = s.replace('[]', '')
	elif s.find(r"{}") != -1:
		s = s.replace(r'{}', '')
	else:
		if s == '':
			print("Скобки расставлены верно")
			break
		else:
			print("Скобки расставлены неверно")
			break


