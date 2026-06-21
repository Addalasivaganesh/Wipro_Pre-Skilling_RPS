import sqlite3

conn = sqlite3.connect('company.db')
cursor= conn.cursor()

cursor.execute("""
DELETE FROM preparation_data
where id = ?
""", (1,))


#save changes
conn.commit()

print("Data deleted successfully")
conn.close()