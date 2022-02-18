import pymysql


class DBconnect(object):
    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  port=port,
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
        # 获取游标
        self.curs = self.db.cursor()

    def select(self, sql):
        """查询语句"""
        self.curs.execute(sql)
        return self.curs.fetchall()

    def execute_sql(self, sql):
        """执行sql"""
        try:
            self.curs.execute(sql)
            self.db.commit()
        except Exception as e:
            print("错误是{}".format_map(sql))
            print(e)
            self.db.rollback()

    def close(self):
        self.curs.close()
        self.db.close()


if __name__ == '__main__':
    db = DBconnect(host="49.235.92.12",
                   user="root",
                   password="123456",
                   database="apps",
                   port=3306,
                   )
    r = db.select('select * from api where id=1')
    print(r)
    db.close()




# db = pymysql.connect(host="49.235.92.12",
#                      user="root",
#                      password="123456",
#                      database="apps",
#                      port=3306,
#                      cursorclass=pymysql.cursors.DictCursor
#                      )
# # 默认返回的结果是元组格式，添加cursorclass=pymysql.cursors.DictCursor参数 返回结果为dict
# # 创建游标
# curs = db.cursor()
# sql = 'select * from api where id=1'
# curs.execute(sql)
# result = curs.fetchall()
# # dict通过.get()或者['key']来获取对应的值
# print(result[0])



