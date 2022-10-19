# PROGRAM SISTEM PENILAIAN MAHASISWA
# Program dibuat untuk menghitung nilai mahasiswa dalam semester tertentu

# KAMUS GLOBAL
# nama, fakultas, programStudi : string
# nim, semester, mataKuliah : int

# FUNCTION AND PROCEDURES    
# Menghitung nilai 1 semester
def SatuSemester (semester) :
    # FUNGSI 
    # Fungsi 
    
    # KAMUS LOKAL
    # 
    
    # ALGORTIMA
    mataKuliah = int(input(f"Berapa banyak mata kuliah dalam semester {semester}: "))
    nilaiAkhir = [0 for i in range (mataKuliah)]
    nilaiIndex = ["*" for i in range (mataKuliah)]
    nilaiMataKuliah = [0 for i in range (mataKuliah)]
    banyakSKS = [0 for i in range (mataKuliah)]
    for i in range (mataKuliah) :
        banyakSKS[i] = int(input(f"Banyak SKS mata kuliah {i+1}: "))
        print("")
        nilaiAkhir[i] = SatuMataKuliah (semester, mataKuliah)
        nilaiIndex[i] = MencariIndexIP (nilaiAkhir[i])
    nilaiIP = MenghitungIP (banyakSKS, nilaiIndex)
    IPSemester = MencariIndexIP (nilaiIP)
    return nilaiIP, IPSemester
        
# Menghitung nilai 1 mata kuliah
def SatuMataKuliah (semester, mataKuliah) :
    # FUNGSI MENGHITUNG NILAI DARI SEMUA MATA KULIAH DALAM 
    # Fungsi dibuat untuk meminta input menghitung nilai akhir dari satu mata kuliah 

    # KAMUS LOKAL
    # semester, mataKuliah : int
    # namaMataKuliah, kodeMataKuliah : string
    # komponenNilai : int
    # nilaiAkhir : float
    # arrayKomponenNilai : arr [0..komponenNilai] of string
    # persentasePenilaian : arr [0..komponenNilai] of int 

    # ALGORITMA
    namaMataKuliah = input("Masukkan nama mata kuliah: ")
    kodeMataKuliah = input("Masukkan kode mata kuliah: ")
    komponenNilai = int(input(f"Berapa banyak komponen penilaian {namaMataKuliah}: "))
    arrayKomponenNilai = ["*" for i in range (komponenNilai)]
    persentasePenilaian = [0 for i in range (komponenNilai)]
    nilaiAkhir = 0
    print("")
    print(f"----------Penilaian {kodeMataKuliah}-{namaMataKuliah}----------")
    for j in range (komponenNilai) :
        print("")
        arrayKomponenNilai[j] = input(f"Nama komponen penilaian ke-{j+1}: ")
        persentasePenilaian[j] = int(input(f"Persentase komponen penilaian ke-{j+1} (dalam persen): "))
        nilaiAkhir += SatuKomponenPenilaian(arrayKomponenNilai[j], persentasePenilaian[j])    
    nilaiAkhir = round(nilaiAkhir, 2)
    print("")
    print(f"Nilai akhir {kodeMataKuliah}-{namaMataKuliah} pada semester {semester} adalah {nilaiAkhir}")
    return nilaiAkhir
    

# Nilai 1 komponen penilaian
def SatuKomponenPenilaian (arrayKomponenNilai, persentasePenilaian) : 
    # FUNGSI MENGHITUNG NILAI DARI SATU KOMPONEN
    # Fungsi dibuat untuk menghitung nilai akhir dari satu komponen penilaian berdasarkan input persentase

    # KAMUS LOKAL
    # arrayKomponenNilai, persentasePenilaian : int
    # banyakInputNilai, nilaiTotal, inputNilai : int
    # nilaiAkhirKomponen : float

    # ALGORITMA
    banyakInputNilai = int(input(f"Berapa banyak input nilai {arrayKomponenNilai}: "))
    nilaiTotal = 0
    for i in range (banyakInputNilai) :
        inputNilai = int(input(f"Masukkan nilai {arrayKomponenNilai} ke-{i+1}: "))
        nilaiTotal += inputNilai
    nilaiAkhirKomponen = ((nilaiTotal/banyakInputNilai)*persentasePenilaian)/100
    return nilaiAkhirKomponen

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
    
# # Input index
# # Digunakan jika ingin menggunakan index sendiri
# hurufIndex = ["A", "AB", "B", "BC", "C", "D", "E"]
# angkaIndex = [0 for i in range (7)]
# for i in range (6) : # Dibawah minimal D pasti nilai E
#     angkaIndex[i] = int(input(f"Masukkan nilai minimal {hurufIndex[i]}: "))
# # print(angkaIndex)
    
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
def CetakHasil (nama, nim, fakultas, programStudi, semester, IPSemester) :
    # PROSEDUR MENCETAK HASIL BELAJAR 1 SEMESTER MAHASISWA
    # Prosedur dibuat untuk mencetak identitas dan hasil belajar mahasiswa dalam jangka waktu 1 semester
    
    # KAMUS
    
    # ALGORITMA
    print("----------HASIL PENILAIAN MAHASISWA----------")
    print("Nama\t\t\t:\t", nama)
    print("NIM\t\t\t:\t", nim)
    print("Fakultas\t\t:\t", fakultas)
    print("Program Studi\t\t:\t", programStudi)
    print(f"Nilai akhir semester {semester} adalah {IPSemester[0]}")
    print(f"Index akhir semester {semester} adalah {IPSemester[1]}")

# MAIN CODE
# Identitas
nama = input("Masukkan nama lengkap: ")
nim = int(input("Masukkan NIM: "))
fakultas = input("Masukkan fakultas: ")
programStudi = input("Masukkan program studi: ")
print("")

# Penilaian
semester = int(input("Menghitung nilai berapa semester: "))
# Looping tiap semester
for i in range (semester) :
    # Mengambil nilai akhir tiap semester
    IPSemester = SatuSemester (semester)
    # Output
    CetakHasil (nama, nim, fakultas, programStudi, semester, IPSemester)
        



