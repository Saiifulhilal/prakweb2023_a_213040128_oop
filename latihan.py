class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_edge(self, kota_asal, kota_tujuan, jarak):
        if kota_asal not in self.graph:
            self.graph[kota_asal] = {}
        self.graph[kota_asal][kota_tujuan] = jarak

def cari_rute_terpendek(graph, kota_asal, kota_tujuan, rute=[]):
    rute = rute + [kota_asal]
    if kota_asal == kota_tujuan:
        return rute
    if kota_asal not in graph:
        return None
    rute_terpendek = None
    for kota in graph[kota_asal]:
        if kota not in rute:
            rute_baru = cari_rute_terpendek(graph, kota, kota_tujuan, rute)
            if rute_baru:
                if not rute_terpendek or len(rute_baru) < len(rute_terpendek):
                    rute_terpendek = rute_baru
    return rute_terpendek

def main():
    graph = Graph()
    graph.tambah_edge("Asrama A", "Kampus X", 5)
    graph.tambah_edge("Asrama B", "Kampus Y", 8)
    graph.tambah_edge("Asrama C", "Kampus X", 10)
    graph.tambah_edge("Asrama A", "Asrama B", 2)
    graph.tambah_edge("Kampus X", "Kampus Y", 3)

    kota_asal = "Asrama A"
    kota_tujuan = "Kampus Y"

    rute_terpendek = cari_rute_terpendek(graph.graph, kota_asal, kota_tujuan)
    
    if rute_terpendek:
        print(f"Rute terpendek dari {kota_asal} ke {kota_tujuan} adalah: {rute_terpendek}")
        
        # Tambahkan opsi pemilihan rute alternatif
        pilihan = input("Apakah Anda ingin melihat rute alternatif? (ya/tidak): ")
        if pilihan.lower() == "ya":
            rute_alternatif = cari_rute_terpendek(graph.graph, kota_asal, kota_tujuan)
            print("Rute alternatif:")
            for idx, rute in enumerate(rute_alternatif):
                print(f"Rute {idx + 1}: {rute}")
    else:
        print(f"Tidak ada rute yang tersedia dari {kota_asal} ke {kota_tujuan}.")

if __name__ == "__main__":
    main()
