import streamlit as st
import random

# Atur halaman
st.set_page_config(page_title="KaloriKu", page_icon="🍱", layout="centered")

# Data makanan sehat
karbo = [
    ("🍚 Nasi Putih", "175 kkal", "150 gram"),
    ("🍚 Nasi Merah", "160 kkal", "150 gram"),
    ("🌽 Nasi Jagung", "155 kkal", "150 gram"),
    ("🥔 Kentang Rebus", "140 kkal", "150 gram"),
    ("🌿 Singkong Kukus", "135 kkal", "150 gram"),
    ("🥣 Oatmeal", "150 kkal", "40 gram"),
    ("🍞 Roti Gandum", "120 kkal", "60 gram"),
    ("🍙 Lontong", "130 kkal", "150 gram"),
    ("🍜 Mie Jagung", "145 kkal", "100 gram"),
    ("🍠 Ubi Rebus", "110 kkal", "100 gram"),
]


lauk = [
    ("🍳 Telur Dadar", "180 kkal", "60 gram"),
    ("🍽️ Tempe Goreng", "200 kkal", "80 gram"),
    ("🍢 Tahu Bacem", "160 kkal", "80 gram"),
    ("🍗 Ayam Rebus", "190 kkal", "100 gram"),
    ("🐟 Ikan Bakar", "180 kkal", "100 gram"),
    ("🥩 Daging Sapi Panggang", "250 kkal", "100 gram"),
    ("🦐 Udang Saus Tiram", "170 kkal", "100 gram"),
    ("🐟 Tuna Kukus", "160 kkal", "100 gram"),
    ("🍗 Ayam Kukus", "175 kkal", "100 gram"),
    ("🥚 Telur Rebus", "90 kkal", "50 gram"),
]


sayur = [
    ("🥬 Sayur Bayam", "40 kkal", "100 gram"),
    ("🥦 Tumis Kangkung", "45 kkal", "100 gram"),
    ("🥕 Capcay", "60 kkal", "120 gram"),
    ("🍲 Sayur Asem", "50 kkal", "150 gram"),
    ("🥣 Sup Wortel", "55 kkal", "120 gram"),
    ("🥗 Gado-Gado", "120 kkal", "200 gram"),
    ("🥒 Lalapan", "30 kkal", "50 gram"),
    ("🍛 Sayur Lodeh", "70 kkal", "150 gram"),
    ("🥦 Tumis Brokoli", "60 kkal", "100 gram"),
    ("🥗 Urap Sayur", "50 kkal", "100 gram"),
]

buah = [
    ("🍌 Pisang", "90 kkal", "100 gram"),
    ("🍎 Apel", "80 kkal", "125 gram"),
    ("🍈 Pepaya", "70 kkal", "150 gram"),
    ("🍊 Jeruk", "60 kkal", "130 gram"),
    ("🍉 Semangka", "50 kkal", "200 gram"),
    ("🍈 Melon", "55 kkal", "150 gram"),
    ("🍍 Nanas", "60 kkal", "150 gram"),
    ("🥭 Mangga", "90 kkal", "150 gram"),
    ("🍇 Anggur", "70 kkal", "100 gram"),
    ("🍎 Salak", "65 kkal", "100 gram"),
]


susu = [
    ("🥛 Susu Sapi", "120 kkal", "200 gram"),
    ("🌱 Susu Kedelai", "100 kkal", "200 gram"),
    ("🍶 Yogurt", "110 kkal", "150 gram"),
    ("🥛 Kefir", "100 kkal", "150 gram"),
    ("🌰 Susu Almond", "80 kkal", "200 gram"),
    ("🥤 Susu UHT", "130 kkal", "250 gram"),
    ("🥛 Susu Skim", "90 kkal", "200 gram"),
    ("🥄 Susu Bubuk", "150 kkal", "25 gram"),
    ("🍫 Susu Coklat", "160 kkal", "250 gram"),
    ("🥛 Susu Full Cream", "140 kkal", "200 gram"),
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
