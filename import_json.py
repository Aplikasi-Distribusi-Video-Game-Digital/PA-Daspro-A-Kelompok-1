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
    table = PrettyTable()
    table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Deskripsi', 'Harga']
    try:
        with open(namafilegame, "r") as file_game:
            data_game = json.load(file_game)
            no = 1
            for game in data_game:
                table.add_row([
                    no, game.get("nama"), game.get("rilis"), game.get("pengembang"), 
                    game.get("genre"), game.get("deskripsi"), game.get("harga")
                ])
                no += 1
        print(table)
    except FileNotFoundError:
        print("Data game tidak ditemukan.")

def menu_pengguna():
    while True:
        # os.system('cls')
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
            print("=== Debug: Pilihan searching dipilih ===")  
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
    keyword = input('Masukkan kata kunci pencarian: ').strip().lower()
    found_games = []
    try:
        with open(namafilegame, "r") as file_game:
            data_games = json.load(file_game)
            for game in data_games:
                if any(keyword in str(value).lower() for value in game.values()):
                    found_games.append(game)
    except FileNotFoundError:
        print("Data game tidak ditemukan.")
        return

    if found_games:
        table = PrettyTable()
        table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Deskripsi', 'Harga']
        no = 1
        for game in found_games:
            table.add_row([
                no, game['nama'], game['rilis'], game['pengembang'], game['genre'], 
                game['deskripsi'], game['harga']
            ])
            no += 1
        print("\nHasil Pencarian:")
        print(table)
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
    print("1. Game Terbaru")
    print("2. Harga Tertinggi")
    print("3. Harga Terendah")
    pilihan = input("Silahkan Pilih Opsi Sorting (1/2/3): ")

    if pilihan == '1':
        data_game.sort(key=lambda game: game.get("rilis", ""), reverse=True)
    elif pilihan == '2':
        data_game.sort(key=lambda game: int(game.get("harga", 0)), reverse=True)
    elif pilihan == '3':
        data_game.sort(key=lambda game: int(game.get("harga", 0)))
    else:
        print("Pilihan tidak valid.")
        return

    table = PrettyTable()
    table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Deskripsi', 'Harga']
    no = 1
    for game in data_game:
        table.add_row([
            no, game['nama'], game['rilis'], game['pengembang'], game['genre'], 
            game['deskripsi'], game['harga']
        ])
        no += 1
    print("\nHasil Sorting:")
    print(table)

login()
