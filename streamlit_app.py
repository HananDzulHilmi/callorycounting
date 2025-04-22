import streamlit as st
from PIL import Image

# Atur konfigurasi halaman
st.set_page_config(page_title="Selamat Datang di KaloriKu", page_icon="🍱", layout="centered")

# Gambar / logo aplikasi (opsional)
# image = Image.open("logo.png")
# st.image(image, use_column_width=True)

# Judul
st.title("🍱 KaloriKu - Aplikasi Gizi Sehatmu")
st.markdown("""
Selamat datang di **KaloriKu**, aplikasi sederhana untuk membantu kamu:

- Menghitung kebutuhan kalori harian berdasarkan berat dan tinggi badan.
- Mendapatkan rekomendasi makanan sehat berdasarkan prinsip 4 Sehat 5 Sempurna.
- Edukasi gizi yang ringan dan menyenangkan untuk semua usia.

---

""")

# Tombol navigasi (bisa diganti pakai multipage atau option-menu)
st.subheader("👀 Mulai Eksplorasi:")
if st.button("🔢 Hitung Kebutuhan Kalori"):
    st.switch_page("kalori_app.py")  # atau arahkan ke halaman lain jika pakai multipage

if st.button("📖 Tentang Gizi Seimbang"):
    st.info("Fitur ini sedang dikembangkan. Nantikan update berikutnya ya! 😄")


import streamlit as st
import random

# Fungsi menghitung kebutuhan kalori berdasarkan rumus Mifflin-St Jeor
def hitung_kalori(b_kg, t_cm, usia=25, gender='Laki-laki'):
    if gender == 'Laki-laki':
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia + 5
    else:
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia - 161
    return int(bmr * 1.2)  # diasumsikan aktivitas ringan

# Data 4 sehat 5 sempurna
karbo = [
    "Nasi Putih", "Nasi Merah", "Nasi Jagung", "Kentang Rebus", "Singkong Kukus", 
    "Oatmeal", "Roti Gandum", "Lontong", "Mie Jagung", "Ubi Rebus"
]

lauk = [
    "Telur Dadar", "Tempe Goreng", "Tahu Bacem", "Ayam Rebus", "Ikan Bakar", 
    "Daging Sapi Panggang", "Udang Saus Tiram", "Tuna Kukus", "Ayam Kukus", "Telur Rebus"
]

sayur = [
    "Sayur Bayam", "Tumis Kangkung", "Capcay", "Sayur Asem", "Sup Wortel", 
    "Gado-Gado", "Lalapan", "Sayur Lodeh", "Tumis Brokoli", "Urap Sayur"
]

buah = [
    "Pisang", "Apel", "Pepaya", "Jeruk", "Semangka", 
    "Melon", "Nanas", "Mangga", "Anggur", "Salak"
]

susu = [
    "Susu Sapi", "Susu Kedelai", "Yogurt", "Kefir", "Susu Almond", 
    "Susu UHT", "Susu Skim", "Susu Bubuk", "Susu Coklat", "Susu Full Cream"
]

# Fungsi membuat rekomendasi menu lengkap
def buat_menu_4_sehat_5_sempurna(jumlah=10):
    menu_list = []
    for _ in range(jumlah):
        menu = f"{random.choice(karbo)} + {random.choice(lauk)} + {random.choice(sayur)} + {random.choice(buah)} + {random.choice(susu)}"
        menu_list.append(menu)
    return menu_list

# Judul aplikasi
st.title("Kalkulator Kebutuhan Kalori Harian")
st.subheader("Dengan Rekomendasi Menu 4 Sehat 5 Sempurna 🍚🥦🥩🍊🥛")

# Input pengguna
nama = st.text_input("Nama kamu")
bb = st.number_input("Berat badan (kg)", min_value=10.0, max_value=300.0, step=0.5)
tb = st.number_input("Tinggi badan (cm)", min_value=50.0, max_value=250.0, step=0.5)
usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Tombol untuk hitung
if st.button("Hitung Kalori"):
    kalori = hitung_kalori(bb, tb, usia, gender)
    st.success(f"{nama}, kebutuhan kalori harianmu diperkirakan sekitar {kalori} kalori.")

    # Tampilkan rekomendasi makanan secara acak
    st.markdown("### Rekomendasi Menu 4 Sehat 5 Sempurna:")
    rekomendasi = buat_menu_4_sehat_5_sempurna(10)
    for i, menu in enumerate(rekomendasi, 1):
        st.markdown(f"{i}. {menu}")
