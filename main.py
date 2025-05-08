import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "72a3f69a9169a1501c9228e234aa5c7c"
URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric"

def hava_durumu_getir():
    sehir = sehir_entry.get()
    if not sehir:
        messagebox.showwarning("Uyari", "Lütfen şehir adi girin.")
        return
    try:
        yanit = requests.get(URL.format(sehir, API_KEY))
        veri = yanit.json()

        if veri["cod"] != 200:
            messagebox.showerror("Hata", f"Şehir bulunamadi: {veri['message']}")
            return

        sehir_adi = veri["name"]
        sicaklik = veri["main"]["temp"]
        hava = veri["weather"][0]["description"]
        nem = veri["main"]["humidity"]

        sonuc = f"{sehir_adi} için hava durumu:\nSicaklik: {sicaklik}°C\nHava: {hava}\nNem: %{nem}"
        sonuc_label.config(text=sonuc)
    except:
        messagebox.showerror("Hata", "Veri alinamadi.")

# Arayüz
pencere = tk.Tk()
pencere.title("Hava Durumu Uygulamasi")

tk.Label(pencere, text="Şehir Girin:").pack()
sehir_entry = tk.Entry(pencere)
sehir_entry.pack()

tk.Button(pencere, text="Hava Durumunu Getir", command=hava_durumu_getir).pack(pady=10)

sonuc_label = tk.Label(pencere, text="", font=("Arial", 12))
sonuc_label.pack(pady=10)

pencere.mainloop()