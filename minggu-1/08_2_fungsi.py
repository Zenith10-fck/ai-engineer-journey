# Minggu 1 - Task 08 - Bagian 2: fungsi (def, return, type hint)


def sapa(nama: str) -> str:
    return "Halo, " + nama


print(sapa("Ahmad"))  # Halo, Ahmad


def kuadrat(x: int) -> int:
    return x * x


print(kuadrat(5))  # 25
