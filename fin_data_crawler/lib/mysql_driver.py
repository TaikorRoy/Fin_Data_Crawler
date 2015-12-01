# -*- coding: utf-8 -*-

import MySQLdb


class MySQLdriver(object):
    def __init__(self, _host, _user, _passwd, _db):
        self.db = MySQLdb.Connect(
            host=_host,
            user=_user,
            passwd=_passwd,
            db=_db
        )
        self.db.query('SET NAMES utf8')
        self.cursor = self.db.cursor()

    def insert(self, sql):
        sql = sql.encode('utf8')
        self.cursor.execute(sql)
        self.db.commit()

    def check_records(self, sql):
        flag = False
        sql = sql.encode('utf8')
        self.cursor.execute(sql)
        self.db.commit()
        result = self.cursor.fetchall()
        match = result[0][0]
        if match > 0:
            flag = True
        return flag

    def clean_up(self):
        self.db.close()


if __name__ == "__main__":
    mysql_host = "pubtopic.org"
    username = "roy"
    pw = "dBJky2AtHVF391cUOms5"
    db = "fin_mysql_db"
    mysql = MySQLdriver(mysql_host, username, pw, db)
    sql = "select count(*) from profitability_ratios where code = 13"
    result = mysql.check_records(sql)
    a = 1




