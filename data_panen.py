data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Menampilkan seluruh data dictionary
print("Data Panen")
for key, value in data_panen.items():
    print(key, value)

# 2. Menampilkan jumlah hasil panen jagung dari lokasi2
print(f"\nHasil Panen Jagung dari lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

# 3. Menampilkan nama lokasi dari lokasi3
print(f"\nNama Lokasi dari lokasi3: {data_panen['lokasi3']['nama_lokasi']}")

# 4. Masukkan jumlah hasil panen padi dan kedelai ke dalam variabel yang berbeda
# 5. buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
jumlah_padi = {key: value['hasil_panen']['padi'] for key, value in data_panen.items()}
jumlah_kedelai = {key: value['hasil_panen']['kedelai'] for key, value in data_panen.items()}

print("\njumlah Padi : ")
for key, value in jumlah_padi.items():
    print(key, value)

print("\njumlah Kedelai : ")
for key, value in jumlah_kedelai.items():
    print(key, value)