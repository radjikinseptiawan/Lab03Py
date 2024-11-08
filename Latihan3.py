saldo = 1000000
print(f'Saldo Saat ini : {saldo} \n')
print('''
1. Tarik uang
2. Keluar
''')

pilih = int(input("Pilih menu (1/2) : "))

if pilih == 1:
    nominalTarik = int(input("Masukkan Jumlah Penarikan : "))
    sisaSaldo = saldo - nominalTarik
    print('penarikan berhasil')
    print(f'Sisa Saldo anda {sisaSaldo}')
else:
    print("Terimakasih telah menggunakan ATM!")