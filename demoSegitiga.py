from pengklasifikasiSegitiga import PengklasifikasiSegitiga

def demo_klasifikasi():
    klasifikasi = PengklasifikasiSegitiga()
    
    print("=== DEMO PENGKLASIFIKASI SEGITIGA ===")
    print("\n1. Contoh Input Bilangan Bulat:")
    print("--------------------------------")
    
    test_cases = [
        (3, 3, 3),        # Sama sisi
        (3, 4, 5),        # Siku-siku
        (2, 2, 3),        # Sama kaki
        (3, 4, 6),        # Bebas
        (1, 2, 4),        # Bukan segitiga
        (-1, 2, 3),       # Nilai negatif
        (0, 2, 3),        # Nilai nol
    ]
    
    for a, b, c in test_cases:
        hasil = klasifikasi.klasifikasi_segitiga(a, b, c)
        print(f"Sisi-sisi: {a}, {b}, {c} => {hasil}")
    
    print("\n2. Contoh Input Bilangan Desimal:")
    print("--------------------------------")
    decimal_cases = [
        (2.99, 3.01, 3.00),  # Sama sisi (dengan toleransi)
        (3.0, 4.0, 5.0),     # Siku-siku
        (2.5, 2.5, 3.0),     # Sama kaki
        (3.1, 4.2, 6.3),     # Bebas
    ]
    
    for a, b, c in decimal_cases:
        hasil = klasifikasi.klasifikasi_segitiga(a, b, c)
        print(f"Sisi-sisi: {a}, {b}, {c} => {hasil}")

if __name__ == "__main__":
    demo_klasifikasi()
