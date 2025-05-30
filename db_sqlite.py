import sqlite3

conn = sqlite3.connect('mydatabase.db')


cursor = conn.cursor()


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER
#     )
# ''')

# Save changes and close connection
conn.commit()
conn.close()