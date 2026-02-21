import streamlit as st

st.title("Otomatik Yazı Puanlama Demo")

metin = st.text_area("Öğrenci cevabını gir:")

if st.button("Puanla"):
    uzunluk = len(metin.split())

    if uzunluk < 5:
        puan = 0
        geri = "Çok kısa cevap."
    elif uzunluk < 15:
        puan = 1
        geri = "Kısa ama anlaşılır."
    else:
        puan = 2
        geri = "Yeterince detaylı."

    st.success(f"Puan: {puan}")
    st.info(f"Geri bildirim: {geri}")
