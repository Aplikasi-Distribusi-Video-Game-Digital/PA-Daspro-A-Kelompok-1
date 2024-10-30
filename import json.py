import json
import pwinput
from prettytable import PrettyTable

print('☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬')

namafileakun = 'data_user.json'
namafilegame = 'data_game.json'

def login():
    while True:
        print('\n========== LOGIN ==========')        
        print('1. Sign In')
        print('2. Sign Up')
        pilihan_akun = input('Silahkan Pilih Login: ')
        if pilihan_akun == "1":
            ada_akun()
            return
        elif pilihan_akun == '2':
            belum_ada_akun()
            return
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
    lihat_game()
    print('\n==========Perbarui Game==========')
    while True:
        nomor = int(input('Masukkan Nomor Game Yang Ingin Diperbarui: '))
        for row in table._rows:
            if row[0] == nomor:
                nama = input('Masukkan Nama Game (kosongkan jika tidak ada): ') or row[1]
                rilis = input('Masukkan Tanggal Rilis Game (kosongkan jika tidak ada): ') or row[2]
                pengembang = input('Masukkan Nama Pengembang Game (kosongkan jika tidak ada): ') or row[3]
                genre = input('Masukkan Genre Game (kosongkan jika tidak ada): ') or row[4]
                deskripsi = input('Masukkan Deskripsi Game (kosongkan jika tidak ada): ') or row[5]
                row[1], row[2], row[3], row[4], row[5] = nama, rilis, pengembang, genre, deskripsi
                print(f'Game dengan nomor {nomor} berhasil diperbarui')
                return
        else:
            print(f'Game dengan nomor {nomor} tidak ditemukan')
            print('-------------------------------------')

def hapus_game():
    lihat_game()
    print('\n==========Hapus Game==========')
    while True:
        nomor = int(input('Masukkan Nomor Game Yang Ingin Dihapus: '))
        for row in table._rows:
            if row[0] == nomor:
                table._rows.remove(row)
                print('=========================================')
                print(f'Game dengan nomor {nomor} berhasil dihapus')
                break
        else:
            print(f'Game dengan nomor {nomor} tidak ditemukan')
        print('----------------------------------------')
        pilihan = input('Apakah Anda Ingin Menghapus Lagi? (YA/TIDAK): ')
        if pilihan.upper() == 'TIDAK':
            break

login()
