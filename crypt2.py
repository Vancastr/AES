# Таблица S-box
Sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
        ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
        ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
        ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
        ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
        ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
        ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
        ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
        ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
        ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
        ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
        ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
        ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
        ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
        ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
        ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]
# Таблица InvS-BOX
InvSbox = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
           ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
           ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
           ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
           ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
           ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
           ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
           ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
           ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
           ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
           ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
           ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
           ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
           ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
           ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
           ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]


# Перевод в нужную систему счисления
def cs(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alph[n]
    else:
        return cs(n // to_base, to_base) + alph[n % to_base]

#  Функция ShiftRows — циклический сдвиг строк state
def shiftrows(mass, flag=False):
    # Проверяем, что требуется провести: зашифрование или расшифрование
    if not flag:
        k = mass[1][0]
        for i in range(3):
            mass[1][i] = mass[1][i + 1]
        mass[1][3] = k
        for j in range(2):
            k = mass[2][0]
            for i in range(3):
                mass[2][i] = mass[2][i + 1]
            mass[2][3] = k
        for j in range(3):
            k = mass[3][0]
            for i in range(3):
                mass[3][i] = mass[3][i + 1]
            mass[3][3] = k
    else:
        k = mass[1][3]
        for i in range(3, 0, -1):
            mass[1][i] = mass[1][i - 1]
        mass[1][0] = k
        for j in range(2):
            k = mass[2][3]
            for i in range(3, 0, -1):
                mass[2][i] = mass[2][i - 1]
            mass[2][0] = k
        for j in range(3):
            k = mass[3][3]
            for i in range(3, 0, -1):
                mass[3][i] = mass[3][i - 1]
            mass[3][0] = k

    return mass


# Функции умножения элементов столбцов
def mul_by_02(num):
    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0b1
    return res % 0x100


def mul_by_03(num):
    return mul_by_02(num) ^ num


def mul_by_09(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


def mul_by_0b(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


def mul_by_0d(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


def mul_by_0e(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)


# Функция MixColumns - перемешивание столбца
def MixColumns(mass, flag=False):
    # Проверяем, что требуется провести: зашифрование или расшифрование
    if flag == False:
        for i in range(4):
            s0 = mul_by_02(mass[0][i]) ^ mul_by_03(mass[1][i]) ^ mass[2][i] ^ mass[3][i]
            s1 = mass[0][i] ^ mul_by_02(mass[1][i]) ^ mul_by_03(mass[2][i]) ^ mass[3][i]
            s2 = mass[0][i] ^ mass[1][i] ^ mul_by_02(mass[2][i]) ^ mul_by_03(mass[3][i])
            s3 = mul_by_03(mass[0][i]) ^ mass[1][i] ^ mass[2][i] ^ mul_by_02(mass[3][i])
            mass[0][i] = s0
            mass[1][i] = s1
            mass[2][i] = s2
            mass[3][i] = s3
    else:
        for i in range(4):
            s0 = mul_by_0e(mass[0][i]) ^ mul_by_0b(mass[1][i]) ^ mul_by_0d(mass[2][i]) ^ mul_by_09(mass[3][i])
            s1 = mul_by_09(mass[0][i]) ^ mul_by_0e(mass[1][i]) ^ mul_by_0b(mass[2][i]) ^ mul_by_0d(mass[3][i])
            s2 = mul_by_0d(mass[0][i]) ^ mul_by_09(mass[1][i]) ^ mul_by_0e(mass[2][i]) ^ mul_by_0b(mass[3][i])
            s3 = mul_by_0b(mass[0][i]) ^ mul_by_0d(mass[1][i]) ^ mul_by_09(mass[2][i]) ^ mul_by_0e(mass[3][i])
            mass[0][i] = s0
            mass[1][i] = s1
            mass[2][i] = s2
            mass[3][i] = s3
    return mass


# Функция для нелинейной замены байт по таблице S-box
def subBytes(mass, flag=False):
    # Проверяем, что требуется провести: зашифрование или расшифрование
    if not flag:
        table = Sbox
    else:
        table = InvSbox
    for i in range(4):
        for j in range(4):
            mass[i][j] = int(cs(table[(mass[i][j] & 240) >> 4][mass[i][j] & 15], 10, 16))
    return mass


# Функция для зашифрования
def encrypt(state, keys):
# Расширение ключа
    statei = [[int(cs(state[i][j], 10, 16)) for j in range(4)] for i in range(4)]
    keyi = [[0] * 45 for i in range(4)]
    helper = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
    for i in range(4):
        for j in range(4):
            keyi[i][j] = int(cs(keys[i][j], 10, 16))
    for i in range(1, 11):
        k = keyi[0][i * 4 - 1]
        # Сдвиг вверх
        keyi[0][i * 4] = keyi[1][i * 4 - 1]
        keyi[1][i * 4] = keyi[2][i * 4 - 1]
        keyi[2][i * 4] = keyi[3][i * 4 - 1]
        keyi[3][i * 4] = k
        # Замена с Sbox
        for j in range(4):
            keyi[j][i * 4] = int(cs(Sbox[(keyi[j][i * 4] & 240) >> 4][keyi[j][i * 4] & 15], 10, 16))
        keyi[0][i * 4] = keyi[0][i * 4] ^ keyi[0][i * 4 - 4] ^ helper[i]
        for j in range(1, 4):
            keyi[j][i * 4] = keyi[j][i * 4] ^ keyi[j][i * 4 - 4]
        for j in range(1, 4):
            for k in range(4):
                keyi[k][i * 4 + j] = keyi[k][i * 4 - 1 + j] ^ keyi[k][(i - 1) * 4 + j]
    for i in range(4):
        for j in range(4):
            statei[i][j] = keyi[i][j] ^ statei[i][j]
    # Шифрование
    for i in range(1, 10):
        subBytes(statei)
        shiftrows(statei)
        MixColumns(statei)
        for j in range(4):
            for k in range(4):
                statei[j][k] = statei[j][k] ^ keyi[j][i * 4 + k]
    subBytes(statei)
    shiftrows(statei)
    for i in range(4):
        for j in range(4):
            statei[i][j] = statei[i][j] ^ keyi[i][40 + j]
    res = [[cs(str(statei[i][j]), 16, 10) for j in range(4)] for i in range(4)]
    return res

# Функция для расшифрования
def decrypt(state, keys):
    # Формируем ключ
    statei = [[int(cs(state[i][j], 10, 16)) for j in range(4)] for i in range(4)]
    keyi = [[0]*45 for i in range(4)]
    helper = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
    for i in range(4):
        for j in range(4):
            keyi[i][j] = int(cs(keys[i][j], 10, 16))
    for i in range(1, 11):
        k = keyi[0][i * 4 - 1]
        # Сдвиг вверх
        keyi[0][i * 4] = keyi[1][i * 4 - 1]
        keyi[1][i * 4] = keyi[2][i * 4 - 1]
        keyi[2][i * 4] = keyi[3][i * 4 - 1]
        keyi[3][i * 4] = k
        # Замена с S-box
        for j in range(4):
            keyi[j][i * 4] = int(cs(Sbox[(keyi[j][i * 4] & 240) >> 4][keyi[j][i * 4] & 15], 10, 16))
        keyi[0][i * 4] = keyi[0][i * 4] ^ keyi[0][i * 4 - 4] ^ helper[i]
        for j in range(1, 4):
            keyi[j][i * 4] = keyi[j][i * 4] ^ keyi[j][i * 4 - 4]
        for j in range(1, 4):
            for k in range(4):
                keyi[k][i * 4 + j] = keyi[k][i * 4 - 1 + j] ^ keyi[k][i * 4 - 4 + j]
    # Расшифрование
    for i in range(4):
        for j in range(4):
            statei[i][j] = statei[i][j] ^ keyi[i][40 + j]
    for i in range(1, 10):
        shiftrows(statei, True)
        subBytes(statei, True)
        for j in range(4):
            for k in range(4):
                statei[j][k] = statei[j][k] ^ keyi[j][40 - i * 4 + k]
        MixColumns(statei, True)
    shiftrows(statei, True)
    subBytes(statei, True)
    for i in range(4):
        for j in range(4):
            statei[i][j] = keyi[i][j] ^ statei[i][j]
    res = [[cs(str(statei[i][j]), 16, 10) for j in range(4)] for i in range(4)]
    return res

dict = {}
with open('Save.txt') as sav:
    counter = 0
    keymem = []
    cipher = []
    for line in sav:
        if counter in [0,1,2,3]:
            keymem.append(tuple(line.strip('\n').split()))
            counter += 1
        elif counter in [5,6,7,8]:
            cipher.append(line.strip('\n').split())
            counter +=1
        elif counter == 4:
            counter += 1
        elif counter == 9:
            dict[tuple(keymem)] = cipher
            keymem = []
            cipher = []
            counter = 0
print(dict)

base = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
key = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
print('Введите данные по столбцам через пробел')
# Ввод данных
base[0][0], base[1][0], base[2][0], base[3][0] = input('Первый столбец: ').split()
base[0][1], base[1][1], base[2][1], base[3][1] = input('Второй столбец: ').split()
base[0][2], base[1][2], base[2][2], base[3][2] = input('Третий столбец: ').split()
base[0][3], base[1][3], base[2][3], base[3][3] = input('Четвертый столбец: ').split()
# Ввод ключа
print('Введите ключ по столбцам через пробел')
key[0][0], key[1][0], key[2][0], key[3][0] = input('Первый столбец: ').split()
key[0][1], key[1][1], key[2][1], key[3][1] = input('Второй столбец: ').split()
key[0][2], key[1][2], key[2][2], key[3][2] = input('Третий столбец: ').split()
key[0][3], key[1][3], key[2][3], key[3][3] = input('Четвертый столбец: ').split()
# Выбор процедуры
print('Выберите процедуру:\n1.Расшифровать\n2.Зашифровать')
choice = input('1 или 2: ')
print('Исходные данные')
for i in range(4):
    for j in range(4):
        print(str(base[i][j]).ljust(3), end=' ')
    print()
checker = tuple(tuple(i) for i in key)
if choice == '1':
    if base in dict.values():
        if dict[checker] == base:
            dec = decrypt(base, key)
            print('Расшифрованное')
            for i in range(4):
                for j in range(4):
                    print(str(dec[i][j]).ljust(3), end=' ')
                print()
        else:
            print('Неподходящий ключ, пожалуйста, введите другой')
    else:
        print('Такого текста нет, введите другой')
elif choice == '2':
    enc = encrypt(base, key)
    print('Зашифрованное')
    for i in range(4):
        for j in range(4):
            print(str(enc[i][j]).ljust(3), end=' ')
        print()
    with open('Save.txt', 'a') as save:
        for i in range(4):
            save.write(" ".join(key[i]) + '\n')
        save.write('\n')
        for j in range(4):
            save.write(" ".join(enc[j]) + '\n')
        save.write('\n')
else:
    print('Неправильное значение, пожалуйста, попробуйте снова.')