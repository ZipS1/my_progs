s = input("Enter string: ")
c_count = 0
s_count = 0
f_count = 0

for i in s:
	if c_count < 0 or s_count < 0 or f_count < 0:
		print("Скобки расставлены неверно")
		exit()

	if i == '(':
		c_count += 1
	elif i == "[":
		s_count += 1
	elif i == "{":
		f_count += 1
	elif i == ")":
		c_count -= 1
	elif i == "]":
		s_count -= 1
	elif i == "}":
		f_count -= 1
	else:
		print("Строка введена неверно")
		exit()

if c_count != 0 or s_count != 0 or f_count != 0:
	print("Скобки расставлены неверно")
else:
	print("Скобки расставлены верно")