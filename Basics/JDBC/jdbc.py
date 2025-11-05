import pymysql
import pymysql.cursors

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='ddl',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # ✅ Corrected CREATE TABLE query
        create_query = """
        CREATE TABLE IF NOT EXISTS employee (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100),
            DEPARTMENT VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        # ✅ Corrected INSERT query (only 2 values, no ID)
        insert_query = "INSERT INTO employee(NAME, DEPARTMENT) VALUES (%s, %s)"
        values = [('starwin', 'IT'), ('abisha', 'TL'), ('selvi', 'HR')]
        cursor.executemany(insert_query, values)

        # Commit changes
        connection.commit()

        # ✅ SELECT query
        select_query = "SELECT * FROM employee"
        cursor.execute(select_query)
        result = cursor.fetchall()

        # ✅ Print result
        for row in result:
            print(row)

finally:
    connection.close()

