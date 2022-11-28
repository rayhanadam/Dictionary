# Rayhan Adam Aria
# TI.22.B1

# import tabulate
from tabulate import tabulate
# membuat dictionary
dict = {'Nama': ['Ari', 'Dina'], 'Nomor Telepon': [628823234647, 6288999776]}

# menampilkan kontak rayhan pada dictionary
print("Menambahkan data baru")
print(dict['Nomor Telepon'][0])
print('')

# menambahkan data baru Nama dan Nomor Telepon
print("Menambahkan data baru")
dict['Nama'].append('Riko')
dict['Nomor Telepon'].append('087654544')
print(dict)

# merubah kontak Adam
# mencari nama Adam apakah ada didalam data dictionary
if 'Adam' in dict['Nama']:
    # Jika ada, cari position Adam adai di index berapa
    AdamIndex = dict['Nama'].index('Adam')
    # Lalu dapatkan index untuk merubah Nomor Telepon
    dict['Nomor Telepon'][AdamIndex] = 6243538987
else:
    print("Tidak ada nama Adam")
print("Merubah Nomor Telepon Adam")
print(dict)

# Menampilkan semua nama
print("Menampilkan semua Nama")
print(dict['Nama'])

# Menampilkan semua Nomor Telepon
print("Menampilkan semua Nomor Telepon")
print(dict['Nomor Telepon'])

# Menampilkan semua Nama & Nomor Telepon
print("Menampilkan semua Nama & Nomor Telepon")
print(tabulate(dict, headers=["Nama", "Nomor Telepon"], tablefmt="fancy_grid"))