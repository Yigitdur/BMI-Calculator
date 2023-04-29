from tkinter import *
import tkinter

# SAYFA
window = Tk()
window.minsize(height=200, width=300)
window.maxsize(height=200, width=300)
window.title("VKİ HESAPLAYICI")
window.config(padx=20, pady=20)


# Buttonİşlevi
def hesapla_button():
    try:
        entryKg = float(kg_entry.get())
        entryBoy = float(boy_entry.get())
        sonuc = entryKg / ((entryBoy/100) ** 2)
        if sonuc < 18.5:
            sonuc_label.config(text="Sonuç: Zayıf - " + str(round(sonuc, 1)))
        if sonuc > 18.5 < 24.9:
            sonuc_label.config(text="Sonuç: Normal Ağırlık - " + str(round(sonuc, 1)))
        if sonuc > 25 < 29.9:
            sonuc_label.config(text="Sonuç: Kilolu - " + str(round(sonuc, 1)))
        if sonuc > 30 < 34.9:
            sonuc_label.config(text="Sonuç: 1. Derece Obez - " + str(round(sonuc, 1)))
        if sonuc > 35 < 39.9:
            sonuc_label.config(text="Sonuç: 2. Derece Obez - " + str(round(sonuc, 1)))
        if sonuc > 40:
            sonuc_label.config(text="Sonuç: 3. Derece Obez - " + str(round(sonuc, 1)))
    except ZeroDivisionError:
        sonuc_label.config(text="Hata! İkinci Sayı 0 Olamaz!")
    except ValueError:
        sonuc_label.config(text="Lütfen Geçerli Bir Sayı Giriniz !")


# KGLABEL
kg_label = tkinter.Label(text="Kilonuzu Giriniz.", pady=5)
kg_label.pack()
# KGENTRY
kg_entry = tkinter.Entry()
kg_entry.focus()
kg_entry.pack()
# BOYLABEL
boy_label = tkinter.Label(text="Boyunuzu Giriniz.", pady=5)
boy_label.pack()
# BOYENTRY
boy_entry = tkinter.Entry()
boy_entry.pack()
# BOŞLUK
bosluk_label = tkinter.Label(text="")
bosluk_label.pack()
# HESAPLABUTONU
hesap_btn = tkinter.Button(text="Hesapla. ", width=15, command=hesapla_button)
hesap_btn.pack()
# SONUCLABEL
sonuc_label = tkinter.Label()
sonuc_label.pack()


window.mainloop()