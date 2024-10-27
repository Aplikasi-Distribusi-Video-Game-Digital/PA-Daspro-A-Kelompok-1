import json
from prettytable import PrettyTable

print('☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬')

def load_data():
    with open("data_user.json", "r") as json_user:
        data_user = json.load(json_user)
    with open("data_game.json", "r") as json_game:
        data_game = json.load(json_game)
    return data_user, data_game

def simpan_data(data_user, data_game):
    with open("data_user.json", "w") as json_user:
        json.dump(data_user, json_user, indent=4)
    with open("data_game.json", "w") as json_game:
        json.dump(data_game, json_game, indent=4)

def login():
    users, games = load_data()
    username = input('Masukkan Username Anda: ')
    password = input('Masukkan Password Anda: ')

    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f'Login Berhasil! Selamat Datang {username}')
            return user['role']
        
    print("Username atau Password Anda Salah")
    return None

def regristasi_pengguna_baru(username, password):
    print('\n========== Regristasi Pengguna Baru ==========')
    users = load_data("data_user.json")
    for user in users:
        if user['username'] == username:
            print('Username Sudah Digunakan!')
            return
    users.append({'username': username, 'password': password})
    simpan_data('data_user.json', users)
    print(f'Regristasi Berhasil! Selamat Datang, {users}')


table = PrettyTable()
table.field_names = ['Nomor', 'Nama Game', 'Tanggal Rilis Game', 'Pengembang Game', 'Genre Game', 'Deskripsi Game', 'Harga']

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
        print('5. Keluar ')
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

def menu_user():
    while True:
        print('\n========== MENU USER ==========') 
        print('1. Lihat Daftar Game')
        print('2. Beli Game')
        print('3. Keluar')
        pilihan = input('Silahkan Masukkan Pilihan Anda: ')
        if pilihan == '1':
            lihat_game()
        elif pilihan == '2':
            beli_game()
        elif pilihan == '3':
            break
        else:
            print('Pilihan Tidak Tersedia')

def tambah_game():
    while True:
        nama = input('Masukkan Nama Game: ')
        rilis = input('Masukkan Tanggal Rilis Game: ')
        pengembang = input('Masukkan Nama Pengembang Game: ')
        genre = input('Masukkan Genre Game: ')
        deskripsi = input('Masukkan Deskripsi Game: ')
        game_list(nama, rilis, pengembang, genre, deskripsi)
        print('==============================================')
        print(f'Game dengan Nama {nama} Berhasil Ditambahkan')
        print('----------------------------------------------')
        pilihan = input('Apakah Ingin Menambah Paket Lagi (YA/TIDAK): ') #Perulangan pilihan
        if pilihan == 'TIDAK':
            break

def lihat_game():
    print(table)

def perbarui_game():
    lihat_game()
    print('\n==========Perbarui Paket==========')
    while True:
        nomor = int(input('Masukkan Nomor Game Yang Ingin Diperbarui: '))
        for row in table._rows:
            if row[0] == nomor:
                nama = input('Masukkan Nama Game (kosongkan jika tidak ada): ')
                rilis = input('Masukkan Tanggal Rilis Game (kosongkan jika tidak ada): ')
                pengembang = input('Masukkan Nama Pengembang Game (kosongkan jika tidak ada): ')
                genre = input('Masukkan Genre Game (kosongkan jika tidak ada): ')
                deskripsi = input('Masukkan Deskripsi Game (kosongkan jika tidak ada): ')
                row[1] = nama
                row[2] = rilis
                row[3] = pengembang
                row[4] = genre
                row[5] = deskripsi
                print(f'Game Dengan {nomor} Berhasil Diperbarui')
                return
        else:
            print(f'Game Dengan Nomor {nomor} Tidak Ditemukan')
            print('-------------------------------------')

def hapus_game():
    lihat_game()
    print('\n==========Hapus Paket==========')
    while True:
        nomor = int(input('Masukkan Nomor Game Yang Ingin Diperbarui: '))
        for row in table._rows:
            if row[0] == nomor:
                table._rows.remove(row)
                print('=========================================')
                print(f'Game Dengan {nomor} Berhasil Dihapus')
                break
        else:
            print(f'Game Dengan Nomor {nomor} Tidak Ditemukan ')
        print('----------------------------------------')
        pilihan = input('Apakah Anda Ingin Menghapus Lagi? (YA/TIDAK): ')
        if pilihan == 'TIDAK':
            break

def beli_game():
    None #Jangan diapa apain dulu ya manis

# Main Program
role = login()
if role == 'admin':
    menu_admin()
elif role == 'user':
    menu_user()
else:
    print("Akses Ditolak.")