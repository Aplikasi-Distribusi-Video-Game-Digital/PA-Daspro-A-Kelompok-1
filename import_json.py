import json
import pwinput
from datetime import datetime
import time
from prettytable import PrettyTable

namafileakun = 'data_user.json'
namafilegame = 'data_game.json'

def countdown(waktu):
    while waktu >= 0:
        print(f'Silahkan coba lagi dalam waktu {waktu} detik', end='\r')
        time.sleep(1)
        waktu -= 1

def login():
    while True:
        print('\n=====================================')
        print('|             Noir Space            |')
        print('=====================================')
        print('|          1. Sign In               |')
        print('|          2. Sign Up               |')
        print('|          3. Keluar Program        |')
        print('=====================================')   
        try:
            pilihan_akun = int(input('Silahkan Pilih Login: '))
            if pilihan_akun == 1:
                ada_akun()
            elif pilihan_akun == 2:
                belum_ada_akun()
            elif pilihan_akun == 3:
                print("Terimakasih!")
                exit()
            else:
                print('Pilihan tidak valid dan gunakan dengan angka ')
        except ValueError:
            print("Input tidak valid")

def ada_akun():
    for l in range(3):
        username = input('Masukkan username anda: ')
        password = pwinput.pwinput('Masukkan password anda: ')
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
        input("Enter untuk lanjut")
    else:
        print("Anda melewati maksimal percobaan")
        countdown(20)

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
        akun_baru = {
            "username": regis_username,
            "password": password,
            "role": "user",
            "saldo": 0  
        }
        data.append(akun_baru)        

        with open(namafileakun, "w") as file:
            json.dump(data, file, indent=4)    

        print("Berhasil Membuat Akun")
        return

def menu_admin():
    while True:
        print('=====================================')        
        print('|            MENU ADMIN             |')        
        print('=====================================')        
        print('|          1. Tambah Game           |')
        print('|          2. Lihat Game            |')
        print('|          3. Perbarui Game         |')
        print('|          4. Hapus Game            |')
        print('|          5. Keluar                |')
        print('=====================================') 
        try:
            pilihan = int(input('Silahkan Masukkan Pilihan Anda: '))
            if pilihan == 1:
                tambah_game()
            elif pilihan == 2:
                lihat_game()
            elif pilihan == 3:
                perbarui_game()
            elif pilihan == 4:
                hapus_game()
            elif pilihan == 5:
                konfirmasi = input('Apakah ingin keluar akun (YA/TIDAK): ')
                if konfirmasi.upper() == 'YA':
                    login()
                elif konfirmasi.upper() == 'TIDAK':
                    menu_admin()
                else:
                    print("SIlahkan ketik (YA/TIDAK)")
            else:
                print('Pilihan Tidak Tersedia')
        except ValueError:
            print("Input tidak valid")

