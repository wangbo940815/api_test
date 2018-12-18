import pymysql
# ip:120.78.128.25
# username:futurevistor
# password:123456
#port :3306
#数据库操作步骤，1引入API模块。2获取与数据库的连接，3执行SQL语句和存储过程，4关闭数据库连接
#http://120.78.128.25:8080/futureloan/mvc/api/member/login
class Connect_db:
    def __init__(self,ip,username,password,dbname):
        self.db = pymysql.connect(ip,username,password,dbname,charset="utf8")
    def Execu_sql(self,*sql):
        self.cursor = self.db.cursor()
        for i in sql:
            self.cursor.execute(i)
        """关闭连接"""
        data = self.cursor.fetchall()
        return  data  
    def commit(self):
        self.db.commit()
    def close(self):
        self.cursor.close()
        self.db.close()
        
a=Connect_db("120.78.128.25","futurevistor","123456","future")
b=a.Execu_sql("show tables")
c=a.Execu_sql("select * from loan ")
a.close()

print(b)      
print(c)   
