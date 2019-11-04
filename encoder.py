import numpy as np


def encoder(text):
    encode = []
    for i in range(len(text)):
        encode_i = ord(text[i])
        encode.append(encode_i+10)
    np.array(encode, dtype=np.uint8)
    return encode
	

encode_char = input('输入字符：')
outputs = encoder(encode_char)
print(outputs)