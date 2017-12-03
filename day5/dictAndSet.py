# dict 是字段的缩写,
# set 是集合的缩写
# 其中他们都和数组类似,python 中的元组用小括号表示()
# 列表用中括号表示[]
# 字典和集合用大括号{}
# 比如,同样描述一个学生信息
stu = ('001',"小毛","男",23)
# 元组 与数组的区别:
# 数组,可以修改,但是不能增加和删除  只能存放一种类型的元素即数组中的所有元素的类型一样
# 元组不能增删改,元素的类型不固定,可以是数字,字符串的混合

stu = ['001',"小毛","男",23]

# 元组和列表的区别 :
# 元组是只读的,不能修改
# 列表可以进行增删改查,列表是常用的数据格式
# find_elements()返回的是列表
stu = {'001',"小毛","男",23}
# 元组和集合的区别:
# 1.集合是无序,不能用下标(索引)的方式查找元素
# 2.集合是不可重复的,重复的元素会自动删除

stu = {"id":"001","姓名":"小毛","性别":"男","年龄":23,"成绩":23}
# 字典和集合的区别
# 冒号前的部分叫Key ,后面的部分叫value
# 字典具有描述性的,你看见先的Key值,就知道value所代表的意思了
# 集合是无序的,集合中的key不能重复,value 值可以重复
# 如果我想打印集合中的id 的值,怎么办
print(stu['id'])