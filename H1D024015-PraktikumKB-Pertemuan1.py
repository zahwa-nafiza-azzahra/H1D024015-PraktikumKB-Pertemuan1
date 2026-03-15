import random
import statistics

print("=== GAME TEBAK ANGKA ===")
angka_rahasia = random.randint(1, 20)
tebakan_list = []

print("Saya memikirkan angka 1–20. Tebak ya!")

while True:
    tebakan = input("Tebakanmu: ")
    if tebakan.lower() == "stop":
        break
    
    if tebakan.isdigit():
        t = int(tebakan)
        tebakan_list.append(t)
        
        if t == angka_rahasia:
            print("BENAR! Angka rahasianya", angka_rahasia)
            break
        elif t < angka_rahasia:
            print("Terlalu kecil!")
        else:
            print("Terlalu besar!")
    else:
        print("Masukkan angka!")

if tebakan_list:
    print("\nSemua tebakanmu:", tebakan_list)
    print("Rata-rata tebakan (statistics):", statistics.mean(tebakan_list))
    print("Tebakan acak dari listmu:", random.choice(tebakan_list))
else:
    print("Tidak ada tebakan.")