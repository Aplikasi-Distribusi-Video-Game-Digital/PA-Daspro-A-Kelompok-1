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
                menu_pengguna(user)
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
            "role": "user",
            "saldo": 0  
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
        print('1. Tambah Video Game ')
        print('2. Lihat Video Game ')
        print('3. Perbarui Video Game ')
        print('4. Hapus Video Game ')
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
        
        while True:
            try:
                harga = int(input('Masukkan Harga Game: '))
                break  
            except ValueError:
                print("Harga harus angka.")

        if not (nama and rilis and pengembang and genre and deskripsi):
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
            print("Batal Hapus")
    else:
        print(f'Game dengan nomor {nomor + 1} tidak ditemukan.')

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

def menu_pengguna(user):
    while True:
        print('=====================================')        
        print('|        🎀 MENU PENGGUNA 🎀        |')        
        print('=====================================')        
        print('|          1. Searching             |')
        print('|          2. Sorting               |')
        print('|          3. Cek Akun              |')
        print('|          4. Cek Saldo             |')
        print('|          5. Top Up Saldo          |')
        print('|          6. Keluar Akun           |')
        print('=====================================')        
        pilihan = input('Silahkan Masukkan Pilihan Anda: ')
        if pilihan == '1':
            search_game()
        elif pilihan == '2':
            sorting(user)
        elif pilihan == '3':
            cek_akun(user)
        elif pilihan == '4':
            cek_saldo(user)
        elif pilihan == '5':
            top_up_saldo(user)
        elif pilihan == '6':
            konfirmasi = input('Apakah ingin keluar akun (YA/TIDAK): ')
            if konfirmasi.upper() == 'YA':
                login()
            else:
                menu_pengguna(user)
        else:
            print('Pilihan Tidak Tersedia')

def beli_game(user, game):
    #saldo tidak cukup
    if user['saldo'] < game['harga']:
        print(f"Saldo anda tidak cukup. Harga: Rp. {game['harga']}")
        return
    
    #sudah punya game
    for game_dibeli in user.get("pembelian", []):
        if game_dibeli['nama'] == game['nama']:
            print(f"Anda sudah memiliki game {game['nama']} ")
            return
    
    #pembelian
    user['saldo'] -= game['harga']
    user.setdefault("pembelian", []).append(game)
    update_user_data(user)
    print(f"Game \"{game['nama']}\" berhasil dibeli! Saldo sekarang: Rp {user['saldo']}")

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

def sorting(user):
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

    #pilih game untuk dibeli
    try:
        pilihan_game = int(input("Masukkan nomor game yang ingin dibeli, 0 untuk batal: ")) - 1
        if pilihan_game == -1:
            print("Batal membeli game.")
            return
        if 0 <= pilihan_game < len(data_game):
            game_terpilih = data_game[pilihan_game]
            beli_game(user, game_terpilih)
        else:
            print("Nomor game tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def cek_akun(user):
    print("\n===== Informasi Akun =====")
    print(f"Username: {user['username']}")
    print(f"Telepon: {user['telepon']}")
    print(f"Saldo: Rp {user['saldo']}")
    
    pembelian = user.get("pembelian", [])
    if pembelian:
        print("\nGame dimiliki: ")
        for game in pembelian:
            print(f"- {game['nama']}")
    else:
        print("\nBelum punya game.")

def cek_saldo(user):
    print(f"\nSaldo Anda: Rp {user['saldo']}")

def top_up_saldo(user):
    try:
        jumlah_topup = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        if jumlah_topup > 0:
            user['saldo'] += jumlah_topup
            update_user_data(user)
            print(f"Saldo berhasil ditambahkan. Saldo Anda sekarang: Rp {user['saldo']}")
        else:
            print("Jumlah saldo harus positif.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def update_user_data(user):
    try:
        with open(namafileakun, "r") as file:
            data = json.load(file)
        
        for data_user in data:
            if data_user['username'] == user['username']:
                data_user.update(user)  
                break

        with open(namafileakun, "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("Data akun tidak ditemukan.")

login()
