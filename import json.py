import json
from prettytable import PrettyTable

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

def tambah_game():
    nama = input
    harga = 
    genre = 