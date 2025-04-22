import streamlit as st
import random
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Kalkulator Kalori", layout="centered")

# Judul Halaman
st.title("🍽️ Kalkulator Kalori & Menu 4 Sehat 5 Sempurna")

# Sidebar untuk memilih jenis kelamin
st.sidebar.header("🔒 Pilih Jenis Kelamin")
gender = st.sidebar.selectbox("Pilih Jenis Kelamin", ["Pria", "Wanita"])

# Input berat dan tinggi badan
berat = st.number_input("Berat Badan (kg)", min_value=1.0, step=0.1)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=1.0, step=1)

# Fungsi untuk menghitung BMR (Basal Metabolic Rate) dan kebutuhan kalori harian
def hitung_kalori(berat, tinggi, gender):
    if gender == "Pria":
        bmr = 10 * berat + 6.25 * tinggi - 5 * 5 + 5
    else:
        bmr = 10 * berat + 6.25 * tinggi - 5 * 5 - 161
    kebutuhan_kalori = round(bmr * 1.2)  # Perkiraan kebutuhan kalori untuk aktivitas ringan
    return kebutuhan_kalori

# Data makanan per jenis (karbo, lauk, sayur, buah, susu)
karbo = [
    ("🍚 Nasi Putih", 175, "150 gram"),
    ("🍞 Roti Gandum", 120, "60 gram"),
    ("🥣 Oatmeal", 150, "40 gram"),
    ("🥔 Kentang Rebus", 140, "150 gram"),
    ("🍠 Ubi Rebus", 110, "100 gram")
]
lauk = [
    ("🍳 Telur Dadar", 180, "60 gram"),
    ("🍽️ Tempe Goreng", 200, "80 gram"),
    ("🐟 Ikan Bakar", 180, "100 gram"),
    ("🍗 Ayam Kukus", 175, "100 gram"),
    ("🥩 Daging Sapi", 250, "100 gram")
]
sayur = [
    ("🥬 Sayur Bayam", 40, "100 gram"),
    ("🥦 Tumis Brokoli", 60, "100 gram"),
    ("🍲 Sayur Asem", 50, "150 gram"),
    ("🥗 Urap Sayur", 50, "100 gram"),
    ("🥕 Capcay", 60, "120 gram")
]
buah = [
    ("🍌 Pisang", 90, "100 gram"),
    ("🍎 Apel", 80, "125 gram"),
    ("🍊 Jeruk", 60, "130 gram"),
    ("🍈 Pepaya", 70, "150 gram"),
    ("🍇 Anggur", 70, "100 gram")
]
susu = [
    ("🥛 Susu Sapi", 120, "200 gram"),
    ("🌱 Susu Kedelai", 100, "200 gram"),
    ("🍶 Yogurt", 110, "150 gram"),
    ("🌰 Susu Almond", 80, "200 gram"),
    ("🥛 Susu Full Cream", 140, "200 gram")
]

# Pilih makanan untuk 3 waktu makan
def pilih_menu():
    menu = []
    for waktu in ["Pagi", "Siang", "Malam"]:
        selected_karbo = random.choice(karbo)
        selected_lauk = random.choice(lauk)
        selected_sayur = random.choice(sayur)
        selected_buah = random.choice(buah)
        selected_susu = random.choice(susu)
        menu.append({
            "waktu": waktu,
            "menu": [selected_karbo, selected_lauk, selected_sayur, selected_buah, selected_susu]
        })
    return menu

# Menampilkan hasil
if st.button("Hitung Kalori & Tampilkan Menu"):
    if berat > 0 and tinggi > 0:
        kebutuhan_kalori = hitung_kalori(berat, tinggi, gender)
        st.success(f"🔢 Kebutuhan Kalori Harianmu: {kebutuhan_kalori} kkal")

        # Rekomendasi menu
        menu_pilih = pilih_menu()
        total_kalori = 0
        kalori_list = []
        label_list = []

        st.subheader("🍱 Rekomendasi Menu 4 Sehat 5 Sempurna")

        # Tampilkan menu per waktu makan
        for waktu in menu_pilih:
            st.markdown(f"### {waktu}")
            menu = waktu['menu']
            waktu_kalori = 0
            for item in menu:
                nama, kalori, berat = item
                kalori_list.append(kalori)
                waktu_kalori += kalori
                st.markdown(f"✅ **{nama}** — {kalori} kkal, {berat}")
            st.markdown(f"**Total Kalori {waktu}: {waktu_kalori} kkal**\n")

            total_kalori += waktu_kalori

        st.markdown(f"### 🔢 Total Kalori Seluruh Menu: **{total_kalori} kkal**")

        if total_kalori > kebutuhan_kalori:
            st.warning("⚠️ Menu melebihi kebutuhan kalori harianmu.")
        elif total_kalori < kebutuhan_kalori:
            st.info("ℹ️ Menu di bawah kebutuhan kalori.")
        else:
            st.success("✅ Menu sesuai kebutuhan kalori harianmu.")

        # Pie chart untuk komposisi kalori
        fig, ax = plt.subplots()
        ax.pie(kalori_list, labels=["Karbo", "Lauk", "Sayur", "Buah", "Susu"] * 3, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

    else:
        st.error("Masukkan berat dan tinggi badan yang valid.")
