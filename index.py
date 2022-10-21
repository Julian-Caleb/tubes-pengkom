# PROGRAM SISTEM PENILAIAN MAHASISWA TPB STEI
# Program dibuat untuk menghitung nilai mahasiswa dalam 2 semester TPB

# KAMUS GLOBAL
# 

# FUNCTION AND PROCEDURES    
# Komputasi atau Rekayasa
def KomputasiRekayasa (nim) :
    if nim // 100000 == 196 :
        return "Komputasi"
    else : # == 165
        return "Rekayasa"

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
            
    SatuMataKuliah (semester, mataKuliahSemester)
    
# Menghitung nilai 1 mata kuliah
def SatuMataKuliah (semester, mataKuliah) :
    print(f"----------\tPENILAIAN SEMESTER {semester}\t----------")  
    print("")  
    for i in range (6) :
        print(mataKuliah[0][i], "-", mataKuliah[1][i], "-", mataKuliah[2][i])
    
# Nilai 1 komponen penilaian
def SatuKomponenPenilaian (arrayKomponenNilai, persentasePenilaian) : 
    print("Nanti")
    
# Mencari index satu mata kuliah
def MencariIndexNilaiAkhir (nilaiAkhir) :
    # inputIndex()
    hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
    angkaIndex = [75, 68, 60, 53, 45, 38, 0]
    bermasalah = input("Apakah bermasalah (Y/N):")
    if bermasalah == "Y" :
        return "T"
    else :
        for i in range (7) :
            if nilaiAkhir >= angkaIndex[i] :
                return hurufIndex[i]
    
# Menghitung IP
def MenghitungIP (banyakSKS, nilaiIndex) :
    totalSKS = 0
    totalNilai = 0
    angkaIndexMatkul = [0 for i in range (7)]
    hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
    angkaIndex = [4, 3.5, 3, 2.5, 2, 1, 0]
    for i in range (len(banyakSKS)) :
        j = 0
        while True :
            if nilaiIndex[i] == hurufIndex[j] :
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
def CetakHasil (nama, nim, fakultas, programStudi, nilaiSatuSemester) :
    # PROSEDUR MENCETAK HASIL BELAJAR 1 SEMESTER MAHASISWA
    # Prosedur dibuat untuk mencetak identitas dan hasil belajar mahasiswa dalam jangka waktu 1 semester
    
    # KAMUS
    
    # ALGORITMA
    print("----------HASIL PENILAIAN MAHASISWA----------")
    print("Nama\t\t\t:\t", nama)
    print("NIM\t\t\t:\t", nim)
    print("Fakultas\t\t:\t", fakultas)


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
    CetakHasil (nama, nim, fakultas, nilaiSatuSemester)
    
        



