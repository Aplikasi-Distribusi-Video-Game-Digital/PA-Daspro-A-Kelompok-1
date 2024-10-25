import json
from prettytable import PrettyTable
print('☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬ ☬')
user = {
    'admin': {'password': 'group1best', 'role': 'admin'}
}
def login():
    while True:
        username = input('Masukkan Username Anda: ')
        if username == user:
            menu_admin()

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

table = PrettyTable()
#Baris ini menentukan nama-nama kolom untuk tabel (field names)
table.field_names = ['Nama Game', 'Tanggal Rilis Game', 'Pengembang Game', 'Genre Game', 'Deskripsi Game'] #
def game(nama, rilis, pengembang, genre, deskripsi): #Mendefinisikan fungsi bernama paket
    table.add_row([nama, rilis, pengembang, genre, deskripsi]) #Didalam fungsi paket, baris ini menambahkan sebuah baris baru ke dalam tabel

def tambah_game():
    while True:
        nama = input('Masukkan Nama Game: ')
        rilis = input('Masukkan Tanggal Rilis Game: ')
        pengembang = input('Masukkan Pengembang Game: ')
        genre = input('Masukkan Genre Game: ')
        deskripsi = input('Masukkan Deskripsi Game: ')
        game(nama, rilis, pengembang, genre, deskripsi)
        print('==============================================')
        print(f'Game dengan Nama {nama} Berhasil Ditambahkan')
        print('----------------------------------------------')
        pilihan = input('Apakah Ingin Menambah Paket Lagi (YA/TIDAK): ') #Perulangan pilihan
        if pilihan == 'TIDAK':
            break

def lihat_game():
    
