# crc sender
data = input('enter input')
divisor = "1101"

p = len(divisor)

divident = data + '0' * (p - 1)

tmp = divident[0: p]


def xor(a, b):
    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


while p < len(divident):

    if tmp[0] == '1':

        tmp = xor(divisor, tmp) + divident[p]
    else:

        tmp = xor('0' * p, tmp) + divident[p]

    p += 1

if tmp[0] == '1':
    tmp = xor(divisor, tmp)
else:
    tmp = xor('0' * p, tmp)

checkword = tmp
print('enter the checkword:', checkword)

codeword = data + checkword

print('enter the codeddata:', codeword)