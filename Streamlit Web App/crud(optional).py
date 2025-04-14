import mysql.connector
import streamlit as st

mydb = None  
mycursor = None 

def main():
    global mydb, mycursor  
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",        #? not mine, for safety
            database="crud_new1"
        )
        mycursor = mydb.cursor()
        print("Connection Established")

        st.title("CRUD Operations With MySQL")
        option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

        if option == "Create":
            st.subheader("Create a Record")
            name = st.text_input("Enter Name")
            email = st.text_input("Enter Email")
            if st.button("Create"):
                sql = "insert into users(name,email) values(%s,%s)"
                val = (name, email)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!!!")

        elif option == "Read":
            st.subheader("Read Records")
            mycursor.execute("select * from users")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

        elif option == "Update":
            st.subheader("Update a Record")
            id = st.number_input("Enter ID", min_value=1)
            name = st.text_input("Enter New Name")
            email = st.text_input("Enter New Email")
            if st.button("Update"):
                sql = "update users set name=%s, email=%s where id =%s"
                val = (name, email, id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Updated Successfully!!!")

        elif option == "Delete":
            st.subheader("Delete a Record")
            id = st.number_input("Enter ID", min_value=1)
            if st.button("Delete"):
                sql = "delete from users where id =%s"
                val = (id,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Deleted Successfully!!!")

    finally:
        if mycursor:
            mycursor.close()
            print("Cursor Closed")
        if mydb and mydb.is_connected():
            mydb.close()
            print("Connection Closed")

if __name__ == "__main__":
    main()