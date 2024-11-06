import json
import pwinput
import os
from datetime import datetime
from prettytable import PrettyTable

print('☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬')

namafileakun = 'data_user.json'
namafilegame = 'data_game.json'

def login():
    while True:
        print('\n========== LOGIN ==========')        
        print('1. Sign In')
        print('2. Sign Up')
        print('3. Keluar Program')
        pilihan_akun = input('Silahkan Pilih Login: ')
        if pilihan_akun == "1":
            ada_akun()
        elif pilihan_akun == '2':
            belum_ada_akun()
        elif pilihan_akun == '3':
            exit()
        else:
            print('Pilihan Tidak Valid.')

def ada_akun():
    username = input('Masukkan Username Anda: ')
    password = pwinput.pwinput('Masukkan Password Anda: ')

    try:
        with open(namafileakun, "r") as file_akun:
            data = json.load(file_akun)
    except FileNotFoundError:
        print('Akun pengguna tidak ditemukan. Silahkan registrasi dahulu.')
        return

    for user in data:
        if user['username'] == username and user['password'] == password:
            print("Login berhasil!")
            if user.get("role") == "admin":
                menu_admin()
            elif user.get("role") == "user":
                menu_pengguna()
            else:
                print(f"Selamat datang, {username}!")
            return
    print("Username atau password salah.")

def username_terpakai(data, regis_username):
    for user in data:
        if user['username'] == regis_username:
            return True
    return False

def belum_ada_akun():
    try:
        with open(namafileakun, "r") as file_akun:
            data = json.load(file_akun)
    except FileNotFoundError:
        data = []

    while True:
        regis_username = input('Masukkan Username Anda: ').strip()
        
        if " " in regis_username:
            print("Username tidak boleh mengandung spasi. Silakan masukkan username lain.")
            continue
        if username_terpakai(data, regis_username):
            print("Username telah terpakai. Silakan masukkan username lain.")
            continue

        password = pwinput.pwinput('Masukkan Password Anda: ')
        telepon = input('Masukkan Telepon Anda: ')

        akun_baru = {
            "username": regis_username,
            "password": password,
            "telepon": telepon,
            "role": "user"
        }
        data.append(akun_baru)
        
        with open(namafileakun, "w") as file:
            json.dump(data, file, indent=4)
        
        print("Berhasil Membuat Akun")
        ada_akun()
        break  
table = PrettyTable()
table.field_names = ['No', 'Nama Game', 'Tanggal Rilis Game', 'Pengembang Game', 'Genre Game', 'Deskripsi Game']

def game_list(nama, rilis, pengembang, genre, deskripsi):   
    nomor = len(table._rows) + 1
    table.add_row([nomor, nama, rilis, pengembang, genre, deskripsi])

def menu_admin():
    while True:
        print('\n========== MENU ADMIN ==========')        
        print('1. Tambah Aplikasi Video Game ')
        print('2. Lihat Aplikasi Video Game ')
        print('3. Perbarui Aplikasi Video Game ')
        print('4. Hapus Aplikasi Video Game ')
        print('5. Keluar')
        pilihan = input('Silahkan Masukkan Pilihan Anda: ')
        if pilihan == '1':
            tambah_game()
        elif pilihan == '2':
            lihat_game()
        elif pilihan == '3':
            perbarui_game()
        elif pilihan == '4':
            hapus_game()
        elif pilihan == '5':
            break
        else:
            print('Pilihan Tidak Tersedia')

def tambah_game():
    try:
        with open(namafilegame, "r") as file_game:
            baca = file_game.read().strip()
            data_game = json.loads(baca) if baca else []
    except FileNotFoundError:
        data_game = []

    while True:
        nama = input('Masukkan Nama Game: ').strip()
        rilis = input('Masukkan Tanggal Rilis Game: ').strip()
        pengembang = input('Masukkan Nama Pengembang Game: ').strip()
        genre = input('Masukkan Genre Game: ').strip()
        deskripsi = input('Masukkan Deskripsi Game: ').strip()
        harga = input('Masukkan Harga Game: ').strip()

        if not (nama and rilis and pengembang and genre and deskripsi and harga):
            print("Semua kolom harus diisi!")
            continue 

        game_baru = {
            "nama": nama,
            "rilis": rilis,
            "pengembang": pengembang,
            "genre": genre,
            "deskripsi": deskripsi,
            "harga": harga
        }
        data_game.append(game_baru)

        print(f'Game dengan Nama {nama} Berhasil Ditambahkan')
        
        pilihan = input('Apakah Ingin Menambah Game Lagi (YA/TIDAK): ')
        if pilihan.upper() == 'TIDAK':
            break

    with open(namafilegame, "w") as file_game:
        json.dump(data_game, file_game, indent=4)
    print("Semua data game berhasil disimpan.")

