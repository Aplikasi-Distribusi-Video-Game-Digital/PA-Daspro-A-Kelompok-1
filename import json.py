import json
from prettytable import PrettyTable

print('☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬')

namafileakun = 'data_user.json'
namafikeakun = 'data_game.json'

def login():
    while True:
        print('\n========== LOGIN ==========')
        print('1. Login')
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
    password = input('Masukkan Password Anda: ')

    try:
        file_akun = open(namafileakun, "r")
        data = json.loads(file_akun.read())
        file_akun.close()
    except FileNotFoundError:
        print('Akun pengguna tidak ditemukan. Silahkan registrasi dahulu.')
        return

def username_terpakai(data, regis_username):
    for user in data:
        if user['regis_username'] == regis_username:
            return True
    return False

def belum_ada_akun():
    try:
        file_akun = open(namafileakun, "r")
        data = json.loads(file_akun.read())
        file_akun.close()
    except FileNotFoundError:
        data = []
    
    while True:
        regis_username = input('Masukkan Username Anda: ')
        password = input('Masukkan Password Anda: ')
        if username_terpakai(data, regis_username):
            print('Username telah terpakai. Silahkan masukkan username lain')
        else:
            break
    
    akun_baru = {
        "username": regis_username,
        "password": password
    }
    data.append(akun_baru)
    with open("namafileakun", "w") as file:
        json.dump(data, file, indent=4)
    print("Berhasil Membuat Akun")
    ada_akun()


table = PrettyTable()
table.field_names = ['Nama Game', 'Tanggal Rilis Game', 'Pengembang Game', 'Genre Game', 'Deskripsi Game'] #
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

login()
