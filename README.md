# PA-Daspro-A-Kelompok-1

## FLowchart

![PA DASPRO drawio (1)](https://github.com/user-attachments/assets/970f111a-e264-4ab9-8a18-5f83c7ef486f)

## Penjelasan Output

1. Login pengguna
   
Pada tampilan awal, pengguna akan diberi 3 pilihan (sign in, sign up, dan keluar)

- Jika pengguna memilih 1 (Sign In)
    
maka pengguna akan diarahkan untuk menginput username dan password, jika username dan password benar, maka login berhasil.

![image](https://github.com/user-attachments/assets/46577760-a1cf-40a3-a2cb-9e53d9f621c7)

  Jika username atau password salah, maka pengguna akan diminta login kembali dengan maksimal percobaan sebanyak 3 kali. namun jika pengguna salah menginputkan username atau password lebih dari 3 kali, maka pengguna akan mendapatkan pinalti (jeda waktu selama 5 detik).

![image](https://github.com/user-attachments/assets/efea2d45-9676-4826-b0ec-f3a5510c68fe)

  Setelah pinalti berakhir, pengguna akan diarahkan kembali ke menu login untuk memilih 3 pilihan kembali

![image](https://github.com/user-attachments/assets/d2aa5b1a-3b6f-4a4a-a902-22584df6d97f)

- Jika pengguna memilih 2 (Sign Up)

   Jika pengguna memilih 2. Sign Up, akan diarahkan untuk memasukkan username dan password, dan jika username telah digunakan oleh user lain, maka akan memasukkan username ulang.

   ![image](https://github.com/user-attachments/assets/262e09ce-979f-467c-8862-0a386d18c18d)

   Jika pengguna memilih 3. Keluar Program, program selesai.
  
   ![image](https://github.com/user-attachments/assets/acb45173-8fb5-4f1e-b2e1-29a4d1aebbec)

2. Menu Admin

   Setelah login admin berhasil, akan diarahkan ke halaman menu admin yang terdapat 5 pilihan yaitu “Tambah Game”, “Lihat Game”, “Perbarui Game”, “Hapus Game”.

   ![image](https://github.com/user-attachments/assets/cca2f39c-7423-4775-ae20-0b4634280686)

   a. Admin memilih “Tambah Game”, akan diarahkan untuk memasukkan nama game, tanggal rilis game, pengembang game, genre game, dan harga game. Setelah semua kolom diisi, data berhasil ditambahkan ke dalam database. Jika semua kolom ada yang tidak diisi, maka admin akan mengulang untuk memasukkan tambah game lagi. Terdapat pilihan ingin menambah lagi, jika admin memilih “YA”, maka akan diarahkan kembali untuk memasukkan data tambah game. Jika “TIDAK”, maka akan diarahkan ke halaman menu admin.

   ![image](https://github.com/user-attachments/assets/afed40c9-9ba8-4e30-8b7a-a8b5700feb7b)

   b. Admin memilih “Lihat Game”, akan menampilkan list game yang tersedia dalam database.

   ![image](https://github.com/user-attachments/assets/ea2a234e-198c-4869-9ee2-28629ea69e75)

   c. Admin memilih “Perbarui Game”, akan diarahkan untuk memasukkan nomor game yang ingin diperbarui, jika nomor game tersebut ada di dalam list game, maka akan diarahkan ke masukkan perbarui data, dapat dikosongkan bila tidak semua yang ingin diperbarui. Setelah kolom diisi, data game akan diperbarui sesuai dengan isian admin sebelumnya.

   ![image](https://github.com/user-attachments/assets/d42e3901-55e3-4d4a-aa28-f990fdd998e8)

   Jika nomor game tersebut tidak ada dalam list game, maka admin memasukkan nomor game lagi yang tersedia di dalam list game.

   ![image](https://github.com/user-attachments/assets/e899a129-a2c6-4cda-8df6-9cfd698a4124)

   d. Admin memilih “Hapus Game”, akan diarahkan untuk memasukkan nomor game yang ingin dihapus. Jika nomor game ada di dalam list game, maka admin konfirmasi penghapusan game dan memilih YA atau TIDAK. Jika memilih YA , data nomor game berhasil dihapus.

   ![image](https://github.com/user-attachments/assets/59defc54-68c9-499f-808b-169ce7d3103c)

   Jika masukkan nomor game tidak tersedia dalam list game, maka akan memasukkan ulang sesuai list game yang tersedia. dan jika konfirmasi penghapusan memilih TIDAK, gagal pengapusan data nomor game.

   ![image](https://github.com/user-attachments/assets/25acebbb-b8b5-437d-b392-296fc0a11f7d)

   e. Admin memilih “Keluar”, akan diarahkan ke halaman menu login.

   ![image](https://github.com/user-attachments/assets/7f41efd4-fac8-436f-befb-1a4588e6de96)

2. Menu Pengguna
   
   Setelah user berhasil login, akan diarahkan ke halaman rekomendasi game, dan pilihan untuk memilih game yang ada di rekomendasi atau memilih ke menu.

   ![image](https://github.com/user-attachments/assets/b37174ff-4089-4176-9326-9dafd549f0a0)

   Jika user memilih pilih game, akan diarahkan untuk memasukkan nomor game yang tertera di list rekomendasi game. Setelah memilih game yang ada dalam list rekomendasi game, menampilkan game dan terdapat pilihan untuk membeli game. Jika user memilih membeli game, akan diarahkan ke pembayaran. Jika saldo mencukupi, user melakukan konfirmasi pembayaran. Jika user memilih YA konfirmasi pembayaran, maka pembelian game berhasil dan game yang dipilih akan ditambahkan ke akun user.

   ![image](https://github.com/user-attachments/assets/9905a1f1-c397-484b-806d-2d128c96a6f3)

   Jika saldo tidak mencukupi, user akan diarahkan  ke halaman menu, untuk melakukan top up saldo terlebih dahulu.

   ![image](https://github.com/user-attachments/assets/6d76d421-dfa5-4fed-8949-ac3a06e2e1ca)

   Jika user memilih ke menu, akan diarahkan ke halaman menu pengguna yang terdapat 5 pilihan yaitu “Searching”, “Sorting”, “Cek Akun”, “Top Up Saldo”, “Keluar Akun”.

   ![image](https://github.com/user-attachments/assets/93127373-0274-4c36-8df0-de1000494c50)

   a. Jika user memilih “Searching”, akan diarahkan untuk memasukkan kata kunci game yang ingin dicari, setelah game muncul sesuai yang diinginkan, terdapat pilihan untuk memilih “Pilih Game”, “Searching lagi”, “Ke menu”. 

   ![image](https://github.com/user-attachments/assets/e374bcc6-debb-4070-abe6-2e7e698d592b)

   Jika user memilih “Pilih Game yang di Beli”, user akan diarahkan untuk memasukkan pilihan game yang terdapat dalam list game yang telah dicari, jika saldo mencukupi untuk pembelian, maka akan diarahkan ke proses pembayaran, kemudian terdapat pilihan konfirmasi, memilih YA untuk konfirmasi pembayaran, maka pembelian berhasil dan game akan ditambahkan ke list game akun user.

   ![image](https://github.com/user-attachments/assets/be43bd84-536b-45a6-a87e-7f01dd23d0e5)

   Jika saldo tidak mencukupi, user akan diarahkan  ke halaman menu, untuk melakukan top up saldo terlebih dahulu.
   
   ![image](https://github.com/user-attachments/assets/9f9302b0-2767-4e6c-aa82-279d7952b837)

   User memilih “Searching lagi”, akan diarahkan kembali untuk melakukan searching dengan mencari kata kunci game.

   ![image](https://github.com/user-attachments/assets/0d5b0098-c4dc-4c3a-9a77-00604a861c47)

   User memilih “Ke menu”, akan diarahkan ke halaman menu pengguna.

   ![image](https://github.com/user-attachments/assets/84442500-05ec-4098-bb5a-7e3b3ef3f492)

   Jika user melakukan searching dan list game tidak muncul, user akan memilih ingin searching lagi atau tidak. Jika memilih TIDAK akan diarahkan ke menu pengguna, jika YA akan diarahkan ke searching lagi.

   ![image](https://github.com/user-attachments/assets/a8eb14d2-6483-4535-8056-c65750788cd3)

   b. User memilih “sorting”, terdapat pilihan “Game Terbaru”, “Harga Terendah”, “Harga Tertinggi”.

   ![image](https://github.com/user-attachments/assets/89efa022-4a38-4b2a-aeae-5978dc503777)

   Jika memilih “Game Terbaru”, akan menampilkan list game terbaru

   ![image](https://github.com/user-attachments/assets/4f82e601-5580-4929-ab6f-0b8abe8f4a77)

   Jika memilih “Harga Tertinggi”, akan menampilkan list game dari harga tertinggi

   ![image](https://github.com/user-attachments/assets/9b2a6aac-0026-479e-b5f3-21b3ff06ba5d)

   Jika memilih “Harga Terendah”, akan menampilkan list game dari harga terendah

   ![image](https://github.com/user-attachments/assets/fdb1614e-874a-4722-b1ab-6aa5f16b15b0)

   Setelah game muncul sesuai dengan urutan yang dipilih, terdapat pilihan untuk memilih “Pilih Game untuk Dibeli”, “Sorting lagi”, “Ke menu”.

   ![image](https://github.com/user-attachments/assets/37d320fb-7f16-46d0-a00b-9671c5b79496)

   Jika user memilih “Pilih Game untuk Dibeli”, user akan diarahkan untuk memilih game yang terdapat dalam list game yang telah dicari, dan akan menampilkan game yang dipilih dan jika saldo mencukupi untuk pembelian, maka akan diarahkan ke proses pembayaran, kemudian terdapat pilihan konfirmasi, memilih YA untuk konfirmasi pembayaran, maka pembelian berhasil dan game akan ditambahkan ke list game akun user. Jika saldo tidak mencukupi, user akan diarahkan  ke halaman menu, untuk melakukan top up saldo terlebih dahulu.
   
   ![image](https://github.com/user-attachments/assets/324777ca-1942-4099-9f9f-14a902d1bd24)

   User memilih “Sorting lagi”, akan diarahkan kembali untuk melakukan sorting dan memilih sorting berdasarkan urutan yang diinginkan.

   ![image](https://github.com/user-attachments/assets/b3c80593-77bc-4348-846f-0fcee608a8d6)

   User memilih “Ke menu”, akan diarahkan ke halaman menu pengguna.

   ![image](https://github.com/user-attachments/assets/11b7934b-c11f-44e8-9e29-3cf2d94da6ff)

   c. User memilih "Cek Akun", akan menampilkan username, saldo, dan list game yang dimiliki.

   ![image](https://github.com/user-attachments/assets/b77d51a7-5b0b-4cbd-9c8a-a3ae4d26b5ab)

   d. User memilih "Top Up Saldo", akan menampilkan saldo yang dimiliki, kemudian konfirmasi pilihan ingin top up. Jika YA, maka masukkan nominal saldo yang ingin ditambahkan, setelah itu top up berhasil dan saldo akan ditambahkan ke data akun user.

   ![image](https://github.com/user-attachments/assets/d2b37492-4c84-4fc9-b7af-6e9abdaa33f8)

   e. User memilih "Keluar Akun", menampilkan pilihan konfirmasi keluar. Jika YA, maka akan keluar dari akun dan kembali ke menu login.

   ![image](https://github.com/user-attachments/assets/7fffc149-f630-44ac-9767-3995d0554fbc)

   Jika TIDAK, maka akan kembali ke halaman rekomendasi.

   ![image](https://github.com/user-attachments/assets/48ea393a-3794-47af-9c57-4f990c8e9986)


















  