def lihat_game():
    table.clear_rows() 
    try:
        with open(namafilegame, "r") as file_game:
            data_game = json.load(file_game)
            for game in data_game:
                game_list(
                    game.get("nama"),
                    game.get("rilis"),
                    game.get("pengembang"),
                    game.get("genre"),
                    game.get("deskripsi")
                )
        print(table)
    except FileNotFoundError:
        print("Data game tidak ditemukan.")

def perbarui_game():
    with open(namafilegame, "r") as file_game:
        data_game = json.load(file_game)

    lihat_game() 
    print('\n========== Perbarui Game ==========')
    
    nomor = int(input('Masukkan Nomor Game Yang Ingin Diperbarui: ')) - 1  
    if 0 <= nomor < len(data_game):
        game = data_game[nomor]
        
        game["nama"] = input('Masukkan Nama Game (kosongkan jika tidak ada perubahan): ') or game["nama"]
        game["rilis"] = input('Masukkan Tanggal Rilis Game (kosongkan jika tidak ada perubahan): ') or game["rilis"]
        game["pengembang"] = input('Masukkan Nama Pengembang Game (kosongkan jika tidak ada perubahan): ') or game["pengembang"]
        game["genre"] = input('Masukkan Genre Game (kosongkan jika tidak ada perubahan): ') or game["genre"]
        game["deskripsi"] = input('Masukkan Deskripsi Game (kosongkan jika tidak ada perubahan): ') or game["deskripsi"]
        game["harga"] = input('Masukkan Harga Game (kosongkan jika tidak ada perubahan): ') or game["harga"]

        print(f'Game dengan nomor {nomor + 1} berhasil diperbarui.')

        with open(namafilegame, "w") as file_game:
            json.dump(data_game, file_game, indent=4)
    else:
        print(f'Game dengan nomor {nomor + 1} tidak ditemukan.')

def hapus_game():
    with open(namafilegame, "r") as file_game:
        data_game = json.load(file_game)
    lihat_game()
    print('\n========== Hapus Game ==========')
    
    nomor = int(input('Masukkan Nomor Game Yang Ingin Dihapus: ')) - 1 
    if 0 <= nomor < len(data_game):
        game_pilih = data_game[nomor]
        nama_game = game_pilih["nama"]
        konfirmasi = input(f'Apakah Anda yakin ingin menghapus game "{nama_game}"? (YA/TIDAK): ')
        
        if konfirmasi.upper() == 'YA':
            data_game.remove(game_pilih)
            print(f'Game "{nama_game}" berhasil dihapus.')

            with open(namafilegame, "w") as file_game:
                json.dump(data_game, file_game, indent=4)
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f'Game dengan nomor {nomor + 1} tidak ditemukan.')

def menu_pengguna():
    print("=== Debug: Masuk ke menu_pengguna ===")  # Debug: Menu pengguna

    while True:
        os.system('cls')
        print('=====================================')        
        print('|        🎀 MENU PENGGUNA 🎀        |')        
        print('=====================================')        
        print('|          1. Searching             |')
        print('|          2. Sorting               |')
        print('|          3. Cek Akun              |')
        print('|          4. Cek Saldo             |')
        print('|          5. Keluar Akun           |')
        print('=====================================')        
        pilihan = input('Silahkan Masukkan Pilihan Anda: ')
        if pilihan == '1':
            print("=== Debug: Pilihan searching dipilih ===")  # Debug: Pilihan 1
            search_game()
        elif pilihan == '2':
            sorting()
        elif pilihan == '3':
            cek_akun()
        elif pilihan == '4':
            cek_saldo()
        elif pilihan == '5':
            konfirmasi = input('Apakah ingin keluar akun (YA/TIDAK): ')
            if konfirmasi.upper() == 'YA':
                login()
            else:
                menu_pengguna()
        else:
            print('Pilihan Tidak Tersedia')

