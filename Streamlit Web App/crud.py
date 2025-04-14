import mysql.connector
import streamlit as st

def main():
    st.title("CRUD Operations With MySQL")
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",        #? not mine, for safety
            database="crud_new1"
        ) as mydb:
            print("Connection Established")
            with mydb.cursor() as mycursor:
                print("Cursor Created")

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

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        print("Operation completed, connections will be closed automatically.")

if __name__ == "__main__":
    main()