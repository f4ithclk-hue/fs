import csv
import os
from models import Tanaman

def simpan_tanaman():
    print("\n=== TAMBAH DATA TANAMAN ===")

    nama_tanaman = input("Nama Tanaman    : ").strip()
    jenis_tanaman = input("Jenis Tanaman    : ").strip()
    cara_penyiraman = input("volume Penyiraman : ").strip()

    if not nama_tanaman or not jenis_tanaman or not cara_penyiraman:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    tanaman = Tanaman(nama_tanaman, jenis_tanaman, cara_penyiraman)

    file_exists = os.path.exists("tanaman.csv")

    with open("tanaman.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Nama Tanaman", "Jenis Tanaman", "Volume Penyiraman", "Status Tanaman"])

        writer.writerow(tanaman.to_list())

    print("\n[BERHASIL] Data tanaman berhasil ditambahkan.\n")

def main():
    while True:
        print("=== MENU TAMBAH TANAMAN ===")
        print("1. Tambah Tanaman")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_tanaman()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()