def search_game():
    print("=== Debug: Fungsi search_game dipanggil ===")  # Debug awal fungsi

    keyword = input('Masukkan kata kunci pencarian: ').strip().lower()  # Hilangkan spasi dan ubah ke huruf kecil
    print(f"=== Debug: Kata kunci pencarian: {keyword} ===")  # Debug untuk kata kunci

    # Cek jika file bisa dibuka dan dibaca
    try:
        with open(namafilegame, "r") as file_game:
            data_games = json.load(file_game)
            print("\n=== Debug: Data game berhasil dimuat dari file ===")  # Debug saat data berhasil dimuat
            print("Jumlah game dalam data:", len(data_games))  # Debug: Jumlah game
            if not data_games:
                print("Data game kosong atau tidak ditemukan.")
                return
    except FileNotFoundError:
        print("Data game tidak ditemukan.")  # File tidak ditemukan
        return
    except json.JSONDecodeError as e:
        print(f"Error saat membaca file JSON: {e}")  # Error format JSON
        return

    # Proses pencarian
    found_games = []
    for game in data_games:
        nama = str(game.get("nama", "")).lower()
        rilis = str(game.get("rilis", "")).lower()
        pengembang = str(game.get("pengembang", "")).lower()
        genre = str(game.get("genre", "")).lower()
        deskripsi = str(game.get("deskripsi", "")).lower()
        harga = str(game.get("harga", "")).lower()

        print(f"\n=== Debug: Game yang sedang diproses ===")
        print(f"Nama: {nama}, Rilis: {rilis}, Pengembang: {pengembang}, Genre: {genre}, Deskripsi: {deskripsi}, Harga: {harga}")  # Debug setiap game

        # Kondisi pencocokan kata kunci
        if (keyword in nama or keyword in rilis or keyword in pengembang or 
            keyword in genre or keyword in deskripsi or keyword in harga):
            print("=== Debug: Game cocok ditemukan ===")  # Debug jika game cocok
            found_games.append(game)
        else:
            print("=== Debug: Game tidak cocok ===")  # Debug jika game tidak cocok

    # Tampilkan hasil pencarian
    if found_games:
        print("\nGame yang cocok:")
        for game in found_games:
            print(f"Nama: {game['nama']}, Rilis: {game['rilis']}, Pengembang: {game['pengembang']}, Genre: {game['genre']}, Deskripsi: {game['deskripsi']}, Harga: {game['harga']}")
    else:
        print("Tidak ada game yang cocok.")

def sorting():
    try:
        with open(namafilegame, "r") as file_game:
            data_game = json.load(file_game)
    except FileNotFoundError:
        print("Data game tidak ditemukan.")
        return

    print("\n========== Sorting Game ==========")
    print("1. Sortir Berdasarkan Game Terbaru")
    print("2. Sortir Berdasarkan Harga Tertinggi")
    print("3. Sortir Berdasarkan Harga Terendah")
    pilihan = input("Silahkan Pilih Opsi Sorting (1/2/3): ")

    if pilihan == '1':
        data_game.sort(key=lambda game: game.get("rilis", ""), reverse=True)
        print("\nDaftar Game Berdasarkan Tanggal Rilis (Terbaru ke Terlama):")
    elif pilihan == '2':
        data_game.sort(key=lambda game: int(game.get("harga", 0)), reverse=True)
        print("\nDaftar Game Berdasarkan Harga (Tertinggi ke Terendah):")
    elif pilihan == '3':
        data_game.sort(key=lambda game: int(game.get("harga", 0)))
        print("\nDaftar Game Berdasarkan Harga (Terendah ke Tertinggi):")
    else:
        print("Pilihan tidak valid.")
        return

    # Tampilkan hasil sorting
    for game in data_game:
        print(f"Nama: {game['nama']}, Rilis: {game['rilis']}, Pengembang: {game['pengembang']}, Genre: {game['genre']}, Deskripsi: {game['deskripsi']}, Harga: {game['harga']}")


def cek_saldo():
    while True:
        with open(namafileakun, "r") as file_akun:
            data_akuns = json.load(file_akun)
        for akun in data_akuns:
                akun(
                    akun.get("saldo")                    
                    )
        print('========== TOP UP Saldo ==========')
        topup = int(input('Masukkan nominal top up e-Money: '))
        proses = namafileakun['e-money'] + topup
        namafileakun['e-money'] = proses
        print('Top Up Berhasil')
        pilihan = input('Apakah ingin top up lagi? (YA/TIDAK): ')
        if pilihan == 'TIDAK':
            menu_pengguna()
            break



def cek_akun():
    while True:
        print('\n========== AKUN ==========')        
        print('1. Lihat Akun ')
        print('2. Lihat game ')
        print('3. Hapus Akun ')
        pilihan_akun = input('Silahkan Pilih Login: ')
        if pilihan_akun == "1":
            akun_user()
        elif pilihan_akun == '2':
            game_user()
        elif pilihan_akun == '3':
            exit()
        else:
            print('Pilihan Tidak Valid.')
    
login()