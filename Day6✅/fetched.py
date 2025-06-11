# infetch.py

import sqlite3

# Connect to the database
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# Fetch all data
cursor.execute("SELECT text, author FROM quotes")
rows = cursor.fetchall()

# Print results
print("\n📜 Quotes from the database:\n")
for idx, row in enumerate(rows, 1):
    print(f"{idx}. {row[0]} — {row[1]}")

conn.close()
