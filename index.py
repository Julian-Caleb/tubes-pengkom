# PROGRAM SISTEM PENILAIAN MAHASISWA TPB STEI
# Program dibuat untuk menghitung nilai mahasiswa dalam 2 semester TPB

# KAMUS GLOBAL
# 

# FUNCTION AND PROCEDURES    
# Komputasi atau Rekayasa
def KomputasiRekayasa (nim) :
    if nim // 100000 == 196 :
        return "Komputasi"
    elif nim // 100000 == 165 :
        return "Rekayasa"
    else :
        return "Bukan NIM STEI"

# Menghitung nilai 1 semester
def SatuSemester (fakultas, semester) :
    semester += 1
    if fakultas == "Komputasi" :
        if semester == 1 :
            mataKuliahSemester = [["Matematika IA", "Fisika Dasar IA", "Olah Raga", "Pengenalan Komputasi", "Tata Tulis Karya Ilmiah", "Bahasa Inggris"],
                ["MA1101", "FI1101", "KU1001", "KU1102", "KU1011", "KU1024"],
                [4, 4, 2, 3, 2, 2]]
        else : # semester == 2
            mataKuliahSemester = [["Matematika IIA", "Fisika Dasar IIA", "Kimia Dasar B", "Pengantar Rekayasa dan Desain", "Komputasi dan Masyarakat", "Dasar Pemrograman"],
                ["MA1201", "FI1201", "KI1002", "KU1202", "II1101", "IF1210"],
                [4, 4, 4, 3, 2, 2]]
    else : # fakultas == "Rekayasa"
        if semester == 1 :
            mataKuliahSemester = [["Matematika IA", "Fisika Dasar IA", "Olah Raga", "Pengenalan Komputasi", "Tata Tulis Karya Ilmiah", "Bahasa Inggris"],
                ["MA1101", "FI1101", "KU1001", "KU1102", "KU1011", "KU1024"],
                [4, 4, 2, 3, 2, 2]]
        else : # semester == 2
            mataKuliahSemester = [["Matematika IIA", "Fisika Dasar IIA", "Kimia Dasar B", "Pengantar Rekayasa dan Desain", "Pengantar Analisis Rangkaian", "Dasar Pemrograman"],
                ["MA1201", "FI1201", "KI1002", "KU1202", "EL1200", "IF1210"],
                [4, 4, 4, 3, 2, 2]]
            
    print(f"----------\tPENILAIAN SEMESTER {semester}\t----------")  
    print("")  
    
    nilaiSatuSemester = [[0 for i in range (6)], ["T" for i in range (6)]]
    for i in range (6) :
        nilaiSatuSemester[0][i] = MataKuliah (mataKuliahSemester,i)
        nilaiSatuSemester[1][i] = MencariIndex (nilaiSatuSemester[0][i])
        print("")
        print(f"Nilai akhir {mataKuliahSemester[0][i]} pada semester {semester} adalah {nilaiSatuSemester[0][i]}.")
        print(f"Index akhir {mataKuliahSemester[0][i]} pada semester {semester} adalah {nilaiSatuSemester[1][i]}.")
        print("")
        print("--------------------------------------------------")
        print("")
    nilaiIP = MenghitungIP (mataKuliahSemester[0], mataKuliahSemester[2], nilaiSatuSemester[1])
    indexIP = MencariIndexIP (nilaiIP)
    return nilaiIP, indexIP
    
# Menghitung nilai tiap mata kuliah
def MataKuliah (mataKuliahSemester,i) :
    nilaiMataKuliah = 0
    print(f"{i+1}. Penilaian Mata Kuliah {mataKuliahSemester[0][i]} - {mataKuliahSemester[1][i]}")
    print("")
    nilaiMataKuliah = KomponenPenilaian()
    
    return nilaiMataKuliah         
    
