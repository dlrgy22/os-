import pymysql

class mysql_db:
        def __init__(self, input_user, input_passwd, input_host, input_db, input_port):
                self.db = pymysql.connect(
                        user = input_user,
                        passwd = input_passwd,
                        host = input_host,
                        port = input_port,
                        db = input_db,
                        charset = 'utf8',
                        unix_socket = '/var/run/mysqld/mysqld.sock'
                )

        def execute_query(self, sql):
                self.curs = self.db.cursor()
                self.curs.execute(sql)
                self.db.commit()

