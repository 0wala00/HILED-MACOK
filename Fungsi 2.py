def cek_masuk():
    umur = int(input("Berapa umurmu? "))
    kartu = input("Apakah kamu punya kartu? (ya/tidak): ").lower()

    if umur >= 18:
        if kartu == "ya":
            pin = input("Masukkan PIN kartu: ")
            if pin == "1234":
                print("Akses diterima. Selamat datang!")
            else:
                print("PIN salah. Akses ditolak.")
        else:
            print("Kamu harus punya kartu untuk masuk.")
    else:
        print("Maaf, umur kamu belum cukup.")


cek_masuk()
