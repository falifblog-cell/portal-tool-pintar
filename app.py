import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🚀", layout="centered")

# --- 2. CUSTOM CSS (TRIMMED TOP SPACE) ---
st.markdown("""
    <style>
    /* Sembunyikan header/footer asal */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* KURANGKAN RUANG ATAS SEKALI */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }

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
        padding: 30px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.4s ease;
        min-height: 380px; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
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
        margin-top: 0px !important; /* Paksa margin h1 jadi 0 */
    }

    .custom-btn {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: white !important;
        text-decoration: none;
        padding: 12px 35px;
        border-radius: 50px;
        font-weight: 700;
        display: inline-block;
        transition: 0.3s all;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
    }

    .custom-btn:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.6);
        color: white !important;
    }

    .neon-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d2ff, transparent);
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. KANDUNGAN (TAG <br> DIBUANG) ---
# Saya dah buang st.markdown("<br><br>") supaya tajuk terus naik ke atas
st.markdown("<h1 style='text-align: center; font-size: 50px; color: white;'>PORTAL TOOL PINTAR</h1>", unsafe_allow_html=True)
st.markdown("<div class='neon-line'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.1rem; opacity: 0.8;'>Navigasi eksklusif untuk alatan digital anda.</p>", unsafe_allow_html=True)
st.write("")

# --- 4. GRID TOOL ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>📊</div>
            <h2 style='color: white; margin-top:10px;'>Kalkulator Saham</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Analisis profit Bursa Malaysia dengan ketepatan fee broker 2025.</p>
            <a href="https://kalkulatorsaham.streamlit.app/" target="_blank" class="custom-btn">🚀 Lancarkan Tool</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>💰</div>
            <h2 style='color: white; margin-top:10px;'>Compounding</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Simulasi pertumbuhan aset anda menggunakan kuasa faedah kompaun.</p>
            <a href="https://kalkulatorcompounding.streamlit.app/" target="_blank" class="custom-btn">🚀 Lancarkan Tool</a>
        </div>
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.1, 0.8, 0.1]) 
with c2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>🎮</div>
            <h2 style='color: white; margin-top:10px;'>Kuiz Sejarah</h2>
            <p style='font-size: 0.95rem; opacity: 0.8;'>Uji ilmu Sejarah Tahun 5 dalam cabaran 'Nyahaktif Bom'. Jawab betul atau meletup!</p>
            <a href="https://soalansejarahtahun5.streamlit.app/" target="_blank" class="custom-btn">🚀 Main Sekarang</a>
        </div>
    """, unsafe_allow_html=True)

# --- 5. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.85rem; opacity: 0.4;'>© 2026 Portal Pintar v2.7 | Uniform Cinematic Hub</p>", unsafe_allow_html=True)
