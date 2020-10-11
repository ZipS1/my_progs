def periodCheck(n, p):
    periodicity = True
    n = n.ljust(len(n) // p * p + 2*p, "?")
    syms = []

    for i in range(p):
        psyms = ''
        for m in range(len(n) // p):
            psyms += n[i + p*m]
        syms.append(psyms)

    for el in syms:
        el = el.replace("?", '')
        if el == '':
            break
        if el.replace(el[0], '') != '':
            periodicity = False

    if periodicity:
        return "YES"
    else:
        return "NO"

n, p = map(int, input().split())

strings = []

for i in range(n):
    strings.append(input())

for string in strings:
    print(periodCheck(string, p))
