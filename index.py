# PROGRAM SISTEM PENILAIAN MAHASISWA
# Program dibuat untuk menghitung nilai mahasiswa dalam semester tertentu

# KAMUS GLOBAL
# nama, fakultas, programStudi : string
# nim, semester, mataKuliah : int

# FUNCTION 

# Menghitung nilai 1 semester
def SatuSemester (semester) :
    # FUNGSI MENGHITUNG NILAI DARI SATU SEMESTER
    # Fungsi dibuat untuk menghitung nilai akhir dari satu semester dengan meminta input berapa banyak mata kuliah dalam satu semester

    # KAMUS LOKAL
    # semester, mataKuliah, nilaiSatuSemester : float
    # nilaiAkhir : 
    
    # ALGORTIMA
    mataKuliah = int(input(f"Berapa banyak mata kuliah dalam semester {semester}: "))
    nilaiSatuSemester = 0
    for i in range (mataKuliah) :
        nilaiAkhir = SatuMataKuliah (semester, mataKuliah)
        nilaiSatuSemester += nilaiAkhir
    nilaiSatuSemester = nilaiSatuSemester/mataKuliah
    print(f"Nilai akhir pada semester {semester} adalah {nilaiSatuSemester}")
    return nilaiSatuSemester
    
        
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
        nilaiAkhir += SatuKomponen(arrayKomponenNilai[j], persentasePenilaian[j])    
    nilaiAkhir = round(nilaiAkhir, 2)
    print("")
    print(f"Nilai akhir {kodeMataKuliah}-{namaMataKuliah} pada semester {semester} adalah {nilaiAkhir}")
    return nilaiAkhir
    

# Nilai 1 komponen penilaian
def SatuKomponen (arrayKomponenNilai, persentasePenilaian) : 
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

# Mencari index
def MencariIndex () :
    print("nanti")
    
# Menghitung IP
def MenghitungIP () :
    print("nanti")

# Mencetak hasil
def CetakHasil (nama, nim, fakultas, programStudi, semester, nilaiSatuSemester) :
    print("----------HASIL PENILAIAN MAHASISWA----------")
    print("Nama\t\t\t:\t", nama)
    print("NIM\t\t\t:\t", nim)
    print("Fakultas\t\t:\t", fakultas)
    print("Program Studi\t\t:\t", programStudi)
    print(f"Nilai akhir semester{semester}\t:\t{nilaiSatuSemester}")

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
    # Mengambil nilai akhir tiap semester
    nilaiSatuSemester = SatuSemester (semester)
    # Output
    CetakHasil(nama, nim, fakultas, programStudi, semester, nilaiSatuSemester)
        



