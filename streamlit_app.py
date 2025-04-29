import streamlit as st
import random

# Atur halaman
st.set_page_config(page_title="Calorie Counting", page_icon="🍱", layout="centered")

# Data makanan sehat
karbo = [
    ("🍚 Nasi Putih", 175, "150 gram"),
    ("🍚 Nasi Merah", 160, "150 gram"),
    ("🌽 Nasi Jagung", 155, "150 gram"),
    ("🥔 Kentang Rebus", 140, "150 gram"),
    ("🌿 Singkong Kukus", 135, "150 gram"),
    ("🥣 Oatmeal", 150, "40 gram"),
    ("🍞 Roti Gandum", 120, "60 gram"),
    ("🍙 Lontong", 130, "150 gram"),
    ("🍜 Mie Jagung", 145, "100 gram"),
    ("🍠 Ubi Rebus", 110, "100 gram"),
]

lauk = [
    ("🍳 Telur Dadar", 180, "60 gram"),
    ("🍽️ Tempe Goreng", 200, "80 gram"),
    ("🍢 Tahu Bacem", 160, "80 gram"),
    ("🍗 Ayam Rebus", 190, "100 gram"),
    ("🐟 Ikan Bakar", 180, "100 gram"),
    ("🥩 Daging Sapi Panggang", 250, "100 gram"),
    ("🦐 Udang Saus Tiram", 170, "100 gram"),
    ("🐟 Tuna Kukus", 160, "100 gram"),
    ("🍗 Ayam Kukus", 175, "100 gram"),
    ("🥚 Telur Rebus", 90, "50 gram"),
]

sayur = [
    ("🥬 Sayur Bayam", 40, "100 gram"),
    ("🥦 Tumis Kangkung", 45, "100 gram"),
    ("🥕 Capcay", 60, "120 gram"),
    ("🍲 Sayur Asem", 50, "150 gram"),
    ("🥣 Sup Wortel", 55, "120 gram"),
    ("🥗 Gado-Gado", 120, "200 gram"),
    ("🥒 Lalapan", 30, "50 gram"),
    ("🍛 Sayur Lodeh", 70, "150 gram"),
    ("🥦 Tumis Brokoli", 60, "100 gram"),
    ("🥗 Urap Sayur", 50, "100 gram"),
]

buah = [
    ("🍌 Pisang", 90, "100 gram"),
    ("🍎 Apel", 80, "125 gram"),
    ("🍈 Pepaya", 70, "150 gram"),
    ("🍊 Jeruk", 60, "130 gram"),
    ("🍉 Semangka", 50, "200 gram"),
    ("🍈 Melon", 55, "150 gram"),
    ("🍍 Nanas", 60, "150 gram"),
    ("🥭 Mangga", 90, "150 gram"),
    ("🍇 Anggur", 70, "100 gram"),
    ("🍎 Salak", 65, "100 gram"),
]

susu = [
    ("🥛 Susu Sapi", 120, "200 gram"),
    ("🌱 Susu Kedelai", 100, "200 gram"),
    ("🍶 Yogurt", 110, "150 gram"),
    ("🥛 Kefir", 100, "150 gram"),
    ("🌰 Susu Almond", 80, "200 gram"),
    ("🥤 Susu UHT", 130, "250 gram"),
    ("🥛 Susu Skim", 90, "200 gram"),
    ("🥄 Susu Bubuk", 150, "25 gram"),
    ("🍫 Susu Coklat", 160, "250 gram"),
    ("🥛 Susu Full Cream", 140, "200 gram"),
]

# Fungsi membuat rekomendasi menu lengkap
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
            f"{k[0]} ({k[2]}) + {l[0]} ({l[2]}) + {s[0]} ({s[2]}) + "
            f"{b[0]} ({b[2]}) + {u[0]} ({u[2]})\n**Total Kalori: {total_kalori} kkal**"
        )
        menu_list.append(menu_str)
    return menu_list

# Fungsi menghitung kalori
def hitung_kalori(b_kg, t_cm, usia=25, gender='Laki-laki'):
    if gender == 'Laki-laki':
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia + 5
    else:
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia - 161
    return int(bmr * 1.2)

# Sidebar untuk navigasi
menu = st.sidebar.selectbox(
    "Navigasi", 
    ["🏠 Halaman Utama", "😎 Perkenalan Kelompok", "🔢 Kalkulator Kalori", "📖 Tentang"]
)

#Mengatur warna latar belakang dan gaya font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #bab86c;  /* Warna latar belakang baru */
        color: #333333;             /* Warna teks baru */
        font-size: 18px;            /* Ukuran font tetap */
    }
    .css-1d391kg {
        color: #c99548;             /* Mengatur warna teks untuk elemen tertentu */
    }
    table {
        border: 2px solid #fb8e54;  /* Garis tabel dengan warna baru */
    }
    th {
        background-color: #fb8e54;  /* Warna latar untuk header tabel */
        color: white;               /* Warna teks untuk header tabel */
    }
    td {
        background-color: #f3e9df;  /* Warna latar untuk sel tabel */
        color: black;               /* Warna teks untuk sel tabel */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Halaman Utama
if menu == "🏠 Halaman Utama":
    st.title("🍱 Calorie Counting - Aplikasi Gizi Sehatmu")
    st.markdown("""
Selamat datang di **Calorie Counting**, aplikasi sederhana untuk membantu kamu:

- 🔢 Menghitung kebutuhan kalori harian  
- 🍽️ Mendapatkan rekomendasi menu 4 Sehat 5 Sempurna  
- 📚 Edukasi gizi seimbang

---

Silakan gunakan menu di sebelah kiri untuk mulai 😊
""")

# Halaman Perkenalan Kelompok
elif menu == "😎 Perkenalan Kelompok":
    st.header("KELOMPOK 6 (E1-PMIP)")

    st.write("""
Kelompok 6 merupakan tim mahasiswa Program Studi Penjaminan Mutu Industri Pangan yang berkolaborasi dalam pengembangan aplikasi ini. Berikut adalah anggota tim beserta NIM masing-masing:

1. Hanan Dzul Hilmi (NIM: 2420601)  
2. Syakira Amalia Sari (NIM: 2420670)  
3. Subhan Zikri (NIM: 2420667)  
4. Nabila Putri Ramadhani (NIM: 2420630)  
5. Clarisha Andini Putri (NIM: 2420582)  
""")

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
        for i, menu in enumerate(rekomendasi, 1):
            st.markdown(f"{i}. {menu}")

# Tentang Aplikasi
elif menu == "📖 Tentang":
    st.title("📖 Tentang Aplikasi Calorie Counting")
    st.markdown("""
Aplikasi ini dibuat untuk memberikan edukasi gizi secara ringan, sederhana, dan menyenangkan.

- Dirancang untuk mendampingi kamu menjaga pola makan sehat 🍽️

**Sumber acuan:**
- Kemenkes RI
- Data USDA & BPOM

---

✨ Terima kasih sudah menggunakan KaloriKu!
""")
