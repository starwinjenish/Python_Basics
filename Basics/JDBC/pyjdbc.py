import mysql.connector

def connect_to_mysql():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'ddl'
    )

    print("connected to mysql successfully")
    con.close()

if __name__ == "__main__":
    connect_to_mysql()