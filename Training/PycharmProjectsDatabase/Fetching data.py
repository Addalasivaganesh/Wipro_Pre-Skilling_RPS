import sqlite3
conn = sqlite3.connect('company.db')
cursor= conn.cursor()


cursor.execute("select * from preparation_data")
preparation_data = cursor.fetchall()

for data in preparation_data:
    print(data)


print("Data fetched successfully")
conn.close()