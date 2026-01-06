import streamlit as st
import pandas as pd
import random
import time
import math

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Portal Tool Serbaguna", page_icon="🛠️", layout="wide")

# --- FUNGSI TOOL 1: KALKULATOR SAHAM ---
def tool_saham():
    st.title("📈 Kalkulator Saham Pro")
    st.caption("Kira untung bersih Bursa Malaysia (Rate 2025)")
    # --- Masukkan kod Kalkulator Saham tuan di sini ---
    # (Saya ringkaskan untuk contoh, tuan paste kod penuh tuan)
    buy_price = st.number_input("Harga Beli", value=0.500, format="%.3f")
    st.info("Tool Saham sedang aktif.")

# --- FUNGSI TOOL 2: COMPOUNDING ---
def tool_compounding():
    st.title("✨ Magic of Compounding")
    # --- Logik Dinamik Tahun yang tuan nak (1-5 tahun) ---
    if 'bil_tahun' not in st.session_state:
        st.session_state.bil_tahun = 3
    
    col_btn1, col_btn2 = st.columns(2)
    if col_btn1.button("➕ Tambah Tahun"):
        if st.session_state.bil_tahun < 5: st.session_state.bil_tahun += 1
    if col_btn2.button("➖ Kurang Tahun"):
        if st.session_state.bil_tahun > 1: st.session_state.bil_tahun -= 1
        
    st.write(f"Rekod: {st.session_state.bil_tahun} Tahun")
    # ... (Sambung kod compounding tuan) ...

# --- FUNGSI TOOL 3: KUIZ SEJARAH ---
def tool_kuiz():
    st.title("💣 Kuiz Sejarah Tahun 5")
    # --- Paste kod Game Bom tuan di sini ---
    if st.button("Mula Kuiz"):
        st.success("Misi Bermula!")

# --- MENU UTAMA (SIDEBAR) ---
with st.sidebar:
    st.title("🏠 Menu Utama")
    nav = st.radio("Pilih Tool:", 
        ["Laman Utama", "Kalkulator Saham", "Magic Compounding", "Kuiz Sejarah Bom"])
    
    st.divider()
    st.caption("Versi Beta 1.0")

# --- LOGIK NAVIGATION ---
if nav == "Laman Utama":
    st.title("🚀 Portal Tool Pintar")
    st.write("Selamat datang! Portal ini menggabungkan semua alatan kewangan dan pendidikan saya dalam satu tempat.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.help("Gunakan Kalkulator Saham untuk kira profit.")
    with col2:
        st.help("Gunakan Compounding untuk rancang masa depan.")
    with col3:
        st.help("Main Kuiz Sejarah untuk asah minda.")

elif nav == "Kalkulator Saham":
    tool_saham()

elif nav == "Magic Compounding":
    tool_compounding()

elif nav == "Kuiz Sejarah Bom":
    tool_kuiz()
