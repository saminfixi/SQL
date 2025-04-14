import mysql.connector

try:
    conn=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="crud_python"   
    )

    mycursor = conn.cursor()
    print("Connection established")
    
except:
    print("Connection failed")


mycursor.execute("CREATE DATABASE crud_python")
conn.commit()

print("Database created")


mycursor.execute(
    """
    CREATE TABLE customers(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        age INTEGER 
    )    
    """)
conn.commit() 
print("Table has created")


mycursor.execute(
    """
    INSERT INTO customers VALUES
        (1, "Anik", "anik@gmail.com", 40),
        (2, "Rahat", "rahat@gmail.com", 24),
        (3, "Polash", "polash@gmail.com", 34)   
    """)
conn.commit()
print("Table has updated")


mycursor.execute("select * from customers")
myresult = mycursor.fetchall()    

for x in myresult:
    print(x)

mycursor.execute("update customers set age=54 where id=1")
conn.commit()
print("Updated")


mycursor.execute("delete from customers where id=1")
conn.commit()
print("Deleted")

mycursor.close()
conn.close()