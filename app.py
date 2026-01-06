import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🚀", layout="centered")

# --- 2. CUSTOM CSS (DESIGN CINEMATIC) ---
st.markdown("""
    <style>
    /* Sembunyikan header/footer asal */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* BACKGROUND CINEMATIC */
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
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
        margin-bottom: 10px;
    }

    .tool-card:hover {
        transform: translateY(-12px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(0, 210, 255, 0.5);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    /* TYPOGRAPHY */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }

    p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #e0e0e0 !important;
    }

    /* BUTTON STYLING */
    .stButton > button {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100%;
        transition: 0.3s all;
        box-shadow: 0 4px 15px rgba(58, 123, 213, 0.3);
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.5);
        color: white;
    }

    /* Garis pemisah neon */
    .neon-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00d2ff, transparent);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. KANDUNGAN ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 55px; color: white;'>PORTAL TOOL PINTAR</h1>", unsafe_allow_html=True)
st.markdown("<div class='neon-line'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Navigasi pantas ke semua alatan digital premium anda.</p>", unsafe_allow_html=True)
st.write("")

# --- 4. GRID TOOL ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>📊</div>
            <h2 style='color: white;'>Kalkulator Saham</h2>
            <p>Analisis untung rugi Bursa Malaysia dengan kiraan fee broker 2025 yang tepat.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorsaham.streamlit.app/")

with col2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>💰</div>
            <h2 style='color: white;'>Compounding</h2>
            <p>Simulasi pelaburan masa depan anda menggunakan kuasa faedah kompaun dinamik.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Lancarkan Tool", "https://kalkulatorcompounding.streamlit.app/")

st.write("")

# Baris 2
c1, c2, c3 = st.columns([0.5, 1, 0.5])
with c2:
    st.markdown("""
        <div class="tool-card">
            <div style='font-size: 50px;'>🎮</div>
            <h2 style='color: white;'>Kuiz Sejarah</h2>
            <p>Cabaran interaktif Sejarah Tahun 5. Jawab dengan betul atau bom meletup!</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Main Sekarang", "https://soalansejarahtahun5.streamlit.app/")

# --- 5. FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.9rem; opacity: 0.5;'>© 2026 Portal Pintar v2.0 | Built with Cinematic UI</p>", unsafe_allow_html=True)
