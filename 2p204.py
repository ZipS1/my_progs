s = input('Введите строку: ')

l = list(s)
r = list(l)
l.reverse()
if l == r:
	print('Palindrom')
else:
	print('Nepalindrom')
input()
