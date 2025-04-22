import streamlit as st

st.title("🎈 callory counting")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

def hitung_bmr(jenis_kelamin, berat, tinggi, umur):
    if jenis_kelamin == 'Pria':
        bmr = 10 * berat + 6.25 * tinggi - 5 * umur + 5
    else:  # Wanita
        bmr = 10 * berat + 6.25 * tinggi - 5 * umur - 161
    return bmr

st.set_page_config(page_title="Kalkulator Kalori", layout="centered")

st.title("🔥 Kalkulator Kebutuhan Kalori Harian")

st.markdown("Masukkan data kamu untuk menghitung kebutuhan kalori berdasarkan rumus Mifflin-St Jeor.")

nama = st.text_input("Nama")
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
umur = st.number_input("Umur (tahun)", min_value=10, max_value=100, value=25)
berat = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=60.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)
aktivitas = st.selectbox("Tingkat Aktivitas", [
    "Tidak aktif (BMR x 1.2)",
    "Sedikit aktif (BMR x 1.375)",
    "Cukup aktif (BMR x 1.55)",
    "Sangat aktif (BMR x 1.725)",
    "Ekstra aktif (BMR x 1.9)"
])

if st.button("Hitung Kebutuhan Kalori"):
    bmr = hitung_bmr(jenis_kelamin, berat, tinggi, umur)
    faktor_aktivitas = {
        "Tidak aktif (BMR x 1.2)": 1.2,
        "Sedikit aktif (BMR x 1.375)": 1.375,
        "Cukup aktif (BMR x 1.55)": 1.55,
        "Sangat aktif (BMR x 1.725)": 1.725,
        "Ekstra aktif (BMR x 1.9)": 1.9
    }
    kalori_harian = bmr * faktor_aktivitas[aktivitas]

    st.success(f"Hai {nama}, kebutuhan kalori harianmu adalah sekitar {kalori_harian:.2f} kkal.")
