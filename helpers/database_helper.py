import mysql.connector


class Database:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="uu_code_challenge"
        )
        self.cursor = self.con.cursor()

    def run_query(self, query_sql):
        self.cursor.execute(query_sql)
        rows = self.cursor.fetchall()
        self.con.commit()
        return rows

    # Ensure we clean up the db instance
    def __del__(self):
        self.cursor.close()
        self.con.close()