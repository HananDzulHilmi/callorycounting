import streamlit as st
import random

# Atur halaman
st.set_page_config(page_title="Calorie Counting", page_icon="🍱", layout="centered")

# DATA MENU
# ... (Bagian karbo, lauk, sayur, buah, susu tidak diubah karena sudah benar)

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

# Fungsi menghitung kalori berdasarkan input pengguna
def hitung_kalori(nama, berat, tinggi, usia, gender, multiplier):
    if gender.lower() == "laki-laki":
        bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)
    kalori = round(bmr * multiplier)
    return kalori

# Gaya dan Warna
st.markdown(
    """
    <style>
    .stApp {
        background-color: #bab86c;
        color: #333333;
        font-size: 18px;
    }
    .css-1d391kg {
        color: #c99548;
    }
    table {
        border: 2px solid #fb8e54;
    }
    th {
        background-color: #fb8e54;
        color: white;
    }
    td {
        background-color: #f3e9df;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigasi
menu = st.sidebar.selectbox(
    "Navigasi",
    ["🏠 Halaman Utama", "😎 Perkenalan Kelompok", "🔢 Kalkulator Kalori", "📖 Tentang"]
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

# Halaman Perkenalan
elif menu == "😎 Perkenalan Kelompok":
    st.header("KELOMPOK 6 (E1-PMIP)")
    st.write("""
Kelompok 6 merupakan tim mahasiswa Program Studi Penjaminan Mutu Industri Pangan yang berkolaborasi dalam pengembangan aplikasi ini. Berikut adalah anggota tim beserta NIM masing-masing:

1. Hanan Dzul Hilmi (NIM: 2420601)  
2. Syakira Amalia Sari (NIM: 2420670)  
3. Subhan Zikry (NIM: 2420667)  
4. Nabila Putri Ramadhani (NIM: 2420630)  
5. Clarisha Andini Putri (NIM: 2420582)  
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

    aktivitas = st.selectbox(
        "Tingkat Aktivitas Harian",
        [
            "🛌 Sangat ringan (tidak aktif/fisik minimal)",
            "🚶 Ringan (jalan kaki ringan, kerja ringan)",
            "🏃 Sedang (olahraga 3-5 hari/minggu)",
            "🏋️ Berat (aktivitas fisik berat atau olahraga intensif)",
            "🏃‍♂️ Sangat berat (latihan keras tiap hari atau pekerjaan fisik berat)"
        ]
    )

    aktivitas_dict = {
        "🛌 Sangat ringan (tidak aktif/fisik minimal)": 1.2,
        "🚶 Ringan (jalan kaki ringan, kerja ringan)": 1.375,
        "🏃 Sedang (olahraga 3-5 hari/minggu)": 1.55,
        "🏋️ Berat (aktivitas fisik berat atau olahraga intensif)": 1.725,
        "🏃‍♂️ Sangat berat (latihan keras tiap hari atau pekerjaan fisik berat)": 1.9
    }

    if st.button("Hitung Kalori"):
        multiplier = aktivitas_dict[aktivitas]
        kalori = hitung_kalori(nama, bb, tb, usia, gender, multiplier)
        st.success(f"{nama}, kebutuhan kalori harianmu sekitar {kalori} kkal.")
        st.markdown("### Rekomendasi Menu 4 Sehat 5 Sempurna:")
        rekomendasi = buat_menu_4_sehat_5_sempurna(5)
        for i, menu_item in enumerate(rekomendasi, 1):
            st.markdown(f"{i}. {menu_item}")
        st.balloons()

# Halaman Tentang
elif menu == "📖 Tentang":
    st.title("📖 Tentang Aplikasi Calorie Counting")
    st.markdown("""
Aplikasi ini dibuat untuk memberikan edukasi gizi secara ringan, sederhana, dan menyenangkan.  
Dirancang untuk mendampingi kamu menjaga pola makan sehat 🍽️

### Fitur Utama
- 🔢 **Kalkulator Kalori Harian:** Menghitung kebutuhan kalori berdasarkan berat badan, tinggi badan, usia, jenis kelamin, dan tingkat aktivitas.
- 🍱 **Rekomendasi Menu 4 Sehat 5 Sempurna:** Disesuaikan dengan kebutuhan kalori pengguna.
- 📚 **Informasi Edukatif:** Menyediakan pengetahuan seputar gizi dan pola makan seimbang.

Kami berharap aplikasi ini bisa membantu kamu lebih bijak dalam memilih asupan makanan dan menjaga kesehatan tubuh secara menyenangkan. 💪😊
""")
