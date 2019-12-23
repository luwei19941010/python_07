#-*- coding:utf-8 -*-
# Author:Lu Wei

########### r+ 可读可写######
'''
读取：根据光标位置，往后面进行读取
写入：根据光标位置，从当前光标位置开始进行写入操作(可能会将当前光标后面的文字覆盖 。


file_object=open('text.txt',mode='r+',encoding='UTF-8')
file_object.seek(3)#调整光标的位置
#file_object.write('按谁的')
content=file_object.read()
print(content)
#file_object.write('按谁的')
#print(content)
file_object.close()


############## w+  写入时会将文件清空，读取时需要调整光标
file_object=open('text.txt',mode='w+',encoding='UTF-8')
data=file_object.read()
print(data)
file_object.write('四大去问')
file_object.seek(0)#读取的时候 根据光标的位置读取光标后面的内容
data=file_object.read()
print(data)
file_object.close()
'''


############# a+
file_object=open('text.txt',mode='a+',encoding='UTF-8')
# file_object.seek(0)#调整光标可以调整读内容
# data=file_object.read()
# print(data)
file_object.seek(0)
file_object.write('55')#写的时候不管如何调整光标，都是在内容最后追加
file_object.close()





























