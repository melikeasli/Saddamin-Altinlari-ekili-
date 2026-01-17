import streamlit as st
import random

random.seed(42)

def cekilis_yap(isim_listesi):
    cekilenler = isim_listesi.copy()
    
    basarili = False
    deneme_sayisi = 0
    max_deneme = 1000 # Sonsuz döngüyü engellemek için
    
    while not basarili and deneme_sayisi < max_deneme:
        random.shuffle(cekilenler)
        basarili = True
        for i in range(len(isim_listesi)):
            if isim_listesi[i] == cekilenler[i]:
                basarili = False
                break
        deneme_sayisi += 1

    if not basarili:
        st.error("Çekiliş yapılamadı. Lütfen tekrar deneyin veya isim listesini kontrol edin.")
        return []

    sonuclar = []
    for i in range(len(isim_listesi)):
        sonuclar.append(f"{isim_listesi[i]} -> {cekilenler[i]} kişisine hediye alacak!")
    return sonuclar

# --- Streamlit Arayüzü ---
st.set_page_config(page_title="🎁 SADDAMIN ALTINLARI ÇEKİLİŞ 🎁", page_icon="🎉", layout="centered")

# Başlık ve Açıklama
st.markdown("""
<style>
.main {
    background-color: #f0f2f6;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" opacity="0.1"><circle cx="10" cy="10" r="3" fill="%23ccc"/><circle cx="50" cy="50" r="3" fill="%23ccc"/><circle cx="90" cy="90" r="3" fill="%23ccc"/></svg>');
    background-size: 50px 50px;
}
.stApp {
    background-color: #f0f2f6;
}
.stButton>button {
    background-color: #e63946;
    color: white;
    border-radius: 20px;
    padding: 0.8em 2em;
    font-size: 1.2em;
    font-weight: bold;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.2s ease-in-out;
}
.stButton>button:hover {
    background-color: #c93643;
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}
.stButton>button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.stAlert {
    border-radius: 10px;
}
.stMarkdown h1 {
    text-align: center;
    color: #e63946;
    font-family: 'Georgia', serif;
    font-size: 3em;
    margin-bottom: 0.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}
.stMarkdown p {
    text-align: center;
    font-size: 1.1em;
    color: #333;
    margin-bottom: 2em;
}
.result-card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
}
.result-card img {
    margin-right: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎁 SADDAMIN ALTINLARI ÇEKİLİŞ 🎁")
st.write("Kim kime hediye alacak çekmek için butona basın!")

# İsim Listesi
isimler = ["Fatma", "Zehra", "Melike", "Rana", "Hale", "Nurefşan", "Nursima"]

# Çekiliş Butonu
if st.button("Çekiliş Yap!"):
    with st.spinner("Çekiliyor... Lütfen bekleyin 🎉"):
        st.balloons() # Balon efekti
        sonuclar = cekilis_yap(isimler)
        if sonuclar:
            st.subheader("🎉 Sonuçlar 🎉")
            for sonuc in sonuclar:
                st.markdown(f"""
                <div class="result-card">
                    <img src="https://em-content.zobj.net/source/apple/354/wrapped-gift_1f381.png" width="30">
                    <span>{sonuc}</span>
                </div>
                """, unsafe_allow_html=True)
            st.success(" Ftm'miz inşallah hemen iyileşirsin ve o projenin anasını ağlatırsın amin🙏 Hepinizi aynı anda çok seviyorum 💕 Güzel şeyler alın 😊")
        else:
            st.error("Çekiliş yapılırken bir hata oluştu. Lütfen tekrar deneyin.")

st.write("---")
st.info("Bu uygulama Fatma, Nurefşan, Nursima, Hale, Rana, Zehra ve Melike için ÖZEL olarak hazırlandı😁!")
