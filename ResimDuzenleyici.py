import tkinter as tk # Ekran oluşturma ve düzenleme
from tkinter import filedialog # resim dosyası seçimi
from tkinter import colorchooser # renk seçim ekranı
from PIL import Image, ImageOps, ImageTk, ImageFilter # resim işleme araçları
from tkinter import ttk # combobox elementi

panel = tk.Tk() # ana panel
panel.geometry("1000x600") # panel boyutunu ayarlıyoruz
panel.title("Resim Düzenleyici - KodEgitimi.com")
panel.config(bg="white") # arka plan rengini beyaz yapıyoruz

kalem_renk = "black"
kalem_boyut = 5
dosya_yolu = ""

def resim_sec():
    global dosya_yolu # global degisken olan dosya_yolu na secilen resmin dosya yolunu atıyoruz
    dosya_yolu = filedialog.askopenfilename(initialdir="C:/Users/taho_/source/repos/PythonProjeler/resimler")
    resim = Image.open(dosya_yolu) # secilen resmi programa okutuyoruz
    # simdi resmi kendi arayüzümüze uygun hale getiriyoruz
    genislik, yukseklik = int(resim.width/2), int(resim.height/2)
    resim = resim.resize((genislik, yukseklik), Image.ANTIALIAS)
    canvas.config(width=resim.width, height=resim.height) # resim gosterim alanının boyutunu guncelliyoruz
    resim = ImageTk.PhotoImage(resim) # resmi tkinter formatına ceviriyoruz
    canvas.image = resim # resim alanına duzenledigimiz resmi atıyoruz
    canvas.create_image(0,0, image=resim, anchor="nw")

def cizim_yap(event): # event = tıklama islemi bilgilerini tasıyan obje
    # kalem boyutuna bağlı olarak olusturacağımız kalem çizimi için konumları alalım
    x1, y1 = (event.x - kalem_boyut), (event.y - kalem_boyut)
    x2, y2 = (event.x + kalem_boyut), (event.y + kalem_boyut)
    # oval şekilde kalem çizimini belirtilen renkte ekleyelim
    canvas.create_oval(x1, y1, x2, y2, fill=kalem_renk, outline='')

def renk_degistir():
    global kalem_renk
    kalem_renk = colorchooser.askcolor(title="Kalem Rengi Seç")[1]

def boyut_degistir(boyut):
    global kalem_boyut
    kalem_boyut = boyut

def canvasi_temizle():
    canvas.delete("all") # temizleme işleminde secili resmi tutmak istiyoruz
    canvas.create_image(0,0, image=canvas.image, anchor="nw")

def filtreyi_uygula(filtre):
    resim = Image.open(dosya_yolu)
    genislik, yukseklik = int(resim.width/2), int(resim.height/2)
    resim = resim.resize((genislik, yukseklik), Image.ANTIALIAS)
    if filtre == "Siyah Beyaz":
        resim = ImageOps.grayscale(resim)
    elif filtre == "Bulanık":
        resim = resim.filter(ImageFilter.BLUR)
    elif filtre == "Kabartma":
        resim = resim.filter(ImageFilter.EMBOSS)
    elif filtre == "Keskin":
        resim = resim.filter(ImageFilter.SHARPEN)
    elif filtre == "Yumuşak":
        resim = resim.filter(ImageFilter.SMOOTH)
    resim = ImageTk.PhotoImage(resim)
    canvas.image = resim
    canvas.create_image(0,0,image=resim, anchor="nw")

sol_bolum = tk.Frame(panel, width=200, height=600, bg="white") # paneldeki buton bölümünü olusturalım
sol_bolum.pack(side="left", fill="y") # bölümün konumu belirtiliyor

canvas = tk.Canvas(panel, width=750, height=600) # resmi gosterecegimizi alanı olusturalım
canvas.pack()

resim_butonu = tk.Button(sol_bolum, text="Resim Sec", command=resim_sec, bg="white") # resim secme butonunu olusturalım
resim_butonu.pack(padx=15, pady= 15) # soldan ve yukarıdan 15 birim bosluk bırakalım

renk_butonu = tk.Button(sol_bolum, text="Kalem Rengini Degistir", command=renk_degistir, bg="white")
renk_butonu.pack(padx=15, pady=15)

kalem_boyutu_bolumu = tk.Frame(sol_bolum, bg="white") # kalem boyutu radio butonlarının yer aldıgı alan
kalem_boyutu_bolumu.pack(pady=15)

# command kısmında 'lambda' notasyonu girdi gönderilen bir metod çağırdığımız için kullanıldı
kalem_boyutu_1 = tk.Radiobutton(kalem_boyutu_bolumu, text="Küçük", value=3, command=lambda: boyut_degistir(3), bg="white")
kalem_boyutu_1.pack(side="left")
kalem_boyutu_2 = tk.Radiobutton(kalem_boyutu_bolumu, text="Orta", value=5, command=lambda: boyut_degistir(5), bg="white")
kalem_boyutu_2.pack(side="left")
kalem_boyutu_2.select() # baslangıçta orta boy secili kalsın istiyoruz
kalem_boyutu_3 = tk.Radiobutton(kalem_boyutu_bolumu, text="Büyük", value=7, command=lambda: boyut_degistir(7), bg="white")
kalem_boyutu_3.pack(side="left")

# temizleme butonu ile kalem çizimleri siliniyor.
temizle_butonu = tk.Button(sol_bolum, text="Temizle", command=canvasi_temizle, bg="#FF9797")
temizle_butonu.pack(pady=15)

filtre_etiketi = tk.Label(sol_bolum, text="Filtre Sec", bg="white")
filtre_etiketi.pack()
# filtre seçeneklerini seçim kutucuğuna ekliyoruz
filtre_secim_kutucugu = ttk.Combobox(sol_bolum, values=["Siyah Beyaz", "Bulanık", "Kabartma", "Keskin", "Yumuşak"])
filtre_secim_kutucugu.pack()
# olusturdugumuz secim kutucugunda secim yapıldıgında secimi 'filtreyi_uygula' metoduna gonderiyoruz
filtre_secim_kutucugu.bind("<<ComboboxSelected>>", lambda event: filtreyi_uygula(filtre_secim_kutucugu.get()))

canvas.bind("<B1-Motion>", cizim_yap) # Eğer canvas üzerinde mouse a sol tıklama ile çizim yapılırsa 'cizim_yap' metodunu çalıştırıyoruz

panel.mainloop() # paneli ayaga kaldıralım