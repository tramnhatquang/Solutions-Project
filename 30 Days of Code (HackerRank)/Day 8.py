# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    num_entries = int(input().strip())
    dic = {}

    for _ in range(num_entries):
        name, phone_num = input().split()
        if name not in dic:
            dic[name] = phone_num

    while True:
        try:
            query = input().strip()
            if query in dic:
                print(f'{query}={dic[query]}')
            else:
                print('Not found')
        except EOFError:
            break