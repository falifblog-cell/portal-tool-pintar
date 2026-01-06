import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🚀", layout="centered")

# --- 2. CUSTOM CSS (DESIGN CINEMATIC + CENTER BUTTON) ---
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

    /* GLASSMORPHISM CARD */
    .tool-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 40px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.4s ease;
        margin-bottom: 15px;
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

    /* LOGIK CENTER BUTTON */
    /* Kita sasarkan div yang mengandungi butang Streamlit */
    .stButton {
        display: flex;
        justify-content: center;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: white !important;
        border: none;
        padding: 12px 35px !important; /* Saiz butang lebih seimbang */
        border-radius: 50px !important; /* Butang berbentuk kapsul */
        font-weight: 700;
        width: auto !important; /* Jangan bagi butang penuh lebar kolum */
        min-width: 200px;
        transition: 0.3s all;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
    }

    .stButton > button:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.6);
        border: none;
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
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>📊</div>
            <h2 style='color: white; margin-top:10px;'>Kalkulator Saham</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Analisis profit Bursa Malaysia dengan ketepatan fee broker 2025.</p>
        </div>
    """, unsafe_allow_html=True)
    # Butang automatik align center sebab CSS .stButton { display: flex; justify-content: center; }
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorsaham.streamlit.app/")

with col2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>💰</div>
            <h2 style='color: white; margin-top:10px;'>Compounding</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Simulasi pertumbuhan aset anda menggunakan kuasa faedah kompaun.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorcompounding.streamlit.app/")

st.write("<br>", unsafe_allow_html=True)

# Baris 2 (Game Sejarah)
c1, c2, c3 = st.columns([0.2, 1, 0.2]) # Buat kolum tengah lebih besar
with c2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>🎮</div>
            <h2 style='color: white; margin-top:10px;'>Kuiz Sejarah</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Uji ilmu Sejarah Tahun 5 dalam cabaran 'Nyahaktif Bom'.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Main Sekarang", "https://soalansejarahtahun5.streamlit.app/")

# --- 5. FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.85rem; opacity: 0.4;'>© 2026 Portal Pintar v2.5 | Premium Cinematic Hub</p>", unsafe_allow_html=True)
