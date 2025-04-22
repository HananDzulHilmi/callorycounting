import streamlit as st

# Fungsi menghitung BMR (Mifflin-St Jeor)
def hitung_bmr(jenis_kelamin, berat, tinggi, umur):
    if jenis_kelamin == 'Pria':
        return 10 * berat + 6.25 * tinggi - 5 * umur + 5
    else:  # Wanita
        return 10 * berat + 6.25 * tinggi - 5 * umur - 161

# Mapping tingkat aktivitas ke faktor kalori
faktor_aktivitas = {
    "Tidak aktif (BMR x 1.2)": 1.2,
    "Sedikit aktif (BMR x 1.375)": 1.375,
    "Cukup aktif (BMR x 1.55)": 1.55,
    "Sangat aktif (BMR x 1.725)": 1.725,
    "Ekstra aktif (BMR x 1.9)": 1.9
}

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Kalori", layout="centered")
st.title("🔥 Kalkulator Kebutuhan Kalori Harian")
st.markdown("### Hitung kebutuhan kalori harian kamu berdasarkan berat badan, tinggi badan, dan aktivitas.")

# Input Form
with st.form("form_kalori"):
    nama = st.text_input("Nama lengkap")
    jenis_kelamin = st.radio("Jenis Kelamin", ["Pria", "Wanita"], horizontal=True)
    umur = st.number_input("Umur (tahun)", min_value=10, max_value=100, value=25)
    berat = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=60.0)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)
    aktivitas = st.selectbox("Tingkat Aktivitas", list(faktor_aktivitas.keys()))
    submit = st.form_submit_button("Hitung Kalori")

# Logika setelah tombol diklik
if submit:
    if not nama:
        st.warning("Nama tidak boleh kosong.")
    else:
        bmr = hitung_bmr(jenis_kelamin, berat, tinggi, umur)
        kalori = bmr * faktor_aktivitas[aktivitas]
        
        st.success(f"📊 Hai **{nama}**, kebutuhan kalori harian kamu adalah **{kalori:.2f} kkal**.")
        st.caption("Perhitungan menggunakan rumus Mifflin-St Jeor berdasarkan data yang kamu masukkan.")
