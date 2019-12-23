#-*-coding:utf-8-*-
# Author:Lu Wei

#####################读操作####################

file_object=open('text.txt',mode='r',encoding='utf-8')
#读取所有的内容到内存
# data=file_object.read(2)

#从当前光标所在位置向后读取2个字符。
#file_object.seek(3)
#data=file_object.read(2)

#读取所有的内容到内存，并按照每一行进行分割到列表中
data_list=file_object.readlines()
print(data_list)

#当文件特别大的时候，可以通过一行一行进行读取。
# for line in file_object:
#     print(line.strip())#.strip可以去换行符及空格
# file_object.close()

###################写操作#####################
# file_object=open('text.txt',mode='w',encoding='utf-8')
# file_object.write('hello\n')
# file_object.write('xiaohei')
# file_object.close()
print(type(data_list))
