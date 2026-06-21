# import sqlite3
#
# #1.Connecting to Data base
# connection = sqlite3.connect('company.db')
#
# #2. Create a cursor
# cursor= connection.cursor()
#
# #DROP TABLE
# cursor.execute("""
# DROP TABLE IF EXISTS employees;
# """)
#
# # Create Table, Insert Data, Update Data, Delete Data
# #3. Create Table
# cursor.execute("""
# CREATE TABLE employees (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# department TEXT,
# salary REAL);
# """)
# #save changes
# connection.commit()
# print("Database and table created successfully")
#
# #4. Insert data
# cursor.execute("""
# INSERT INTO employees(name, department, salary)
# VALUES('Addala siva ganesh', 'IT', '50000');
# """)
# cursor.execute("""
# INSERT INTO employees(name, department, salary)
# VALUES('Raja', 'NON-IT', '35000');
#
# """)
# #save changes
# connection.commit()
# print("Data Inserted successfully")
#
# #5. Read the data
#
# cursor.execute("SELECT * from employees")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# #6. update data
#
# cursor.execute("""
# UPDATE employees
# SET salary = 55000
# WHERE id = 1
# """)
#
# connection.commit()
# print("Data Updated successfully")
#
# #reading the data again
# cursor.execute("SELECT * from employees")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
#
#
# #7. delete the data
#
# cursor.execute("""
# DELETE FROM employees
#     where id = 2;
# """)
#
#
#
# connection.commit()
#
# connection.close()
# print("SQLite CRUD operations completed")
