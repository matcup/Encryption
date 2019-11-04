import numpy as np

key = list('15234567890')


def decoder(text):
    decoder_num = []
    decoder_str = []
    for i in range(len(text)):
        k = key[i % 10]
        decode_i = ord(text[i]) - int(k)
        decoder_num.append(decode_i)

    for j in range(len(decoder_num)):
        a = chr(decoder_num[j])
        decoder_str.append(a)
        decoder = ''.join(decoder_str)
    return decoder


def str_trans_list(text):
    text_list = []

    for i in range(len(text)):
        b = text[i]
        text_list.append(b)
    return text_list


decode_char = input('输入字符：')
decode_char = str_trans_list(decode_char)
outputs = decoder(decode_char)
print(outputs)
