# Minggu 1 - Task 08 - Bagian 3: perulangan dan list comprehension

angka_list: list[int] = [1, 2, 3, 4, 5]

# Perulangan biasa: mencetak satu-satu
for a in angka_list:
    print(a * 2)  # 2, 4, 6, 8, 10

# Comprehension: hasilnya dikumpulkan ke list baru
kuadrat_list: list[int] = [a * a for a in angka_list]
print(kuadrat_list)  # [1, 4, 9, 16, 25]

# Comprehension dengan penyaring (if)
genap: list[int] = [a for a in angka_list if a % 2 == 0]
print(genap)  # [2, 4]

# Latihan gabungan: angka 1-10, ambil genap, kuadratkan
angka_10: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hasil_genap: list[int] = [a * a for a in angka_10 if a % 2 == 0]
print(hasil_genap)  # [4, 16, 36, 64, 100]
