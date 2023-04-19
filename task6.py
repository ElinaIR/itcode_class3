def is_simple(number):
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return print('Составное')
    return print('Простое')


number = int(input('Enter a number\n'))
while number < 0:
    number = int(input('Number must be >= 0\n'))

is_simple(number)

