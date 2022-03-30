# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


if __name__ == '__main__':
    number = input()
    print(abs(complex(number)))
    print(cmath.phase(complex(number)))

