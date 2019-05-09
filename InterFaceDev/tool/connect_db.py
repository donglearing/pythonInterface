#coding:utf-8
import MySQLdb
import json
class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(host='10.128.0.192',port=3306,user='root',passwd='Connext@0101',db='cloudproject_pg',charset='utf8')
        self.cur = self.conn.cursor()
        #self.conn = MySQLdb.cursors(host='localhost',port=3306,user='root',passwd='1234',db='cloud',charset='utf8',cursorclass=MySQLdb.cursors.DictCursor)
        #self.cur = self.conn.cursor()

    def search_one(self,sql):
        #self.cur.execute(sql)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        print (result)
        print("wwwwwwwwwwwwwwwwww")

        #result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from application")
    #res.decode('unicode-escape')
    #res.decode()
    #print res.decode('unicode-escape')
    print (res[0])

    for i in range(len(res)):
        print (res[i])
        #print res1