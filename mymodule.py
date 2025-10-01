name = 'Stas'

def say():
    print('Hello,', name)

def summa():
    x = 0
    while x == 0:
        try:
            a = int(input('Введи число: '))
            b = int(input('Введи число: '))
            c = int(input('Введи число: '))

            if a != 0 and b != 0 and c != 0:
                print(a + b + c)
                x += 1
            else:
                print("Есть нули")
        except ValueError:
            print('Некорректный ввод')


