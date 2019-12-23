### day07

##### 今日内容

- 深浅拷贝
- 文件操作

##### ###1.深浅拷贝

int，str，bool的深浅拷贝都一致，都是新创建一块内存地址进行复制，理论上内存地址应该不一样，但是由于python常见数据类型导致是一样的。

![image-20191222214526382](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191222214526382.png)



list，set，dict浅拷贝只拷贝第一层外壳。

list，set, dict深拷贝找到所有层次中可变类型进行拷贝，不可变类型不进行拷贝。

![image-20191222214343689](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191222214343689.png)



##### 小总结：

-浅拷贝：拷贝第一层-

深拷贝：拷贝嵌套层次中所有可变类型数据（list dict set)#---特殊情况

#v1=(1,2,3,4) #同一个

v1=(1,2,3,[1,2,3])#浅copy相同。深copy不同，需要新建新的内存地址copy元组

```
'''
import copy
v1='@1231231f'
v2=copy.copy(v1)
print(id(v1),id(v2))
'''
import copy
#v1=(1,2,3,4) #同一个
v1=(1,2,3,[1,2,3])#浅copy相同。深copy不同，需要新建新的内存地址copy元组
v2=copy.copy(v1)
print(id(v1),id(v2))
v3=copy.deepcopy(v1)
print(id(v1),id(v3))
```



##### ###2.文件操作

内存中编码 unicode，

- ​	打开
  - r,只能读。
  - w,只能写，写之前清空。
  - a,只能追加。
  - r+
    - 读：默认从0的光标位置开始读，可以通过seek调整光标的位置开始读
    - 写：从光标所在的位置开始写，可以通过seek调整光标的位置，从而开始写。
  - w+
    - 读：默认光标永远在写入的最后或0，可以通过seek调整光标的位置进行读取。
    - 写：先清空再写入
  - a+
    - 读：默认光标在最后，可以通过seek调整光标的位置，然后再去读取
    - 写：永远写到最后
- ​	操作
  - 读
    - read()
    - read(2)##注意：2表示字符不是字节
    - readlines()###读取每一行，以列表形式给到。
  - write
- ​	关闭





##### 今日总结

- 深浅拷贝
  - 深浅拷贝对不可变类型不进行拷贝
  - 深拷贝对所以层次的可变类型进行拷贝
- 文件操作
  - 打开
  - 操作
  - 关闭
- 文件操作和数据类型的结合使用

