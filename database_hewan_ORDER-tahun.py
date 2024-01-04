import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# URUTKAN NAMA HEWAN BERDASARKAN TAHUN TERLAMA KE TERBARU
kursor.execute("SELECT * FROM HEWAN ORDER BY THN_DITEMUKAN ASC")
baris_tabel = kursor.fetchall()

print("DATA HEWAN")
print("="*125)
print("{:<15}{:<20}{:<20}{:<25}{:<20}{:<20}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*125)

for baris in baris_tabel:
    print("{:<15}{:<20}{:<20}{:<25}{:<20}{:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
print("-"*125)

koneksi.close()