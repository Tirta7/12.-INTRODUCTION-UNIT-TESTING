class PengklasifikasiSegitiga:
    def __init__(self):
        self.TOLERANSI = 0.02  # Toleransi untuk perbandingan angka desimal

    def hampir_sama(self, a, b):
        return abs(a - b) <= self.TOLERANSI

    def klasifikasi_segitiga(self, a, b, c):
        # Langkah 1: Periksa nilai negatif atau nol
        if a <= 0 or b <= 0 or c <= 0:
            return "BUKAN SEGITIGA"
        
        # Urutkan sisi-sisi untuk memudahkan perbandingan
        sisi = sorted([a, b, c])
        terkecil, tengah, terbesar = sisi
        
        # Langkah 2: Periksa ketidaksamaan segitiga
        if terbesar >= terkecil + tengah:
            return "BUKAN SEGITIGA"
            
        # Langkah 3: Periksa segitiga sama sisi
        if self.hampir_sama(a, b) and self.hampir_sama(b, c):
            return "SEGITIGA SAMA SISI"
            
        # Langkah 4: Periksa segitiga siku-siku
        # Menggunakan teorema Pythagoras dengan toleransi
        if self.hampir_sama(terbesar * terbesar, 
                          terkecil * terkecil + tengah * tengah):
            return "SEGITIGA SIKU-SIKU"
            
        # Langkah 5: Periksa segitiga sama kaki
        if (self.hampir_sama(a, b) or 
            self.hampir_sama(b, c) or 
            self.hampir_sama(a, c)):
            return "SEGITIGA SAMA KAKI"
            
        # Langkah 6: Jika bukan semua di atas, maka segitiga bebas
        return "SEGITIGA BEBAS"

import unittest

class TestPengklasifikasiSegitiga(unittest.TestCase):
    def setUp(self):
        self.klasifikasi = PengklasifikasiSegitiga()

    def test_nilai_negatif(self):
        """Uji Jalur 1: Nilai negatif harus mengembalikan BUKAN SEGITIGA"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(-1, 2, 3), "BUKAN SEGITIGA")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(1, -2, 3), "BUKAN SEGITIGA")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(1, 2, -3), "BUKAN SEGITIGA")

    def test_nilai_nol(self):
        """Uji Jalur 2: Nilai nol harus mengembalikan BUKAN SEGITIGA"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(0, 2, 3), "BUKAN SEGITIGA")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(1, 0, 3), "BUKAN SEGITIGA")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(1, 2, 0), "BUKAN SEGITIGA")

    def test_ketidaksamaan_segitiga(self):
        """Uji Jalur 3: Melanggar ketidaksamaan segitiga harus mengembalikan BUKAN SEGITIGA"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(1, 2, 4), "BUKAN SEGITIGA")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(7, 2, 3), "BUKAN SEGITIGA")

    def test_segitiga_sama_sisi(self):
        """Uji Jalur 4: Sisi sama harus mengembalikan SEGITIGA SAMA SISI"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(3, 3, 3), "SEGITIGA SAMA SISI")
        # Uji dengan nilai desimal
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(2.99, 3.01, 3.00), "SEGITIGA SAMA SISI")

    def test_segitiga_siku_siku(self):
        """Uji Jalur 5: Segitiga siku-siku harus mengembalikan SEGITIGA SIKU-SIKU"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(3, 4, 5), "SEGITIGA SIKU-SIKU")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(5, 12, 13), "SEGITIGA SIKU-SIKU")

    def test_segitiga_sama_kaki(self):
        """Uji Jalur 6: Dua sisi sama harus mengembalikan SEGITIGA SAMA KAKI"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(2, 2, 3), "SEGITIGA SAMA KAKI")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(4, 3, 4), "SEGITIGA SAMA KAKI")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(5, 6, 5), "SEGITIGA SAMA KAKI")

    def test_segitiga_bebas(self):
        """Uji Jalur 7: Sisi berbeda harus mengembalikan SEGITIGA BEBAS"""
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(3, 4, 6), "SEGITIGA BEBAS")
        self.assertEqual(self.klasifikasi.klasifikasi_segitiga(7, 8, 9), "SEGITIGA BEBAS")

if __name__ == '__main__':
    unittest.main()
