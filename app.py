import streamlit as st

# --- 1. SETUP PAGE ---
st.set_page_config(page_title="Pusat Tool Pintar", page_icon="🚀", layout="centered")

# --- CSS UNTUK KEMAS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.title("🚀 Pusat Tool Pintar")
st.write("Klik pada butang di bawah untuk membuka alatan yang anda perlukan di tab baru.")
st.divider()

# --- 3. SUSUNAN TOOL (GRID) ---

# Baris 1: Tool Saham & Compounding
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📈 Saham")
    st.write("Kira untung bersih Bursa Malaysia dengan rate broker terkini.")
    st.link_button("Buka Kalkulator Saham", "https://kalkulatorsaham.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✨ Compounding")
    st.write("Simulasi potensi kekayaan jangka panjang dengan kuasa kompaun.")
    st.link_button("Buka Magic Compounding", "https://kalkulatorcompounding.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("") # Jarak sikit

# Baris 2: Game Sejarah
col3, _ = st.columns([1, 1]) # Guna satu kolum sahaja supaya duduk sebelah kiri atau tengah

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💣 Kuiz Sejarah")
    st.write("Uji ilmu Sejarah Tahun 5 dalam misi nyahaktifkan bom.")
    st.link_button("Main Game Sejarah", "https://soalansejarahtahun5.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. FOOTER ---
st.divider()
st.caption("© 2026 Portal Tool Pintar | Dikuasakan oleh Streamlit")
