# Catatan Materi: Minggu 1, Task 08 (Python Core)

Dokumen ini merangkum apa yang dipelajari di commit ini. Kode latihannya ada di file `08_1` sampai `08_5` di folder yang sama.

Cara menjalankan tiap file:

```
uv run --python 3.12 nama_file.py
```

---

## 1. Variabel dan type hint (`08_1_variabel_type.py`)

**Variabel** adalah kotak bernama yang menyimpan nilai.

```python
nama: str = "ahmad"
```

- `nama` = nama kotak
- `: str` = label jenis isinya (type hint)
- `= "ahmad"` = isi kotak

| Jenis | Isi | Contoh |
|---|---|---|
| `str` | teks | `"ahmad"` |
| `int` | bilangan bulat | `21` |
| `float` | pecahan | `1.7` |
| `bool` | benar atau salah | `True` |

**Poin penting**

- Tanda kutip menentukan jenis nilai. `"21"` adalah teks, `21` adalah angka.
- Type hint hanya label untuk manusia dan alat bantu. Python **tidak** memeriksanya saat program jalan. Label `: int` dengan isi `"7"` tetap berjalan tanpa error.
- `type(nilai)` menunjukkan jenis nilai yang sebenarnya, misalnya `<class 'int'>`.
- Nama variabel Python biasanya huruf kecil semua.

---

## 2. Fungsi (`08_2_fungsi.py`)

```python
def kuadrat(x: int) -> int:
    return x * x
```

| Bagian | Arti |
|---|---|
| `def kuadrat` | membuat resep bernama `kuadrat` |
| `(x: int)` | bahan yang diterima |
| `-> int` | jenis hasil yang dikembalikan (stiker) |
| `return x * x` | hasil, dihitung di sini (kerja) |

**Poin penting**

- Stiker (`-> int`) hanya berisi **nama jenis**. Hitungan tidak boleh ditaruh di sana.
- Hitungan ada di samping `return`.
- Fungsi baru berjalan kalau **dipanggil**: `print(kuadrat(5))`.
- 4 spasi di depan baris dalam fungsi adalah **wajib**. Spasi menentukan baris mana yang milik fungsi.
- `return` adalah pintu keluar. Baris sesudah `return` tidak dijalankan.
- Fungsi yang hanya mencetak dan tidak mengembalikan nilai memakai `-> None`.

---

## 3. Perulangan dan comprehension (`08_3_comprehension.py`)

**Perulangan `for`** mengulang blok yang menjorok untuk tiap isi list.

```python
for a in angka_list:
    print(a * 2)
```

**List comprehension** adalah perulangan yang ditulis satu baris, hasilnya dikumpulkan ke list baru.

```
[ HASIL   for  NAMA  in  SUMBER   if  SYARAT ]
```

| Bagian | Peran |
|---|---|
| `a * a` | apa yang dihasilkan |
| `for a in angka_10` | sumber data, dan `a` adalah nama untuk tiap isi |
| `if a % 2 == 0` | siapa yang lolos |

Contoh gabungan: `[a * a for a in angka_10 if a % 2 == 0]` menghasilkan `[4, 16, 36, 64, 100]`.

**Poin penting**

- `%` adalah sisa bagi. Angka genap sisa baginya dengan 2 adalah 0.
- `=` mengisi nilai, `==` membandingkan. Jangan tertukar.
- Comprehension **mengumpulkan** hasil, perulangan biasa dengan `print` **mencetak** satu-satu.

---

## 4. Exception handling (`08_4_exception.py`)

Error yang tidak ditangani membuat program **crash**: program berhenti total dan baris sesudahnya tidak dijalankan.

```python
try:
    print(bagi(10, 0))
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")
```

- `try:` = coba jalankan blok ini
- `except NamaError:` = kalau error jenis ini muncul, jalankan blok ini dan program lanjut
- Nama error di `except` diambil dari pesan error yang muncul saat crash.

**Poin penting**

- `10 / 2` menghasilkan `5.0`, bukan `5`. Operator `/` selalu menghasilkan float.
- `try / except` menggantikan pengecekan `if b == 0`. Tidak perlu dicek dulu, cukup coba dan tangkap kalau gagal.
- Penjagaan bisa ditaruh di dalam fungsi (`bagi_aman`), sehingga siapa pun yang memanggilnya aman.

**Cara membaca traceback**

- Baris paling bawah: jenis error dan penjelasannya (`ZeroDivisionError: division by zero`).
- Nomor baris menunjukkan tempat crash, dan itu tidak selalu baris yang baru ditulis. Panggilan lama yang belum dibungkus `try` bisa crash lebih dulu.
- `RecursionError` dan `[Previous line repeated N more times]` berarti fungsi memanggil dirinya sendiri tanpa henti. Di dalam `bagi_aman`, hitung `a / b` langsung, jangan panggil `bagi_aman` lagi.

---

## 5. Dictionary, for, dan if (`08_5_dictionary.py`)

**Dictionary** adalah kumpulan pasangan kunci dan nilai.

```python
umur_teman: dict[str, int] = {"Budi": 20, "Sari": 22}
umur_teman["Sari"]     # 22, ambil nilai lewat KUNCI
```

- Cari dari kunci ke nilai, tidak sebaliknya. `audit["belum bisa"]` gagal dengan `KeyError` karena `"belum bisa"` adalah nilai, bukan kunci.
- `.items()` memberi pasangan kunci dan nilai untuk diulang: `for nama, umur in umur_teman.items():`.

**`if`** artinya "kalau". Baris di bawahnya hanya dijalankan kalau syaratnya benar.

```python
for skill, kemampuan in audit_romdhon.items():
    if kemampuan == "belum bisa":
        print(skill)
```

**Poin penting**

- Titik dua `:` wajib di ujung baris `def`, `for`, `if`, `try`, dan `except`.
- Membandingkan teks harus persis sama, termasuk huruf besar dan kecil. `"Butuh bantuan"` tidak sama dengan `"butuh bantuan"`.

---

## Kebiasaan yang terbentuk minggu ini

- Menebak output **sebelum** menjalankan kode.
- Membaca pesan error dari bawah ke atas: jenis error, lalu nomor baris.
- Satu topik satu file, supaya bukti belajar tetap utuh.
- Commit ke GitHub setelah sesi belajar selesai.
