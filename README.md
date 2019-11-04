# --ASCII_encryption
## 对字符串进行加密和解密
* encoder为加密文件
* decoder为解密文件
* 所需环境为python3.x&numpy
* 激活环境并进入项目根目录，运行encoder文件，并输入加密字符串，得到加密后的字符串：
```
python encoder.py
输入字符：www.baidu.com
x|y1ffok}7dto
```
*运行decoder文件，输入解密字符串，得到原始字符串：
```
python decoder.py
输入字符：x|y1ffok}7dto
www.baidu.com
```