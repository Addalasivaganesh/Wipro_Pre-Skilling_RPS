# import sqlite3
# conn = sqlite3.connect('company.db')
# cursor= conn.cursor()
#
#
# cursor.execute(
#     """
# INSERT INTO preparation_data (name, department, salary)
# VALUES (?, ?, ?);
# """,('Addala siva ganesh', 'IT', '50000')
# )
#
#
# #save changes
# conn.commit()
#
# print("Data inserted successfully")
# conn.close()