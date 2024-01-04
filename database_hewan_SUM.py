import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM(JML_SKRNG) FROM HEWAN")
total_hewan = kursor.fetchone()[0]

print(f"Total populasi hewan langka saaat ini adalah: {total_hewan} ekor")
kursor.close()