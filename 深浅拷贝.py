#-*-coding:utf-8-*-
# Author:Lu Wei
'''
-浅拷贝：拷贝第一层
-深拷贝：拷贝嵌套层次中所有可变类型数据（list dict set)

#---特殊情况
#v1=(1,2,3,4) #同一个
v1=(1,2,3,[1,2,3])#浅copy相同。深copy不同，需要新建新的内存地址copy元组
'''

import copy
v1='@1231231f'
v2=copy.deepcopy(v1)
print(id(v1),id(v2))

'''
import copy
#v1=(1,2,3,4) #同一个
v1=(1,2,3,[1,2,3])#浅copy相同。深copy不同，需要新建新的内存地址copy元组
v2=copy.copy(v1)
print(id(v1),id(v2))
v3=copy.deepcopy(v1)
print(id(v1),id(v3))
'''