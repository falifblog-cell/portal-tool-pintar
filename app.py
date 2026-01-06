import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🚀", layout="centered")

# --- 2. CUSTOM CSS (FIXED HEIGHT + CENTERED BUTTONS) ---
st.markdown("""
    <style>
    /* Sembunyikan header/footer asal */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* BACKGROUND CINEMATIC */
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), 
                          url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    /* GLASSMORPHISM CARD DENGAN UNIFORM SIZE */
    .tool-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 35px 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.4s ease;
        
        /* Teknik Flexbox untuk samakan saiz & letak butang di bawah */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        min-height: 400px; /* Samakan ketinggian semua kotak */
        margin-bottom: 20px;
    }

    .tool-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(0, 210, 255, 0.5);
    }

    /* TYPOGRAPHY */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }

    /* LOGIK BUTANG DI TENGAH BAWAH KOTAK */
    .stButton {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-top: auto; /* Paksa butang ke bahagian bawah kotak */
    }

    .stButton > button {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: white !important;
        border: none;
        padding: 10px 30px !important;
        border-radius: 50px !important;
        font-weight: 700;
        width: auto !important;
        min-width: 180px;
        transition: 0.3s all;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
    }

    .stButton > button:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.6);
    }

    .neon-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d2ff, transparent);
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. KANDUNGAN ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 50px; color: white;'>PORTAL TOOL PINTAR</h1>", unsafe_allow_html=True)
st.markdown("<div class='neon-line'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.1rem; opacity: 0.8;'>Pusat navigasi eksklusif untuk semua alatan digital anda.</p>", unsafe_allow_html=True)
st.write("")

# --- 4. GRID TOOL ---
col1, col2 = st.columns(2)

with col1:
    # Buka kotak
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.markdown(" <div style='font-size: 50px;'>📊</div>", unsafe_allow_html=True)
    st.markdown(" <h2 style='color: white; margin-top:10px;'>Kalkulator Saham</h2>", unsafe_allow_html=True)
    st.markdown(" <p style='font-size: 0.95rem; opacity: 0.8;'>Analisis profit Bursa Malaysia dengan ketepatan fee broker 2025.</p>", unsafe_allow_html=True)
    # Butang diletakkan di dalam div kotak
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorsaham.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.markdown(" <div style='font-size: 50px;'>💰</div>", unsafe_allow_html=True)
    st.markdown(" <h2 style='color: white; margin-top:10px;'>Compounding</h2>", unsafe_allow_html=True)
    st.markdown(" <p style='font-size: 0.95rem; opacity: 0.8;'>Simulasi pertumbuhan aset anda menggunakan kuasa faedah kompaun.</p>", unsafe_allow_html=True)
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorcompounding.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# Baris 2 (Game Sejarah) - Guna layout yang sama supaya size kotak konsisten
c1, c2, c3 = st.columns([0.1, 0.8, 0.1]) 
with c2:
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.markdown(" <div style='font-size: 50px;'>🎮</div>", unsafe_allow_html=True)
    st.markdown(" <h2 style='color: white; margin-top:10px;'>Kuiz Sejarah</h2>", unsafe_allow_html=True)
    st.markdown(" <p style='font-size: 0.95rem; opacity: 0.8;'>Uji ilmu Sejarah Tahun 5 dalam cabaran 'Nyahaktif Bom'. Jawab betul atau meletup!</p>", unsafe_allow_html=True)
    st.link_button("🚀 Main Sekarang", "https://soalansejarahtahun5.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.85rem; opacity: 0.4;'>© 2026 Portal Pintar v2.6 | Uniform Cinematic Hub</p>", unsafe_allow_html=True)
