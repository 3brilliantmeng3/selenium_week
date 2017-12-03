#1.首先导入pymysql
import pymysql
def connectDb():

    # 链接数据库需要那些信息
    # IP地址,端口号,用户名和密码,数据库的名称.........
    coon = pymysql.Connect(host="127.0.0.1",user="root",password="root",database="pirate",port=3306,charset="utf8")

    sql = "select * from hd_user order by id desc"
    # 要想在代码中执行这条sql语句,首先要获取数据库的 游标 cursor
    curs=coon.cursor()
    curs.execute(sql)
    # 想获取数据库中最新的记录,fetchone()
    # 那么就要把数据所有记录倒叙排列
    # 然后用sfetchone() 获取第一条记录,几最新记录
    result = curs.fetchone()
    # 如果获取所有的查询结果,fetchall()
    return result
if __name__ == '__main__':
   print (connectDb())
