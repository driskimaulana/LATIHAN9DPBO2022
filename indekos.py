from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, fasilitas, luas_tanah = 0, kapasitas_listrik = 0, lokasi = ""):
        super().__init__("Indekos", 0, 0, luas_tanah, kapasitas_listrik, lokasi)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.fasilitas = fasilitas

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."

    def get_fasilitas(self):
        return self.fasilitas