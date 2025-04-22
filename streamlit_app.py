import streamlit as st
import random

# Set konfigurasi halaman
st.set_page_config(page_title="calorie counting", page_icon="🍱", layout="centered")

# DATA dengan emoji dan estimasi kalori (kkal per porsi)
 # Data makanan
                karbo = [
                    ("🍚 Nasi Putih", "175 kkal", "150 gram"),
                    ("🍞 Roti Gandum", "120 kkal", "60 gram"),
                    ("🥣 Oatmeal", "150 kkal", "40 gram"),
                    ("🥔 Kentang Rebus", "140 kkal", "150 gram"),
                    ("🍠 Ubi Rebus", "110 kkal", "100 gram")
                ]
                lauk = [
                    ("🍳 Telur Dadar", "180 kkal", "60 gram"),
                    ("🍽️ Tempe Goreng", "200 kkal", "80 gram"),
                    ("🐟 Ikan Bakar", "180 kkal", "100 gram"),
                    ("🍗 Ayam Kukus", "175 kkal", "100 gram"),
                    ("🥩 Daging Sapi", "250 kkal", "100 gram")
                ]
                sayur = [
                    ("🥬 Sayur Bayam", "40 kkal", "100 gram"),
                    ("🥦 Tumis Brokoli", "60 kkal", "100 gram"),
                    ("🍲 Sayur Asem", "50 kkal", "150 gram"),
                    ("🥗 Urap Sayur", "50 kkal", "100 gram"),
                    ("🥕 Capcay", "60 kkal", "120 gram")
                ]
                buah = [
                    ("🍌 Pisang", "90 kkal", "100 gram"),
                    ("🍎 Apel", "80 kkal", "125 gram"),
                    ("🍊 Jeruk", "60 kkal", "130 gram"),
                    ("🍈 Pepaya", "70 kkal", "150 gram"),
                    ("🍇 Anggur", "70 kkal", "100 gram")
                ]
                susu = [
                    ("🥛 Susu Sapi", "120 kkal", "200 gram"),
                    ("🌱 Susu Kedelai", "100 kkal", "200 gram"),
                    ("🍶 Yogurt", "110 kkal", "150 gram"),
                    ("🌰 Susu Almond", "80 kkal", "200 gram"),
                    ("🥛 Susu Full Cream", "140 kkal", "200 gram")
                ]

                # Pilih makanan secara acak
                selected_karbo = random.choice(karbo)
                selected_lauk = random.choice(lauk)
                selected_sayur = random.choice(sayur)
                selected_buah = random.choice(buah)
                selected_susu = random.choice(susu)

                menu = [selected_karbo, selected_lauk, selected_sayur, selected_buah, selected_susu]
                total_kalori = 0
                kalori_list = []

                st.subheader("🍱 Rekomendasi Menu")
                for item in menu:
                    nama, kalori, berat = item
                    kal = int(kalori.split()[0])
                    kalori_list.append(kal)
                    total_kalori += kal
                    st.markdown(f"✅ **{nama}** — {kalori}, {berat}")

                st.markdown(f"### 🔢 Total Kalori Menu: **{total_kalori} kkal**")

                # Pie Chart
                fig, ax = plt.subplots()
                ax.pie(kalori_list, labels=["Karbo", "Lauk", "Sayur", "Buah", "Susu"], autopct='%1.1f%%')
                ax.axis('equal')
                st.pyplot(fig)

                if st.button("💾 Simpan Menu Ini"):
                    st.session_state['history'].append({
                        "menu": menu,
                        "total": total_kalori
                    })
                    st.success("✅ Menu berhasil disimpan!")
            else:
                st.error("Masukkan berat dan tinggi badan yang valid.")
    else:
        st.warning("Silakan login terlebih dahulu di sidebar.")
# Fungsi menghitung kebutuhan kalori
def hitung_kalori(b_kg, t_cm, usia=25, gender='Laki-laki'):
    if gender == 'Laki-laki':
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia + 5
    else:
        bmr = 10 * b_kg + 6.25 * t_cm - 5 * usia - 161
    return int(bmr * 1.2)

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

---

Silakan pilih fitur dari sidebar 👈 untuk memulai!
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
        st.success(f"{nama}, kebutuhan kalori harianmu sekitar {kalori} kalori.")
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


Sumber acuan:
- Kemenkes RI
- Data USDA & BPOM

---

✨ Terima kasih sudah menggunakan KaloriKu!
""")
