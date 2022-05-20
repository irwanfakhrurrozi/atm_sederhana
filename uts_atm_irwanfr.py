#UTS_PRAKTIK_DASAR_PEMROGRAMAN
import os

nama_bank = "Fakhrurrozi"
nim = 210601032
saldo = 600000

#tampilan awal ketika program dijalankan
print("Selamat Datang di ATM Bank ",nama_bank)
print("Kode: ",nim)

#user memasukan kode pin
pin_user = input("Masukkan PIN anda: ")

if pin_user == "090522":
    print("")
    print("Saldo anda saat ini sebesar ",saldo)
    print("Silahkan pilih transaksi yang anda inginkan:")
    print("(1) Tarik Tunai (2) Transfer (3) Bayar Tagihan (4) Batal")
    
    pilih=input("silahkan pilih (1-4) > ")
   
   #logika tarik tunai
    if pilih == "1":
        print()
        print("Pilih nominal yang ingin anda tarik:")
        print("(1) 100.000 (2) 500.000 (3) 1.000.000 (4) Batal")
        transaksi=input("silahkan pilih (1-4) > ")
        
        
        if transaksi == "1":
            if saldo >= 100000:
                sisa_saldo = saldo - 100000
                print("Silahkan ambil uang dan kartu anda, Saldo anda tersisa ", sisa_saldo)
                 
            else:
                print("Saldo anda tidak cukup, silahkan ambil kartu anda")
                os.system("exit")

        elif transaksi == "2":
            if saldo >= 500000:
                sisa_saldo = saldo - 500000
                print("Silahkan ambil uang dan kartu anda, Saldo anda tersisa ", sisa_saldo)
                
            else:
                print("Saldo anda tidak cukup, silahkan ambil kartu anda")
                os.system("exit")
                
        elif transaksi == "3":
            if saldo >= 1000000:
                sisa_saldo = saldo - 1000000
                print("Silahkan ambil uang dan kartu anda, Saldo anda tersisa ", sisa_saldo)
                
            else:
                print("Saldo anda tidak cukup, silahkan ambil kartu anda")
                os.system("exit")
                
                
    #logika transfer
    elif pilih == "2":
        no_rek_tujuan = input("Masukkan nomor rekening tujuan: ")
        nom_transfer = int(input("Nominal yang ingin anda transfer: "))
        pesan_transfer = input("Pesan transfer: ")
        
        if saldo >= nom_transfer:
            print("Anda akan mentransfer dana sejumlah {} ke nomor rekening {} dengan pesan {} ".format(nom_transfer, no_rek_tujuan, pesan_transfer))
            konfir = input("Lanjut (1.OK, 2. Batal): ")
            if konfir == "1":
                sisa_saldo = saldo - nom_transfer
                print("Transfer berhasil, saldo anda tersisa ",sisa_saldo)
            elif konfir == "2":
                print("Transfer dibatalkan")
            else:
                os.system("exit")
                
        elif saldo < nom_transfer:
            print("Anda akan mentransfer dana sejumlah {} ke nomor rekening {} dengan pesan {} ".format(nom_transfer, no_rek_tujuan, pesan_transfer))
            print("Saldo anda tidak cukup, silahkan ambil kartu anda")         
       
        else:
            print("Anda membatalkan transaksi, silahkan ambil kartu anda")
        
    
    #logika tagihan pembayaran
    elif pilih == "3":
        print("Pilih tagihan (1) Kartu Kredit, (2) Telepon ")
        opsi_tagihan = input("silahkan pilih (1-2) > ")
        if opsi_tagihan == "1":
            print("Terjadi kesalahan, fitur tidak dapat digunakan")
            os.system("exit")
        elif opsi_tagihan == "2":
            tagihan = 250000
            no_telp = input("Masukkan nomor telepon anda: ")
            print("Anda akan membayar tagihan telepon untuk nomor telepon {} sejumlah {}".format(no_telp, tagihan))
            konfir = input("Lanjut (1.OK, 2. Batal): ")
            if konfir == "1":
                sisa_saldo = saldo - tagihan
                print("Pembayaran berhasil, saldo anda tersisa ",sisa_saldo)
                os.system("exit")
            elif konfir == "2":
                print("Pembayaran dibatalkan")
            else:
                os.system("exit")

        else:
            os.system("exit")
    
    else :
        print("Anda membatalkan transaksi, silahkan ambil kartu anda")
        os.system("exit")
    
else:
    print("Maaf, PIN anda salah, kartu anda disita untuk keamanan")
    