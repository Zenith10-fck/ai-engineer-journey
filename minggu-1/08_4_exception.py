# Minggu 1 - Task 08 - Bagian 4: exception handling (try / except)


def bagi(a: int, b: int) -> float:
    return a / b


print(bagi(10, 2))  # 5.0 (operator / selalu menghasilkan float)

# Tanpa penjagaan, bagi(10, 0) akan crash dengan ZeroDivisionError
# dan baris sesudahnya tidak dijalankan.

# Dengan try / except, program tetap lanjut
try:
    print(bagi(10, 0))
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")

print("Selesai")


# Penjagaan dipindahkan ke dalam fungsi
def bagi_aman(a: int, b: int) -> None:
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Tidak bisa dibagi dengan nol")


bagi_aman(10, 2)  # 5.0
bagi_aman(10, 0)  # Tidak bisa dibagi dengan nol
