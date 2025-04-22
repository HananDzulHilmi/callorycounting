import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="Calorie Caounting", page_icon="🍱", layout="centered")

# Data makanan: (emoji + nama, kalori per porsi, berat gram)
karbo = [
    ("🍚 Nasi Putih", 175, 150), ("🍚 Nasi Merah", 160, 150), ("🌽 Nasi Jagung", 155, 150),
    ("🥔 Kentang Rebus", 140, 150), ("🌿 Singkong Kukus", 135, 150), ("🥣 Oatmeal", 150, 40),
    ("🍞 Roti Gandum", 120, 60), ("🍙 Lontong", 130, 150), ("🍜 Mie Jagung", 145, 100), ("🍠 Ubi Rebus", 110, 100)
]

lauk = [
    ("🍳 Telur Dadar", 180, 60), ("🍽️ Tempe Goreng", 200, 80), ("🍢 Tahu Bacem", 160, 80),
    ("🍗 Ayam Rebus", 190, 100), ("🐟 Ikan Bakar", 180, 100), ("🥩 Daging Sapi Panggang", 250, 100),
    ("🦐 Udang Saus Tiram", 170, 100), ("🐟 Tuna Kukus", 160, 100), ("🍗 Ayam Kukus", 175, 100), ("🥚 Telur Rebus", 90, 50)
]

sayur = [
    ("🥬 Sayur Bayam", 40, 100), ("🥦 Tumis Kangkung", 45, 100), ("🥕 Capcay", 60, 120),
    ("🍲 Sayur Asem", 50, 150), ("🥣 Sup Wortel", 55, 120), ("🥗 Gado-Gado", 120, 200),
    ("🥒 Lalapan", 30, 50), ("🍛 Sayur Lodeh", 70, 150), ("🥦 Tumis Brokoli", 60, 100), ("🥗 Urap Sayur", 50, 100)
]

buah = [
    ("🍌 Pisang", 90, 100), ("🍎 Apel", 80, 125), ("🍈 Pepaya", 70, 150), ("🍊 Jeruk", 60, 130),
    ("🍉 Semangka", 50, 200), ("🍈 Melon", 55, 150), ("🍍 Nanas", 60, 150), ("🥭 Mangga", 90, 150),
    ("🍇 Anggur", 70, 100), ("🍎 Salak", 65, 100)
]

susu = [
    ("🥛 Susu Sapi", 120, 200), ("🌱 Susu Kedelai", 100, 200), ("🍶 Yogurt", 110, 150),
    ("🥛 Kefir", 100, 150), ("🌰 Susu Almond", 80, 200), ("🥤 Susu UHT", 130, 250),
    ("🥛 Susu Skim", 90, 200), ("🥄 Susu Bubuk", 150, 25), ("🍫 Susu Coklat", 160, 250), ("🥛 Susu Full Cream", 140, 200)
]

# Fungsi hitung kalori harian
def hitung_kalori(bb, tb, usia=25, gender='Laki-laki'):
    if gender == 'Laki-laki':
        bmr = 10 * bb + 6.25 * tb - 5 * usia + 5
    else:
        bmr = 10 * bb + 6.25 * tb - 5 * usia - 161
    return int(bmr * 1.2)

# Fungsi buat menu
def buat_menu_4_sehat_5_sempurna(jumlah=10):
    menu_list = []
    for _ in range(jumlah):
        k = random.choice(karbo)
        l = random.choice(lauk)
        s = random.choice(sayur)
        b = random.choice(buah)
        u = random.choice(susu)

        total_kalori = k[1] + l[1] + s[1] + b[1] + u[1]

        menu_str = (
            f"{k[0]} — {k[1]} kkal / {k[2]} gr + "
            f"{l[0]} — {l[1]} kkal / {l[2]} gr + "
            f"{s[0]} — {s[1]} kkal / {s[2]} gr + "
            f"{b[0]} — {b[1]} kkal / {b[2]} gr + "
            f"{u[0]} — {u[1]} kkal / {u[2]} gr"
        )

        menu_list.append((menu_str, total_kalori))
    return menu_list

# Navigasi
menu = st.sidebar.selectbox("Navigasi", ["🏠 Halaman Utama", "🔢 Kalkulator Kalori", "📖 Tentang"])

# Halaman Utama
if menu == "🏠 Halaman Utama":
    st.title("🍱 KaloriKu - Aplikasi Gizi Sehatmu")
    st.markdown("""
Selamat datang di **KaloriKu**, aplikasi sederhana untuk membantu kamu:

- 🔢 Menghitung kebutuhan kalori harian
- 🍽️ Mendapatkan rekomendasi menu 4 Sehat 5 Sempurna
- 📚 Edukasi gizi seimbang

Silakan pilih fitur dari sidebar 👈 untuk memulai!
""")
    st.caption("Dibuat dengan ❤️ oleh kamu, untuk kamu dan Audrey 🍥")

# Kalkulator Kalori
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
        st.success(f"{nama}, kebutuhan kalori harianmu sekitar {kalori} kkal.")
        st.markdown("### Rekomendasi Menu 4 Sehat 5 Sempurna:")
        rekomendasi = buat_menu_4_sehat_5_sempurna(10)
        for i, (menu_text, total) in enumerate(rekomendasi, 1):
            st.markdown(f"**{i}. {menu_text}**\n\n🔢 Total Kalori: `{total} kkal`")

# Halaman Tentang
elif menu == "📖 Tentang":
    st.title("📖 Tentang Aplikasi KaloriKu")
    st.markdown("""
Aplikasi ini dibuat untuk memberikan edukasi gizi secara ringan, sederhana, dan menyenangkan.

- Dirancang untuk mendampingi kamu menjaga pola makan sehat 🍽️
- Cocok untuk semua usia, terutama buat yang sedang LDR dan pengen jagain pola makan satu sama lain 😋

Sumber acuan:
- Kemenkes RI
- Data USDA & BPOM

✨ Terima kasih sudah menggunakan KaloriKu!
""")
