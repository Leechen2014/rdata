import os
import numpy as np
path = '../data/'
headFile = '100.hea'
atrFile = '/100.atr'

Samples2Read = 512

'''
头文件 读取

'''
f = open(path+headFile, encoding='UTF-8')
data = f.readline()
lineData = data.split(sep=' ')
print(lineData)

fileName = lineData[0] # 读取第一行
nosig = int(lineData[1])  # 信道数目
print('信道的数目', nosig)
sfreq = lineData[2]  # 采样频率
print('采样的频率', sfreq)

#  声明字典....
fName= []  ## 对应的数据名称  [] list   {} dict
dFormat=[] # 数据的格式
gain=[] # 每mV 包含的整数个数
bitres=[] # 采样的精度
zerovalue = [] # 信号中的零点值
fristvalue=[] # 信号文件中的第一个整数值  用于校验
'''
解析 hea 文件
'''
for i in range(nosig):
    strline = f.readline()
    lines = strline.split(' ')
    print('第', (i + 1), '行的数据:')
    fName.append(lines[0])  # 文件名称
    dFormat.append(int(lines[1]))
    gain.append(int(lines[2]))
    bitres.append(int(lines[3]))
    zerovalue.append(int(lines[4]))
    fristvalue.append(int(lines[5]))
    print(strline)
f.close()

print(dFormat)

'''校验'''
if dFormat in [212, 212]:
    print('hea文件格式错误....')
    exit()

f = open(path+fName[0],mode='br') ## r  可读, b 以二进制的形式读取
data = f.read()










