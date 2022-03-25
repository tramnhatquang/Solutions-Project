# Read input from STDIN. Print output to STDOUT
import re
while True:
    try:
        line = input().rstrip()
        op, typ, word = line.split(';')
        if op == 'S':
            if typ == 'M':
                new_word = word[:-2]
            else:
                new_word = word
            line = re.sub('(\w)([A-Z])', r'\1 \2', new_word).lower()
            print(line.lower())

        else: # op == 'C'
            new_word = word.title()
            line = re.sub(r' ', r'', new_word)
            m = line[:1].lower() + line[1:]

            if typ == 'M':
                print(m + '()')
            elif typ == 'C':
                print(line)
            else:
                print(m)

    except EOFError:
        break

if __name__ == '__main__':
    pass
