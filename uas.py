def total_diskon(harga, jumlah):
    if jumlah < 5:
        diskon = 0.05
    elif jumlah < 15:
        diskon = 0.25
    elif jumlah < 20:
        diskon = 0.50
    else:
        diskon = 0.75
    total_harga = (1 - diskon) * harga
    return total_harga, diskon

def rincian():
    harga = int(input("Total harga beli: Rp."))
    jumlah = int(input("Jumlah barang: "))
    return harga, jumlah

def main():
    harga, jumlah = rincian()
    total_harga, diskon = total_diskon(harga, jumlah) 
    print("Total Diskon: ", diskon)
    print("Total Harga: ", total_harga)

if __name__ == "__main__":
    main()