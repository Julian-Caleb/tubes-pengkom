# PROGRAM SISTEM PENILAIAN MAHASISWA TPB STEI
# Program dibuat untuk menghitung nilai mahasiswa dalam 2 semester TPB

# KAMUS GLOBAL
# nama, fakultas, programStudi : string
# nim, semester, mataKuliah : int

# FUNCTION AND PROCEDURES    
# Menghitung nilai 1 semester
def SatuSemester (semester) :
    print("Nanti")
    
# Menghitung nilai 1 mata kuliah
def SatuMataKuliah (semester, mataKuliah) :    
    print("Nanti")
    
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
    print("Program Studi\t\t:\t", programStudi)


# MAIN CODE
# Identitas
nama = input("Masukkan nama lengkap: ")
nim = int(input("Masukkan NIM: "))
fakultas = input("Masukkan fakultas: ")
programStudi = input("Masukkan program studi: ")
print("")

# Penilaian
# Looping tiap semester
for i in range (2):
    nilaiSatuSemester = SatuSemester (i)
    CetakHasil (nama, nim, fakultas, programStudi, nilaiSatuSemester)
    
        



