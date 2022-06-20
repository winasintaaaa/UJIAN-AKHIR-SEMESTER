data = []

while True:
    pengguna = input ("Masukkan angka: ")
    if pengguna == "n":
        break
    data.append(int(pengguna))

total = sum(data)
rata = total/len(data)
print("rata data", rata)