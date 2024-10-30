import json
import pwinput
import os
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
            return
        elif pilihan_akun == '2':
            belum_ada_akun()
            return
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
        regis_username = input('Masukkan Username Anda: ')
        password = pwinput.pwinput('Masukkan Password Anda: ')
        email = input('Masukkan Email Anda: ')

        if username_terpakai(data, regis_username):
            print('Username telah terpakai. Silahkan masukkan username lain.')
        else:
            break

    akun_baru = {
        "username": regis_username,
        "password": password,
        "email": email,
        "role": "user"
    }
    data.append(akun_baru)
    with open(namafileakun, "w") as file:
        json.dump(data, file, indent=4)
    print("Berhasil Membuat Akun")
    ada_akun()

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
   
    with open(namafilegame, "r") as file_game:
        content = file_game.read().strip()
        data_games = json.load(file_game) if file_game.read() else []

    while True:
       
        nama = input('Masukkan Nama Game: ')
        rilis = input('Masukkan Tanggal Rilis Game: ')
        pengembang = input('Masukkan Nama Pengembang Game: ')
        genre = input('Masukkan Genre Game: ')
        deskripsi = input('Masukkan Deskripsi Game: ')
        harga = input('Masukkan Harga Game: ')

        game_baru = {
            "nama": nama,
            "rilis": rilis,
            "pengembang": pengembang,
            "genre": genre,
            "deskripsi": deskripsi,
            "harga": harga
        }
        data_games.append(game_baru)

        print(f'Game dengan Nama {nama} Berhasil Ditambahkan')
        
        pilihan = input('Apakah Ingin Menambah Game Lagi (YA/TIDAK): ')
        if pilihan.upper() == 'TIDAK':
            break

    with open(namafilegame, "w") as file_game:
        json.dump(data_games, file_game, indent=4)
    print("Semua data game berhasil disimpan.")

def lihat_game():
    table.clear_rows() 
    try:
        with open(namafilegame, "r") as file_game:
            data_games = json.load(file_game)
            for game in data_games:
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
        data_games = json.load(file_game)

    lihat_game() 
    print('\n========== Perbarui Game ==========')
    
    nomor = int(input('Masukkan Nomor Game Yang Ingin Diperbarui: ')) - 1  
    if 0 <= nomor < len(data_games):
        game = data_games[nomor]
        
        game["nama"] = input('Masukkan Nama Game (kosongkan jika tidak ada perubahan): ') or game["nama"]
        game["rilis"] = input('Masukkan Tanggal Rilis Game (kosongkan jika tidak ada perubahan): ') or game["rilis"]
        game["pengembang"] = input('Masukkan Nama Pengembang Game (kosongkan jika tidak ada perubahan): ') or game["pengembang"]
        game["genre"] = input('Masukkan Genre Game (kosongkan jika tidak ada perubahan): ') or game["genre"]
        game["deskripsi"] = input('Masukkan Deskripsi Game (kosongkan jika tidak ada perubahan): ') or game["deskripsi"]
        game["harga"] = input('Masukkan Harga Game (kosongkan jika tidak ada perubahan): ') or game["harga"]

        print(f'Game dengan nomor {nomor + 1} berhasil diperbarui.')

        with open(namafilegame, "w") as file_game:
            json.dump(data_games, file_game, indent=4)
    else:
        print(f'Game dengan nomor {nomor + 1} tidak ditemukan.')

def hapus_game():
    with open(namafilegame, "r") as file_game:
        data_games = json.load(file_game)
    lihat_game()
    print('\n========== Hapus Game ==========')
    
    nomor = int(input('Masukkan Nomor Game Yang Ingin Dihapus: ')) - 1 
    if 0 <= nomor < len(data_games):
        game_pilih = data_games[nomor]
        nama_game = game_pilih["nama"]
        konfirmasi = input(f'Apakah Anda yakin ingin menghapus game "{nama_game}"? (YA/TIDAK): ')
        
        if konfirmasi.upper() == 'YA':
            data_games.remove(game_pilih)
            print(f'Game "{nama_game}" berhasil dihapus.')

            with open(namafilegame, "w") as file_game:
                json.dump(data_games, file_game, indent=4)
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f'Game dengan nomor {nomor + 1} tidak ditemukan.')

def menu_pengguna():
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
            tambah_game()
        elif pilihan == '2':
            lihat_game()
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

def cek_saldo():
    while True:
            with open(namafileakun, "r") as file_akun:
                data_akuns = json.load(file_akun)
                for game in data_akuns:
                    game_list(
                        game.get("saldo")
                    )


def cek_akun():
    while True:
        print('\n========== AKUN ==========')        
        print('1. Lihat Akun ')
        print('2. Lihat game ')
        print('3. Hapus Akun ')
        try:
            pilihan = input("Silahkan Masukkan Pilihan Anda: ")
            if pilihan == "1":
                lihat_akun()
            elif pilihan == "2":
                game_dibeli()
            elif pilihan == "3":
                hapus_akun()
            else:
                print("Pilihan tidak tersedia")
        except ValueError:
            print("Pilihan tidak sesuai \nSilahkan Masukkan Pilihan Anda Kembali")

login()
