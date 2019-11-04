import numpy as np


def decoder(text):
    decoder = []
    for i in range(len(text)):
        decode_i = chr(int(text[i])-10)
        decoder.append(decode_i)
    decoder = ''.join(decoder)
    return decoder
	

def str_trans_list(text):
	a = []
	b = []
	a = text.strip('[').strip(']').split(', ')
	for i in range(len(a)):
		b.append(int(a[i]))
	return b 
	
	
decode_char = input('输入字符：')
decode_char = str_trans_list(decode_char)
outputs = decoder(decode_char)
print(outputs)
