from random import randint


def triangle(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a + b > c and b + c > a and c + a > b:
            if a == b == c:
                print('Равносторонний')
            elif a == b or b == c or c == a:
                print('Равнобедренный')
            else:
                print('Разносторонний')
        else:
            print('Не треугольник')
    else:
        print('Переменная(ые) не числа')


# triangle(10, 10, 10)


def simple_name(numbers):
    if numbers == 1 or numbers == 2:
        print('Простое')
    elif 0 < numbers < 100_000:
        for i in range(2, numbers):
            if numbers % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
    else:
        print('Вышел за пределы')


# simple_name(int(input('Enter number: ')))


def guess_the_number(number, attempts):
    print(f'Guess the number in {attempts} attempts.')
    while (True):
        print(f'Attempts left {attempts}.')
        num = int(input('Guess the number from 0 to 1000: '))
        attempts -= 1
        if attempts > 0:
            if num == number:
                print('right\n')
                break
            elif num > number:
                print('less\n')
            else:
                print('more\n')
        else:
            print('attempts ended')
            break


# guess_the_number(randint(0, 1000), 10)
