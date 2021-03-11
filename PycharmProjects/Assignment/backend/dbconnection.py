
import mysql.connector as ms


class DBConnect:
    def __init__(self):
        self.con = ms.connect(host='localhost', user='root', password='manish1#',
                              database='student_management')
        self.cur = self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        self.cur.execute(query, values)
        records = self.cur.fetchall()
        return records

    def select2(self, query):
        self.cur.execute(query)
        records = self.cur.fetchall()
        return records

    def update(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()