def tambah_game():
    try:
        with open(namafilegame, "r") as file_game:
            baca = file_game.read().strip()
            data_game = json.loads(baca) if baca else []
    except FileNotFoundError:
        data_game = []
    while True:
        print('\n========== Tambah Game ==========')
        nama = input('Masukkan Nama Game: ').strip()
        rilis = input('Masukkan Tanggal Rilis Game: ').strip()
        pengembang = input('Masukkan Nama Pengembang Game: ').strip()
        genre = input('Masukkan Genre Game: ').strip()

        while True:
            try:
                harga = int(input('Masukkan Harga Game: Rp. '))
                break
            except ValueError:
                print("Harga harus berupa angka")

        if not (nama and rilis and pengembang and genre and harga):
            print("Semua kolom harus diisi!")
            continue 

        game_baru = {
            "nama": nama,
            "rilis": rilis,
            "pengembang": pengembang,
            "genre": genre,
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
        while True:
            try:
                game["harga"] = input('Masukkan Harga Game (kosongkan jika tidak ada perubahan): ') or game["harga"]
                break
            except ValueError:
                print("Harga harus berupa angka")
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
    table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Harga (Rp)']
    try:
        with open(namafilegame, "r") as file_game:
            data_game = json.load(file_game)
            no = 1
            for game in data_game:
                table.add_row([
                    no, game.get("nama"), game.get("rilis"), game.get("pengembang"), 
                    game.get("genre"), game.get("harga")
                ])
                no += 1
        print('\n========== Lihat Game ==========')
        print(table)
    except FileNotFoundError:
        print("Data game tidak ditemukan.")

def menu_pengguna(user):
    rekomendasi(user)
    while True:
        print('\n=====================================')        
        print('|        🎮 MENU PENGGUNA 🎮        |')        
        print('=====================================')        
        print('|          1. Searching             |')
        print('|          2. Sorting               |')
        print('|          3. Cek Akun              |')
        print('|          4. Top Up Saldo          |')
        print('|          5. Keluar Akun           |')
        print('=====================================')
        try:    
            pilihan = int(input('Silahkan Masukkan Pilihan Anda: '))
            if pilihan == 1:
                search_game(user)
            elif pilihan == 2:
                sorting(user)
            elif pilihan == 3:
                cek_akun(user)
            elif pilihan == 4:
                top_up_saldo(user)
            elif pilihan == 5:
                konfirmasi = input('Apakah ingin keluar akun (YA/TIDAK): ')
                if konfirmasi.upper() == 'YA':
                    login()
                elif konfirmasi.upper() == 'TIDAK':
                    menu_pengguna(user)
                else:
                    print("SIlahkan ketik (YA/TIDAK)")
            else:
                print('Pilihan Tidak Tersedia')
        except ValueError:
            print("Input tidak sesuai")

def rekomendasi(user):
    while True:
        table = PrettyTable()
        table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Harga (Rp)']
        jumlah_game = 5
        try:
            with open(namafilegame, "r") as file_game:
                data_game = json.load(file_game)
                no = 1
                for game in data_game[:jumlah_game]:
                    table.add_row([
                        no, game.get("nama"), game.get("rilis"), game.get("pengembang"), 
                        game.get("genre"), game.get("harga")
                    ])
                    no += 1
            print("\n======================== Rekomendasi Game ============================")
            print(table)
            print('\n=====================================')
            print('|            REKOMENDASI            |')
            print('=====================================')
            print('|         1. Pilih game             |')
            print('|         2. Ke menu                |')
            print('=====================================')
            try:
                pilihan = int(input("Silahkan masukkan pilihan anda: "))
                if pilihan == 1:
                    print(table)
                    pilih_game = int(input('Masukkan game yang ingin dipilih: '))
                    if 0 <= pilih_game < len(data_game):
                        game_terpilih = data_game[pilih_game]
                        beli_game(user, game_terpilih)
                    print(f"Anda memilih gam: {game['nama']} dengan harga: Rp. {game['harga']}")
                elif pilihan == 2:
                    return
                else:
                    print("Pilihan tidak tersedia")
            except ValueError:
                print("Input tidak sesuai")
        except FileNotFoundError:
            print("Data game tidak ditemukan.")

def buat_invoice(user, game):
    print("\n===== INVOICE/NOTA PEMBELIAN =====")
    print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Nama Pembeli: {user['username']}")
    print("\nDetail Pembelian:")
    print(f"Nama Game: {game['nama']}")
    print(f"Harga: Rp {game['harga']}")
    print(f"Sisa Saldo: Rp {user['saldo']}")
    print("=====================================")
    print("Terima Kasih!\n")

def beli_game(user, game):
    #saldo tidak cukup
    if user['saldo'] < game['harga']:
        print(f"Saldo anda tidak cukup. Harga: Rp. {game['harga']}, Silahkan top up terlebih dahulu")
        input("Tekan Enter untuk lanjut.... ")
        menu_pengguna(user)
    
    #sudah punya game
    for game_dibeli in user.get("pembelian", []):
        if game_dibeli['nama'] == game['nama']:
            print(f"Anda sudah memiliki game {game['nama']} ")
            return
    
    #pembelian
    konfirmasi = input("Ingin melanjutkan pembelian (YA/TIDAK) ")
    if konfirmasi.upper() == 'YA':
        user['saldo'] -= game['harga']
        user.setdefault("pembelian", []).append(game)
        update_user_data(user)
        print(f"Game \"{game['nama']}\" berhasil dibeli! Saldo sekarang: Rp {user['saldo']}")
        buat_invoice(user, game)
    elif konfirmasi.upper() == 'TIDAK':
        print("Transaksi dibatalkan")
        return
    else:
        print("Input tidak sesuai")

def search_game(user):
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
        table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Harga (Rp)']
        no = 1
        for game in found_games:
            table.add_row([
                no, game['nama'], game['rilis'], game['pengembang'], game['genre'], 
                game['harga']
            ])
            no += 1
        print("\nHasil Pencarian:")
        print(table)

        print('\n=====================================')
        print('|            Searching              |')
        print('=====================================')
        print('|         1. Pilih game             |')
        print('|         2. Searching lagi         |')
        print('|         3. Ke menu                |')
        print('=====================================')
        try:
            pilihan = int(input("Silahkan masukkan pilihan anda: "))
            if pilihan == 1:
                try:
                    pilihan_game = int(input("Masukkan nomor game yang ingin dibeli, 0 untuk batal: ")) - 1
                    if pilihan_game == -1:
                        print("Batal membeli game.")
                        return
                    if 0 <= pilihan_game < len(found_games):
                        game_terpilih = found_games[pilihan_game]
                        beli_game(user, game_terpilih)
                    else:
                        print("Nomor game tidak valid.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")
            elif pilihan == 2:
                search_game(user)
            elif pilihan == 3: 
                return
            else:
                print("Pilihan tidak tersedia")
        except ValueError:
            print("Input tidak sesuai")
    else:
        print("Tidak ada game yang cocok.")
        pilih = input("Apakah ingin searching lagi (YA/TIDAK)? ")
        if pilih == 'YA':
            search_game()
        else:
            print("Pencarian selesai")

def sorting(user):
    while True:
        try:
            with open(namafilegame, "r") as file_game:
                data_game = json.load(file_game)
        except FileNotFoundError:
            print("Data game tidak ditemukan.")
            return

        print('\n=====================================')
        print('|              Sorting              |')
        print('=====================================')
        print('|         1. Game Terbaru           |')
        print('|         2. Harga Tertinggi        |')
        print('|         3. Harga Terendah         |')
        print('=====================================')
        pilihan = int(input("Silahkan masukkan pilihan anda: "))
        try:
            if pilihan == 1:
                data_game.sort(key=lambda game: game.get("rilis", ""), reverse=True)
            elif pilihan == 2:
                data_game.sort(key=lambda game: int(game.get("harga", 0)), reverse=True)
            elif pilihan == 3:
                data_game.sort(key=lambda game: int(game.get("harga", 0)))
            else:
                print("Pilihan tidak valid.")
                return
        except ValueError:
            print("Input tidak sesuai")

        table = PrettyTable()
        table.field_names = ['No', 'Nama Game', 'Tanggal Rilis', 'Pengembang', 'Genre', 'Harga (Rp)']
        no = 1
        for game in data_game:
            table.add_row([
                no, game['nama'], game['rilis'], game['pengembang'], game['genre'], 
                game['harga']
            ])
            no += 1
        print("\nHasil Sorting:")
        print(table)

        # PERBAIKIN KETERANGANNYA MENUNYA INDAH
        print('\n=====================================')
        print('|              Sorting              |')
        print('=====================================')
        print('|         1. Pilih game             |')
        print('|         2. Sorting lagi           |')
        print('|         3. Ke menu                |')
        print('=====================================')
        try:
            pilih = int(input("Masukkan pilihan anda: "))
            if pilih == 1:
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
            elif pilih == 2:
                sorting(user)
            elif pilih == 3:
                return
            else:
                print("Pilihan tidak tersedia")
        except ValueError:
            print("Input tidak sesuai")

def cek_akun(user):
    print("\n===== Informasi Akun =====")
    print(f"Username: {user['username']}")
    print(f"Saldo: Rp {user['saldo']}")
    
    pembelian = user.get("pembelian", [])
    if pembelian:
        print("\nGame dimiliki: ")
        for game in pembelian:
            print(f"- {game['nama']}")
    else:
        print("\nBelum punya game.")

def top_up_saldo(user):
    while True:
        try:
            print(f"Anda memiliki saldo sebesar {user['saldo']}")
            pilih = input("Apakah anda ingin menambah saldo (YA/TIDAK)? ")
            if pilih.upper() == 'YA':
                try:
                    jumlah_topup = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
                    if jumlah_topup > 0:
                        user['saldo'] += jumlah_topup
                        update_user_data(user)
                        print(f"Saldo berhasil ditambahkan. Saldo Anda sekarang: Rp {user['saldo']}")
                    else:
                        print("Jumlah saldo harus positif.")
                except ValueError:
                    print("Input tidak valid")
            elif pilih.upper() == 'TIDAK':
                return
            else:
                print("Input tidak sesuai")
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

if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\nPorgram dihentikan oleh pengguna.")