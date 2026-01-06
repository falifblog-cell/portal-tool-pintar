import streamlit as st
import pandas as pd
import random
import time
import math

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🛠️", layout="wide")

# --- CSS GLOBAL ---
st.markdown("""
    <style>
    .stButton button { width: 100%; font-size: 16px; border-radius: 8px; }
    .status-box { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
    .safe { background-color: #d4edda; color: #155724; border: 2px solid #c3e6cb; }
    .warning { background-color: #fff3cd; color: #856404; border: 2px solid #ffeeba; }
    .danger { background-color: #f8d7da; color: #721c24; border: 2px solid #f5c6cb; }
    .boom { background-color: #000000; color: #ff0000; font-size: 30px; border: 3px solid red; }
    .celebration-banner { background-color: #d1e7dd; color: #0f5132; padding: 20px; border-radius: 15px; text-align: center; font-size: 24px; font-weight: 800; border: 3px solid #badbcc; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.02); } 100% { transform: scale(1); } }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANK SOALAN SEJARAH ---
soalan_master = [
    {"soalan": "Apakah gelaran bagi Ketua Utama Negara Malaysia?", "pilihan": ["Yang di-Pertuan Agong", "Perdana Menteri", "Sultan", "Yang di-Pertua Negeri"], "jawapan": "Yang di-Pertuan Agong"},
    {"soalan": "Bunga Raya dipilih sebagai bunga kebangsaan. Berapakah kelopak yang ada padanya?", "pilihan": ["4 Kelopak", "5 Kelopak", "6 Kelopak", "7 Kelopak"], "jawapan": "5 Kelopak"},
    {"soalan": "Lagu 'Negaraku' berasal daripada irama lagu negeri mana?", "pilihan": ["Johor", "Kedah", "Perak", "Selangor"], "jawapan": "Perak"},
    {"soalan": "Warna kuning pada Jalur Gemilang melambangkan apa?", "pilihan": ["Perpaduan Rakyat", "Kesucian Agama", "Keberanian", "Kedaulatan Raja"], "jawapan": "Kedaulatan Raja"},
    {"soalan": "Haiwan apakah yang terdapat pada Jata Negara Malaysia?", "pilihan": ["Gajah", "Harimau", "Singa", "Kijang"], "jawapan": "Harimau"},
    {"soalan": "Siapakah Perdana Menteri Malaysia yang pertama (Bapa Kemerdekaan)?", "pilihan": ["Tun Abdul Razak", "Tun Hussein Onn", "Tunku Abdul Rahman", "Tun Dr Mahathir"], "jawapan": "Tunku Abdul Rahman"},
    {"soalan": "Bahasa Kebangsaan Malaysia ialah?", "pilihan": ["Bahasa Inggeris", "Bahasa Melayu", "Bahasa Ibunda", "Bahasa Baku"], "jawapan": "Bahasa Melayu"},
    {"soalan": "Rukun Negara mempunyai berapa prinsip?", "pilihan": ["3 Prinsip", "4 Prinsip", "5 Prinsip", "6 Prinsip"], "jawapan": "5 Prinsip"},
    {"soalan": "Apakah nama bendera Malaysia?", "pilihan": ["Sang Saka Merah Putih", "Jalur Gemilang", "Harimau Malaya", "Bintang 14"], "jawapan": "Jalur Gemilang"},
    {"soalan": "Institusi Raja Berperlembagaan bermaksud raja bertindak mengikut?", "pilihan": ["Kehendak sendiri", "Perlembagaan Persekutuan", "Nasihat rakyat", "Adat istiadat semata-mata"], "jawapan": "Perlembagaan Persekutuan"}
]

# --- 3. SESSION STATE ---
if 'nav' not in st.session_state: st.session_state.nav = "Utama"
if 'bil_tahun' not in st.session_state: st.session_state.bil_tahun = 3
if 'game_active' not in st.session_state: st.session_state.game_active = False

# --- 4. NAVIGATION SIDEBAR ---
with st.sidebar:
    st.title("🏠 Menu Utama")
    nav_choice = st.radio("Pilih Alatan:", ["Laman Utama", "📈 Kalkulator Saham", "✨ Magic Compounding", "💣 Kuiz Sejarah"], key="main_nav")
    st.divider()
    st.caption("© 2026 Portal Tool Pintar")

# --- TOOL 1: KALKULATOR SAHAM ---
def show_saham():
    st.title("📈 Kalkulator Saham Pro")
    st.caption("Kira untung bersih dengan Rate Rasmi 2025")
    # Tuan boleh paste kod penuh Kalkulator Saham tuan di sini
    st.info("Sila masukkan harga beli dan lot untuk kira untung.")
    # (Contoh ringkas untuk placeholder)
    buy = st.number_input("Harga Beli (RM)", value=0.500, format="%.3f")
    st.write(f"Harga yang anda masukkan: RM{buy}")

# --- TOOL 2: MAGIC COMPOUNDING ---
def show_compounding():
    st.title("✨ Magic of Compounding")
    
    jenis = st.radio("Pilih Cara:", ["Manual", "Ikut Rekod"], horizontal=True)
    
    if jenis == "Manual":
        rate = st.slider("Pulangan Setahun (%)", 1.0, 50.0, 6.0, 0.25)
    else:
        st.write("Bilangan Tahun Rekod:")
        c1, c2, c3 = st.columns([1,1,1])
        if c1.button("➖"): 
            if st.session_state.bil_tahun > 1: st.session_state.bil_tahun -= 1
        if c3.button("➕"): 
            if st.session_state.bil_tahun < 5: st.session_state.bil_tahun += 1
        c2.markdown(f"### {st.session_state.bil_tahun}")
        
        inputs = []
        cols = st.columns(st.session_state.bil_tahun)
        for i in range(st.session_state.bil_tahun):
            inputs.append(cols[i].number_input(f"Thn {i+1} (%)", value=5.0))
        rate = sum(inputs)/len(inputs)
        st.success(f"Purata: {rate:.2f}%")

# --- TOOL 3: KUIZ SEJARAH ---
def show_kuiz():
    if not st.session_state.game_active:
        st.title("💣 Kuiz Sejarah Tahun 5")
        if st.button("Mula Misi"):
            st.session_state.game_active = True
            st.session_state.current_q_index = 0
            st.session_state.wrong_count = 0
            st.session_state.score = 0
            st.session_state.shuff_q = random.sample(soalan_master, 10)
            st.rerun()
    else:
        # Paparan visual bom & soalan (Copy dari kod Sejarah yang saya bagi tadi)
        st.write(f"Soalan {st.session_state.current_q_index + 1}/10")
        if st.button("Keluar Game"):
            st.session_state.game_active = False
            st.rerun()

# --- LOGIK PAPARAN ---
if nav_choice == "Laman Utama":
    st.title("🚀 Portal Tool Pintar")
    st.write("Semua alatan digital anda di bawah satu bumbung.")
elif nav_choice == "📈 Kalkulator Saham":
    show_saham()
elif nav_choice == "✨ Magic Compounding":
    show_compounding()
elif nav_choice == "💣 Kuiz Sejarah":
    show_kuiz()
