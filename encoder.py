import numpy as np

key = list('15234567890')
outputs = []


def encoder(text):
    encode = []
    for i in range(len(text)):
        encode_i = ord(text[i])
        k = key[i % 10]
        encode.append(encode_i + int(k))
    np.array(encode, dtype=np.uint8)
    return encode


encode_char = input('输入字符：')
output = encoder(encode_char)
for i in range(len(encode_char)):
    c = chr(output[i])
    outputs.append(c)

print(''.join(outputs))
