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
berat = st.number_input("Berat Badan (kg)", min_value=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=1.0)

# Fungsi untuk menghitung BMR (Basal Metabolic Rate) dan kebutuhan kalori harian
def hitung_kalori(berat, tinggi, gender):
    if gender == "Pria":
        bmr = 10 * berat + 6.25 * tinggi - 5 * 5 + 5
    else:
        bmr = 10 * berat + 6.25 * tinggi - 5 * 5 - 161
    kebutuhan_kalori = round(bmr * 1.2)  # Perkiraan kebutuhan kalori untuk aktivitas ringan
