# import sqlite3
#
# connection = sqlite3.connect('company.db')
# cursor= connection.cursor()
#
# cursor.execute("""
# CREATE TABLE preparation_data(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# department TEXT,
# salary REAL
# email TEXT);
# """)



#save changes
connection.commit()

print("Database and table created successfully")
connection.close()