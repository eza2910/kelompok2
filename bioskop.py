class Film:
    pass

class Tiket:
    pass

daftar_film = {
    "action": {
        "fastx": {"nama": "FastX", "waktu": "13:00 - 15:00 WIT", "harga": {"biasa": 40, "sabtu": 50, "minggu": 55}},
        "lift": {"nama": "Lift", "waktu": "15:00 - 17:00 WIT", "harga": {"biasa": 35, "sabtu": 45, "minggu": 50}},
        "pertaruhan": {"nama": "Pertaruhan", "waktu": "19:00 - 21:00 WIT", "harga": {"biasa": 45, "sabtu": 55, "minggu": 60}}
    },
    "horor": {
        "sijjin": {"nama": "Sijjin", "waktu": "14:00 - 16:00 WIT", "harga": {"biasa": 40, "sabtu": 50, "minggu": 55}},
        "the incantion": {"nama": "The Incantion", "waktu": "16:00 - 18:00 WIT", "harga": {"biasa": 35, "sabtu": 45, "minggu": 50}},
        "midsommar": {"nama": "Midsommar", "waktu": "20:00 - 22:00 WIT", "harga": {"biasa": 45, "sabtu": 55, "minggu": 60}}
    },
    "anime": {
        "naruto": {"nama": "Naruto", "waktu": "12:00 - 14:00 WIT", "harga": {"biasa": 30, "sabtu": 40, "minggu": 45}},
        "black clover": {"nama": "Black Clover", "waktu": "14:00 - 16:00 WIT", "harga": {"biasa": 35, "sabtu": 45, "minggu": 50}},
        "darlin in frank": {"nama": "Darlin in Frank", "waktu": "18:00 - 20:00 WIT", "harga": {"biasa": 40, "sabtu": 50, "minggu": 55}}
    }
}

print("Pilihan Genre Film:")
for genre in daftar_film.keys():
    print(genre.capitalize())

genre = input("Masukkan genre film yang Anda inginkan: ").lower()
if genre in daftar_film.keys():
    print(f"Daftar Film {genre.capitalize()}:")
    for film in daftar_film[genre].keys():
        print(film)
        
    film = input("Pilih film yang ingin Anda tonton: ").lower()
    if film in daftar_film[genre].keys():
        hari = input("Pilih hari (biasa/sabtu/minggu): ").lower()
        if hari in daftar_film[genre][film]["harga"].keys():
            usia = int(input("Masukkan usia Anda: "))
            if usia <= 17:
                print("Maaf, Anda tidak dapat membeli tiket karena usia Anda di bawah 17 tahun.")
            else:
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                if jumlah_tiket > 1:
                    nama_penyewa_list = []
                    for i in range(jumlah_tiket):
                        nama_penyewa = input(f"Masukkan nama pembeli untuk tiket ke-{i+1}: ")
                        nama_penyewa_list.append(nama_penyewa)
                    total_harga = daftar_film[genre][film]["harga"][hari] * jumlah_tiket
                    
                    print("Anda telah membeli tiket:")
                    print(f"Nama Film: {daftar_film[genre][film]['nama'].capitalize()}")
                    print(f"Waktu: {daftar_film[genre][film]['waktu']}")
                    print(f"Jumlah Tiket: {jumlah_tiket} orang")
                    print(f"Total Harga Tiket: {total_harga} rb")
                    print("Invoice:")
                    for i in range(jumlah_tiket):
                        print(f"{i+1}. Nama: {nama_penyewa_list[i]}")
                    print(f"{jumlah_tiket+1}. Usia: {usia} Tahun")
                    print(f"{jumlah_tiket+2}. Film: {daftar_film[genre][film]['nama'].capitalize()}")
                    print(f"{jumlah_tiket+3}. Waktu: {daftar_film[genre][film]['waktu']}")
                    print(f"{jumlah_tiket+4}. Hari: {hari.capitalize()}")
                    print(f"{jumlah_tiket+5}. Quantity: {jumlah_tiket} orang")
                    print(f"{jumlah_tiket+6}. Total Harga: {total_harga} rb")
                else:
                    nama_penyewa = input("Masukkan nama Anda: ")
                    total_harga = daftar_film[genre][film]["harga"][hari] * jumlah_tiket
                    
                    print("Anda telah membeli tiket:")
                    print(f"Nama Film: {daftar_film[genre][film]['nama'].capitalize()}")
                    print(f"Waktu: {daftar_film[genre][film]['waktu']}")
                    print(f"Jumlah Tiket: {jumlah_tiket} orang")
                    print(f"Total Harga Tiket: {total_harga} rb")
                    print("Invoice:")
                    print(f"1. Nama: {nama_penyewa}")
                    print(f"2. Usia: {usia} Tahun")
                    print(f"3. Film: {daftar_film[genre][film]['nama'].capitalize()}")
                    print(f"4. Waktu: {daftar_film[genre][film]['waktu']}")
                    print(f"5. Hari: {hari.capitalize()}")
                    print(f"6. Quantity: {jumlah_tiket} orang")
                    print(f"7. Total Harga: {total_harga} rb")
        else:
            print("Hari tidak valid!")
    else:
        print("Film tidak ditemukan!")
else:
    print("Genre film tidak ditemukan!")
