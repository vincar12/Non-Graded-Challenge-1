'''
=================================================
Graded Challenge 1

Nama  : Muhammad Vincar Rafi Theoseta
Batch : HCK-018

Program ini bertujuan untuk menyimpan dan menampilkan barang belanjaan.
Program ini dapat menerima 5 input dari pengguna:
Input 1 menambah barang dengan memasukkan nama dan harga;
Input 2 menghapus barang dengan memasukkan no.index barang tersebut;
Input 3 menampilkan daftar barang dalam keranjang;
Input 4 menjumlahkan harga tiap barang dalam keranjang;
Input 5 mematikan aplikasi
=================================================
'''

"""
Membuat class CartItem untuk menciptakan representasi barang 
    belanjaan yang memiliki atribut berupa nama dan harga
"""
class CartItem:
    """
    Menginisiasi class CartItem
    """
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

"""
Membuat class ShoppingCart untuk representasi keranjang belanjaan yang memiliki beberapa metode fungsi di dalamnya
"""    
class ShoppingCart:

    """
    Membuat keranjang kosong untuk diisi
    """
    def __init__(self):
        self.shopcart = []

    """
    Fungsi untuk menambahkan barang ke dalam keranjang; menunjukkan kalimat 'item berhasil ditambahkan' saat proses berhasil
    """
    def addcart(self, item):
        self.shopcart.append(item)
        print("item berhasil ditambahkan\n")
    
    """
    Fungsi untuk menghapus barang di dalam keranjang; menunjukkan kalimat 'item berhasil dihapus' saat proses berhasil
    """
    def removecart(self, item):
        self.shopcart.pop(item)
        print("item berhasil dihapus\n")
    
    """
    Fungsi untuk menunjukkan barang di dalam keranjang; Jika keranjang masih kosong, akan menunjukkan kalimat 'keranjang kosong'.
    Jika sudah berisi, akan mencetak header 'no|nama|harga', lalu menjabarkan barang dalam keranjang dengan fitur loop berupa nomor|nama barang|harga barang
    Variable nomor berguna untuk menunjukkan barang yang sudah ada dalam keranjang, perlu didefinisikan nomor=1 agar memulai penghitungan dari angka 1 dan setiap loop akan ditambah 1
    """
    def showcart(self):
        if self.shopcart == []:
            print("keranjang kosong\n")

        else:
            print("no|nama|harga")
            nomor = 1
            for item in self.shopcart:
                print(nomor, item.nama, item.harga, sep="|")
                nomor += 1

    """
    Fungsi untuk menunjukkan total harga barang di dalam keranjang. Jika keranjang masih kosong, akan menunjukkan kalimat  'keranjang kosong'.
    Jika sudah berisi, akan membuat variabel harg yang bernilai 0 untuk representasi titik awal harga dari keranjang yang belum ditambahkan dengan harga barang. 
    Lalu fungsi loop digunakan untuk menjabarkan barang yang ada dalam keranjang. Setelah itu variabel intharg akan mengkonversi harga setiap barang dari String menjadi Integer.
    Setelah itu setiap harga barang yang sudah berupa angka akan dijumlahkan ke variabel harg yang awalnya bernilai 0
    Terakhir, memasukkan variable harg ke dalam string kalimat 'total harga belanja Rp.{harg}' dan mencetaknya
    """
    def totalcart(self):
        if self.shopcart == []:
            print("keranjang kosong\n")

        else:
            harg = 0
            for item in self.shopcart:
                intharg = int(item.harga)
                harg += intharg
            return harg
            #print(f"total harga belanja Rp.{harg}")


"""
Main app
Variabel shop untuk memanggil class ShoppingCart agar metode fungsi untuk memanipulasi keranjang dapat digunakan
"""
if __name__ == "__main__":
    shop = ShoppingCart()

    """
    While loop untuk menjalankan aplikasi agar jalan terus menerus sebelum dimatikan
    """
    while True:

        """
        Mencetak tampilan aplikasi berisi menu yang dapat dipilih; variabel user_input berfungsi menginput pilihan menu dari pengguna
        """
        print("Selamat Datang di Keranjang Belanja")
        print("\n Menu:")
        print("1. Menambah Barang")
        print("2. Menghapus Barang")
        print("3. Tampilkan Keranjang")
        print("4. Total Belanja")
        print("5. Exit")
        user_input = input("ketik menu untuk diakses:(1-5)")
        print("\n Pilih menu:", user_input)


        """
        Jika user input menu 1, akan diarahkan untuk menginput nama dan harga dari barang yang ingin dimasukkan ke dalam keranjang.
        Variabel nama dan harga bertugas mengambil input dari user.
        Variable barang berfungsi untuk memanggil class CartItem untuk membuat sebuah barang dengan atribut nama dan harga
        Lalu menggunakan fungsi addcart() dari class ShoppingCart untuk menambahkan barang yang sudah dibuat
        """
        if user_input == "1":
            nama = input("Masukkan nama:")
            harga = input("Masukkan harga:")
            barang = CartItem(nama, harga)
            shop.addcart(barang)
            
            """
            Jika user input menu 2, akan ditunjukkan list barang yang sudah masuk menggunakan fungsi showcart()
            Lalu user diarahkan untuk menginput nomor barang yang ingin dihapus
            Setelah mendapat input, variable nomer_hapus akan mengubah input user dari string menjadi integer lalu dikurangi 1. 
            Ini dilakukan karena list dalam python bermulai dengan index 0, maka jika mengetik no.1 akan menghapus barang dengan index 0 dari list
            Fungsi try dipakai agar aplikasi tidak error jika user menginput nomor yang tidak ada dalam index list.
            Jika tidak ada maka akan mencetak pesan 'opsi tidak tersedia, mohon ketik angka lain'
            """
        elif user_input == "2":
            shop.showcart()
            input_hapus = input("masukkan no. dihapus: ")
            nomer_hapus = int(input_hapus) - 1
            try:
                shop.removecart(nomer_hapus)
            except:
                print("opsi tidak tersedia, mohon ketik angka lain")

            """
            Jika user input menu 3, akan ditunjukkan list barang yang sudah masuk menggunakan fungsi showcart()
            """
        elif user_input == "3":
            shop.showcart()

            """
            Jika user input menu 4, akan mencetak "total harga belanja dalam keranjang: Rp.{tot}"
            Dimana variabel tot adalah representasi fungsi totalcart() untuk menunjukkan jumlah harga total dari barang dalam keranjang
            """
        elif user_input == "4":
            tot = shop.totalcart()
            print(f"total harga belanja dalam keranjang: Rp.{tot}")
            
            """
            Jika user input menu 5, akan mencetak 'sampai jumpa' lalu program berhenti
            """
        elif user_input == "5":
            print("\nsampai jumpa")
            break
            
        else:
            print("\ninput tidak dikenal mohon coba angka lain")
            """
            Jika user input menu selain angka 1-5 akan mencetak 'input tidak dikenal mohon coba angka lain'
            """
