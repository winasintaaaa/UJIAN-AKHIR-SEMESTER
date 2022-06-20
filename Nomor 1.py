data = [
    {
        "Nama": "Ni Luh WIna Sinta Ariesta",
        "NIM": "42130092",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "Nama": "Cantika Wijaya",
        "NIM": "421313248",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "Nama": "Adi Saputra",
        "NIM": "42130086",
        "Jurusan": "Teknologi Informasi"
    }

]

print("Silahkan Pilih Nama Mahasiswa Berikut : ")
print("1. Ni Luh Wina Sinta Ariesta")
print("2. Cantika Wijaya")
print("3. Adi Saputra")

input = input("\nMasukkanlah Angka 1 sampai 3 :")


if input == '1':
    print("Nama = ", data[0]['Nama'])
    print("Nim = ", data[0]['NIM'])
    print("Jurusan = ", data[0]['Jurusan'])

elif input == '2':
    print("Nama = ", data[1]['Nama'])
    print("Nim = ", data[1]['NIM'])
    print("Jurusan = ", data[1]['Jurusan'])
else:
    print("Nama = ", data[2]['Nama'])
    print("Nim = ", data[2]['NIM'])
    print("Jurusan = ", data[2]['Jurusan'])
