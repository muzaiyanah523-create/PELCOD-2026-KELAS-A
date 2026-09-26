# TOTAL BELANJA

# INPUT:
# BUKU ; PULPEN ; BELANJA ; HARGA ; DISKON 

# PROSES;
# Menghitung humlah buku, 
# jumlah pulpen, dan 
# jumlah total belanja, 
# total belanja setelah diskon 

#CARANYA 
# - Menghitung jumlah pulpen dan buku 
# - Menghitung harga pulpen dan buku 
# - menghitung total belanja belanja setelah diskon 

# OUTPUT 
# - Hitung total harga buku 
# - Hitung total harga pulpen 
# - Total diskon 
# - Total bayar 


# ===============================================================
# ===============================================================


jumlahBuku = 3
hargaBuku = 15000
jumlahPulpen = 2
hargaPulpen = 5000

totalHargaBuku = jumlahBuku * hargaBuku
totalHargaPulpen = jumlahPulpen * hargaPulpen
totalBelanja = totalHargaBuku + totalHargaPulpen

if  totalBelanja >= 5000:
    diskon = totalBelanja * 10 / 100
else:
    diskon = 0

totalBayar = totalBelanja - diskon

print("Total harga buku      : Rp", totalHargaBuku)
print("Total harga Pulpen    : Rp", totalHargaPulpen)
print("Harga sebelum diskon  : Rp", totalBelanja)
print("Besar diskon          : Rp", diskon)
print("Total                 : Rp", totalBayar)