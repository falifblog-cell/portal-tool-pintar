import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Portal Tool Pintar", page_icon="🚀", layout="centered")

# --- 2. CUSTOM CSS (UNTUK DESIGN CANTIK) ---
st.markdown("""
    <style>
    /* Sembunyikan header default Streamlit */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Background Gradient untuk keseluruhan page */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }

    /* Design Kad Tool (Glassmorphism) */
    .tool-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }

    .tool-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.15);
    }

    /* Tajuk & Text */
    h1, h2, h3, p {
        color: white !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 50px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(0,210,255,0.4);
        transform: scale(1.05);
        color: white;
    }

    /* Garis pemisah */
    hr {
        border: 0;
        height: 1px;
        background: rgba(255, 255, 255, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. KANDUNGAN UTAMA ---
st.markdown("<h1 style='text-align: center; font-size: 50px;'>🚀 Portal Tool Pintar</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; opacity: 0.8;'>Segala alatan digital anda di hujung jari.</p>", unsafe_allow_html=True)
st.write("---")

# --- 4. GRID TOOL ---

# Baris 1
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="tool-card">
            <h2 style='font-size: 40px;'>📈</h2>
            <h3>Kalkulator Saham</h3>
            <p>Semak untung rugi Bursa Malaysia dengan kiraan Brokerage, Stamp Duty & Clearing Fee tepat.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Buka Tool Saham", "https://kalkulatorsaham.streamlit.app/")

with col2:
    st.markdown("""
        <div class="tool-card">
            <h2 style='font-size: 40px;'>✨</h2>
            <h3>Compounding</h3>
            <p>Rancang masa depan anda dengan simulasi faedah kompaun dinamik (1-5 tahun rekod).</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Buka Tool Compounding", "https://kalkulatorcompounding.streamlit.app/")

st.write("") # Jarak

# Baris 2
col3, _ = st.columns([1, 1])

with col3:
    st.markdown("""
        <div class="tool-card">
            <h2 style='font-size: 40px;'>💣</h2>
            <h3>Kuiz Sejarah</h3>
            <p>Asah minda Sejarah Tahun 5 dengan cabaran bom meletup yang mendebarkan.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Main Game Sejarah", "https://soalansejarahtahun5.streamlit.app/")

# --- 5. FOOTER ---
st.write("---")
st.markdown("<p style='text-align: center; opacity: 0.6;'>© 2026 Portal Pintar. Dicipta untuk kemudahan anda.</p>", unsafe_allow_html=True)
