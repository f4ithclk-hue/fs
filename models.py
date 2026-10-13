class Tanaman:

    def __init__(self, nama_tanaman, jenis_tanaman, volume_penyiraman, status="Sehat"):
        self.nama_tanaman = nama_tanaman
        self.jenis_tanaman = jenis_tanaman
        self.volume_penyiraman = volume_penyiraman
        self.status = status

    def to_list(self):
        return [self.nama_tanaman, self.jenis_tanaman, self.volume_penyiraman, self.status]

    def __str__(self):
        return f"{self.nama_tanaman} ({self.jenis_tanaman}) - Penyiraman: {self.volume_penyiraman} - {self.status}"

class Perawatan:

    def __init__(self, id_perawatan, nama_tanaman, volume_penyiraman, jadwal_penyiraman):
        self.id = id_perawatan
        self.nama_tanaman = nama_tanaman
        self.volume_penyiraman = volume_penyiraman
        self.jadwal_penyiraman = jadwal_penyiraman

    def to_list(self):
        return [self.id, self.nama_tanaman, self.volume_penyiraman, self.jadwal_penyiraman]

    def __str__(self):
        return f"{self.nama_tanaman} ({self.id}) - Penyiraman: {self.volume_penyiraman}, Jadwal: {self.jadwal_penyiraman}"

