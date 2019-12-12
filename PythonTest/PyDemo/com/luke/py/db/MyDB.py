import mysql.connector


class MyDB:
    cursor = ''
    db = ''

    # 定义构造方法
    # host:主机明
    # username；用户名
    # passwor 密码
    # dbname  数据库名
    # db 打开的数据库连接
    # cursor  获取游标句柄
    def __init__(self, host: object, username: object, password: object, dbname: object) -> object:
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname

        self.db = mysql.connector.connect(
            host=self.host,
            port='3306',
            user=self.username,
            passwd=self.password,
            db=self.dbname
        )

        self.cursor=self.db.cursor()

    #获取所有结果集
    def getAllResult(self,sql):
        self.cursor.execute(sql)
        results=self.cursor.fetchone()
        return  results
    #插入或更新数据
    def insertOrUpdateInfo(self,sql):
        print(sql)
        try:
            #执行sql语句
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        #返回受影响的行数
        return self.cursor.rowcount
    #关闭连接
    def close(self):
        self.db.close()