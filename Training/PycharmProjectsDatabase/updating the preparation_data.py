# import sqlite3
# conn = sqlite3.connect('company.db')
# cursor= conn.cursor()
#
# cursor.execute("""
# update preparation_data
# set salary = ?
# where id = ?
# """, (60000, 1))
#
#
# #save changes
# conn.commit()
#
# print("Data updated successfully")
# conn.close()