# Menghitung nilai tiap komponen penilaian
def KomponenPenilaian () : 
    nilaiMataKuliah = 0 
    komponenPenilaian = [["UAS", "UTS", "Kuis / KBF", "PR, Tugas, dan lain-lain"], 
                         [37.5, 37.5, 15, 10]]
    for i in range(4) :
        print(f"- Penilaian {komponenPenilaian[0][i]} - ")
        nilaiSatuKomponen = 0
        apakahAda = int(input(f"Berapa banyak penilaian {komponenPenilaian[0][i]}: "))
        if apakahAda == 0 :
            print(f"Tidak ada penilaian {komponenPenilaian[0][i]}") # Kalau tidak ada, bagaimana persentasenya?
        else :
            for j in range (apakahAda) :
                nilaiSementara = float(input(f"Masukkan nilai ke-{j+1}: "))
                nilaiSatuKomponen += nilaiSementara
            nilaiSatuKomponen = nilaiSatuKomponen / apakahAda
            
        nilaiMataKuliah += (nilaiSatuKomponen * komponenPenilaian[1][i]) / 100
        print("")
    
    
    return nilaiMataKuliah
    
# Mencari index satu mata kuliah
def MencariIndex (nilaiSatuMataKuliah) :
    # inputIndex()
    hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
    angkaIndex = [75, 68, 60, 53, 45, 38, 0]
    bermasalah = input("Apakah bermasalah di mata kuliah ini? (Y/N): ")
    if bermasalah == "Y" :
        return "T"
    else :
        for i in range (7) :
            if nilaiSatuMataKuliah >= angkaIndex[i] :
                return hurufIndex[i]
    
# Menghitung IP
def MenghitungIP (mataKuliah, banyakSKS, nilaiIndex) :
    totalSKS = 0
    totalNilai = 0
    angkaIndexMatkul = [0 for i in range (7)]
    hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
    angkaIndex = [4, 3.5, 3, 2.5, 2, 1, 0]
    for i in range (len(banyakSKS)) :
        j = 0
        while True :
            if nilaiIndex[i] == "T" :
                print(f"Nilai mata kuliah {mataKuliah[i]} bermasalah, silahkan konsultasikan ke dosen")
                exit()
            elif nilaiIndex[i] == hurufIndex[j] :
                angkaIndexMatkul[i] = angkaIndex[i]
                break
            else :
                j += 1
        totalNilai += banyakSKS[i] * angkaIndexMatkul[i]
        totalSKS += banyakSKS[i]
    nilaiIP = totalNilai/totalSKS
    return nilaiIP

# Mencari index IP
def MencariIndexIP (nilaiAkhir) :
    hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
    angkaIndex = [4, 3.5, 3, 2.5, 2, 1, 0]
    for i in range (7) :
        if nilaiAkhir >= angkaIndex[i] :
            return hurufIndex[i]

# Mencetak hasil
def CetakHasil (nama, nim, fakultas, nilaiSatuSemester, semester) :
    # PROSEDUR MENCETAK HASIL BELAJAR 1 SEMESTER MAHASISWA
    # Prosedur dibuat untuk mencetak identitas dan hasil belajar mahasiswa dalam jangka waktu 1 semester
    
    # KAMUS
    
    # ALGORITMA
    print("----------HASIL PENILAIAN MAHASISWA----------")
    print("Nama\t\t\t:\t", nama)
    print("NIM\t\t\t:\t", nim)
    print("Fakultas\t\t:\t", fakultas)
    print(f"Nilai akhir Semester {semester+1} \t:\t", nilaiSatuSemester[0])
    print(f"Index akhir Semester {semester+1} \t:\t", nilaiSatuSemester[1])
    print("")

# ALGORITMA
# Judul
print("")
print("----------\tSISTEM PENILAIAN MAHASISWA\t----------")
print("----------\t\tTPB STEI 2022\t\t----------")
print("")

# Identitas
nama = input("Masukkan nama lengkap\t: ")
nim = int(input("Masukkan NIM\t\t: "))
fakultas = KomputasiRekayasa (nim)
print(f"Fakultas\t\t: {fakultas}")
print("")

# Penilaian
# Looping tiap semester
for i in range (2):
    nilaiSatuSemester = SatuSemester (fakultas, i)
    CetakHasil (nama, nim, fakultas, nilaiSatuSemester, i)
    
        



