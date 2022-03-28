if __name__ == '__main__':
    for i in range(1, 16):
        if i % 3 == 0:
            print('Fizz')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz1')
            print('FizzBuzz2')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
