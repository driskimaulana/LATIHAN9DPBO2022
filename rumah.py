from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik , lokasi ):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_tanah, kapasitas_listrik, lokasi)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
   