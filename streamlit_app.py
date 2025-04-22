import streamlit as st
import random

# Atur halaman
st.set_page_config(page_title="Calorie Counting", page_icon="🍱", layout="centered")

# Data makanan sehat
karbo icon_image=image.open("🍚")= [
    "Nasi Putih", "Nasi Merah", "Nasi Jagung", "Kentang Rebus", "Singkong Kukus", 
    "Oatmeal", "Roti Gandum", "Lontong", "Mie Jagung", "Ubi Rebus"
]

lauk icon_image=image.open("🍗")= [
    "Telur Dadar", "Tempe Goreng", "Tahu Bacem", "Ayam Rebus", "Ikan Bakar", 
    "Daging Sapi Panggang", "Udang Saus Tiram", "Tuna Kukus", "Ayam Kukus", "Telur Rebus"
]

sayur icon_image=image.open("🥬")= [
    "Sayur Bayam", "Tumis Kangkung", "Capcay", "Sayur Asem", "Sup Wortel", 
    "Gado-Gado", "Lalapan", "Sayur Lodeh", "Tumis Brokoli", "Urap Sayur"
]

buah icon_image=image.open("🍇")= [
    "Pisang", "Apel", "Pepaya", "Jeruk", "Semangka", 
    "Melon", "Nanas", "Mangga", "Anggur", "Salak"
]

susu icon_image=image.open("🥛")= [
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

# Fungsi menghitung kalori
def hitung_kalori(b_kg, t_cm, usia=25, gender='Laki-laki'):
    if gender == 'Laki-laki':
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia + 5
    else:
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia - 161
    return int(bmr * 1.2)

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Navigasi", ["🏠 Halaman Utama", "🔢 Kalkulator Kalori", "📖 Tentang"])

# Halaman Utama
if menu == "🏠 Halaman Utama":
    st.title("🍱 KaloriKu - Aplikasi Gizi Sehatmu")
    st.markdown("""
Selamat datang di **KaloriKu**, aplikasi sederhana untuk membantu kamu:

- 🔢 Menghitung kebutuhan kalori harian
- 🍽️ Mendapatkan rekomendasi menu 4 Sehat 5 Sempurna
- 📚 Edukasi gizi seimbang

---

Silakan pilih fitur dari sidebar 👈 untuk memulai!
    """)
   
# Halaman Kalkulator Kalori
elif menu == "🔢 Kalkulator Kalori":
    st.title("🔢 Kalkulator Kebutuhan Kalori Harian")
    st.subheader("Dengan Rekomendasi Menu 4 Sehat 5 Sempurna 🍚🥦🥩🍊🥛")

    nama = st.text_input("Nama kamu")
    bb = st.number_input("Berat badan (kg)", min_value=10.0, max_value=300.0, step=0.5)
    tb = st.number_input("Tinggi badan (cm)", min_value=50.0, max_value=250.0, step=0.5)
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
    gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])

    if st.button("Hitung Kalori"):
        kalori = hitung_kalori(bb, tb, usia, gender)
        st.success(f"{nama}, kebutuhan kalori harianmu sekitar {kalori} kalori.")
        st.markdown("### Rekomendasi Menu 4 Sehat 5 Sempurna:")
        rekomendasi = buat_menu_4_sehat_5_sempurna(10)
        for i, menu in enumerate(rekomendasi, 1):
            st.markdown(f"{i}. {menu}")

# Halaman Tentang
elif menu == "📖 Tentang":
    st.title("📖 Tentang Aplikasi KaloriKu")
    st.markdown("""
Aplikasi ini dibuat untuk memberikan edukasi gizi secara ringan, sederhana, dan menyenangkan.

- Dirancang untuk mendampingi kamu menjaga pola makan sehat 🍽️

Sumber acuan:
- Kemenkes RI
- Data USDA & BPOM

---

✨ Terima kasih sudah menggunakan KaloriKu!
""")
