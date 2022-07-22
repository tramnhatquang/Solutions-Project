def timeConversion(s):
    # Write your code here
    ## First approach
    # time = s[-2]
    # res = ''
    # if time == 'A':
    #     if s[:2] == '12':
    #         res += '00' + s[2:-2]
    #     else:
    #         res = s[:-2]
    # else:
    #     if int(s[:2]) < 12:
    #         res += str(int(s[:2]) + 12) + s[2:-2]
    #     else:
    #         res = s[:-2]
    # return res

    ## More elegant code
    if s.endswith('AM'):
        return '00' + s[2:-2] if s[:2] == '12' else s[:-2]

    return str(12 + int(s[:2]) % 12) + s[2:-2]
