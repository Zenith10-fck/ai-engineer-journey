# Minggu 1 - Task 08 - Bagian 5: dictionary, for, dan if

umur_teman: dict[str, int] = {"Budi": 20, "Sari": 22, "Dani": 19}
print(umur_teman["Sari"])  # 22 (ambil nilai lewat kunci)

for nama, umur in umur_teman.items():
    print(nama, umur)

# Latihan: dari self-audit Minggu 0, cetak skill yang levelnya "belum bisa"
audit_romdhon: dict[str, str] = {
    "Python": "butuh bantuan",
    "FastAPI": "belum bisa",
    "Postgres": "belum bisa",
    "Docker": "butuh bantuan",
    "Claude API": "butuh bantuan",
}

for skill, kemampuan in audit_romdhon.items():
    if kemampuan == "belum bisa":
        print(skill)  # FastAPI, Postgres
