import csv
import os
from models import Tanaman

def muat_data():
    daftar_tanaman = []

    if not os.path.exists("tanaman.csv"):
        print("File tanaman.csv tidak ditemukan.")
        return daftar_tanaman

    with open("tanaman.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header

        for row in reader:
            tanaman = Tanaman(
                nama_tanaman=row[0],
                jenis_tanaman=row[1],
                volume_penyiraman=row[2],
                status=row[3]
            )
            daftar_tanaman.append(tanaman)

    return daftar_tanaman

def tampilkan_tanaman():
    daftar_tanaman = muat_data()

    if not daftar_tanaman:
        print("Tidak ada data tanaman.")
        return

    print("\n=== DAFTAR TANAMAN ===\n")

    print(f"{'Nama Tanaman':25}{'Jenis Tanaman':20}{'Volume Penyiraman':20}{'Status Tanaman'}")
    print("-" * 75)

    for tanaman in daftar_tanaman:
        print(
            f"{tanaman.nama_tanaman:25}"
            f"{tanaman.jenis_tanaman:20}"
            f"{tanaman.volume_penyiraman:20}"
            f"{tanaman.status}"
        )

    print("-" * 75)
    print(f"Total Tanaman: {len(daftar_tanaman)}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Tanaman")
        print("2. Refresh Data")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_tanaman()

        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_tanaman()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()







