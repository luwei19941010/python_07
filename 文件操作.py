#-*-coding:utf-8-*-
# Author:Lu Wei



###########读 r 只读不能写 + 文件不存在报错#########
'''
file_object=open('text.txt',mode='r',encoding='utf-8')#mode='r=read(只读),w=white('只写'),a=append('追加')
context=file_object.read()
print(context)
file_object.close()


##########写 w 只写不能读，先清空，再写+文件不存在，则新建##########
file_object=open('text1.txt',mode='w',encoding='utf-8')#mode='r=read(只读),w=white('只写,先清空，一般用于新建文件'),a=append('追加')
file_object.write('123')
file_object.close()


########追加 a 追加，只追加不能读+文件不存在，则新建###########
file_object=open('text.txt',mode='a',encoding='utf-8')#mode='r=read(只读),w=white('只写,先清空，一般用于新建文件'),a=append('追加')
file_object.write('a123123')
file_object.close()
'''

