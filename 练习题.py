#-*-coding:utf-8-*-
# Author:Lu Wei

#1.
# user=['alex','eric']
# data='_'.join(user)
# file_object=open('log.txt',mode='w',encoding='utf-8')
# file_object.write(data)
# file_object.close()
# print(data)

#2.
'''
user=[
    {'user':'alex','psd':'123'},
{'user':'eric','psd':'oldbody'}
]
#alex|123
#eric|oldbody

i=0
file_object=open('log.txt',mode='w',encoding='utf-8')
while True:
    user_list = []
    user_list.append(user[i]['user'])
    user_list.append(user[i]['psd'])
    data='|'.join(user_list)
    i+=1
    print(data)
    file_object.write(data)
    file_object.write('\n')
    if i >=len(user):#2
        break
file_object.close()
'''
'''
file_object=open('log.txt',mode='w',encoding='utf-8')
for item in user:
    line='%s|%s\n'%(item['user'],item['psd'])
    file_object.write(line)
file_object.close()
'''

#3.读取log.txt 放入列表['alex|123','eric|oldbody']
'''
#方式一
file_object=open('log.txt',mode='r',encoding='utf-8')
user_list=[]
for i in file_object:
    user_list.append(i.strip())
file_object.close()
print(user_list)

#方式二
file_object=open('log.txt',mode='r',encoding='utf-8')
data=file_object.read()
file_object.close()
content=data.strip().split('\n')
print(content)
'''









