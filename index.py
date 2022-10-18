# PROGRAM SISTEM PENILAIAN MAHASISWA
# Program dibuat untuk menghitung nilai mahasiswa dalam semester tertentu

# KAMUS
# nama, fakultas, programStudi : string
# nim, semester, mataKuliah : int

# FUNCTION 
# Menghitung nilai 1 semester
def SatuSemester (semester, mataKuliah) :
    for i in range (semester) :
        SatuMataKuliah(semester, mataKuliah)
        
# Menghitung nilai 1 mata kuliah
def SatuMataKuliah (semester, mataKuliah) :
    for i in range (mataKuliah) :
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
            persentasePenilaian[j] = int(input(f"Persentase komponen penilaian ke-{j+1}: "))
            nilaiAkhir += SatuKomponen(arrayKomponenNilai[j], persentasePenilaian[j])    
        nilaiAkhir = str(round(nilaiAkhir, 2))
        print("")
        print(f"Nilai akhir {kodeMataKuliah}-{namaMataKuliah} pada semester {semester} adalah {nilaiAkhir}")

# Nilai 1 komponen penilaian
def SatuKomponen (arrayKomponenNilai, persentasePenilaian) : 
    banyakInputNilai = int(input(f"Berapa banyak input nilai {arrayKomponenNilai}: "))
    nilaiTotal = 0
    for i in range (banyakInputNilai) :
        inputNilai = int(input(f"Masukkan nilai {arrayKomponenNilai} ke-{i+1}: "))
        nilaiTotal += inputNilai
    nilaiAkhirKomponen = ((nilaiTotal/banyakInputNilai)*persentasePenilaian)/100
    return nilaiAkhirKomponen

# Mencari index
def MencariIndex () :
    print("nanti")
    
# Menghitung IP
def MenghitungIP () :
    print("nanti")

# Mencetak hasil
def CetakHasil (nama, nim, fakultas, programStudi, test) :
    print("HASIL PENILAIAN MAHASISWA")
    print("Nama\t\t:\t", nama)
    print("NIM\t\t:\t", nim)
    print("Fakultas\t:\t", fakultas)
    print("Program Studi\t:\t", programStudi)

# MAIN CODE
# Identitas
nama = input("Masukkan nama lengkap: ")
nim = int(input("Masukkan NIM: "))
fakultas = input("Masukkan fakultas: ")
programStudi = input("Masukkan program studi: ")

# Penilaian
semester = int(input("Menghitung nilai berapa semester: "))
# Looping tiap semester
for i in range (semester) :
    # Declare variabel array
    mataKuliah = int(input(f"Berapa banyak mata kuliah dalam semester {semester}: "))
    # Subprogram menghitung nilai satu mata kuliah
    SatuMataKuliah(semester, mataKuliah)
    # Output
    CetakHasil(nama, nim, fakultas, programStudi)
        



