letters = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
crypt_mode = 0
while crypt_mode != 1 and crypt_mode != 2 and crypt_mode != 3:
    print('Введите шифр работы (1 - шифр Цезаря, 2 - шифр Виженера):')
    crypt_mode = int(input())
    if crypt_mode != 1 and crypt_mode != 2:
        print('Неверно введен режим!')

mode = 100

if crypt_mode == 1:                                                     # шифр Цезаря
    while mode != 1 and mode != 2 and mode != 3:
        print('Введите режим (1 - шифрование, 2 - дешифрование с изв. сдвигом, 3 - дешифрование с неизв. сдвигом):')
        mode = int(input())
    if mode != 1 and mode != 2 and mode != 3:
        print('Неверно введен режим!')                                     
    if mode == 1:
        print('Введите сдвиг: ',end='')
        push = int(input())
        print('Введите строку для шифрования: ',end='')
        word = input()
        decr = ''
        for l in word:
            if l == ' ':
                decr += ' '
                continue
            cin = letters.index(l) + push
            if cin > 32:
                cin -= 33
            decr += letters[cin]
        print('Зашифрованное слово:', decr)
        input()
    elif mode == 2:
        print('Введите сдвиг: ',end='')
        push = int(input())
        print('Введите строку для дешифрования: ',end='')
        word = input()
        decr = ''
        for l in word:
            if l == ' ':
                decr += ' '
                continue
            cin = letters.index(l) - push
            decr += letters[cin]
        print('Расшифрованное слово:', decr)
        input()
    else:
        print('Введите строку для дешифрования: ',end='')
        word = input()
        print('Варианты шифровки:')
        for push in range(1, 33):
                decr = ''
                for l in word:
                    if l == ' ':
                        decr += ' '
                        continue
                    cin = letters.index(l) - push
                    decr += letters[cin]
                print(decr,'\t\t\t\t\t\tСдвиг - ',push)
else:                                                     # шифр Виженера
    push_array = []    
    keyword = ' '     
    decr = ''                                          
    while not keyword.isalpha():
        print('Введите ключевое слово: ',end='')
        keyword = input()
    for i in keyword:
        push_array.append(letters.index(i))
    push_count = 0
    print ('Введите шифруемое слово: ',end='')
    word = input()
    for i  in word:
        if i == ' ':
            decr += ' '
            continue
        cin = letters.index(i) + push_array[push_count]
        decr += letters[cin]
        push_count += 1
        if push_count == len(push_array):
            push_count = 1
    print('Зашифрованное слово:', decr)
    input()



