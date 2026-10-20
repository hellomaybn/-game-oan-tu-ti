import streamlit as st
import random

if "diem_nguoi" not in st.session_state:
    st.session_state.diem_nguoi = 0
    st.session_state.diem_may = 0

st.title("✊✋✌ Trò chơi Oẳn tù tì")
lua_chon = ["Đá", "Giấy", "Kéo"]
chon_nguoi = st.selectbox("Bạn chọn gì?", lua_chon)

if st.button("Chơi!"):
    chon_may = random.choice(lua_chon)
    st.write(f"Máy chọn: {chon_may}")
    if chon_nguoi == chon_may:
        st.info("⚖️ Hòa!")
    elif (chon_nguoi == "Đá" and chon_may == "Kéo") or \
         (chon_nguoi == "Giấy" and chon_may == "Đá") or \
         (chon_nguoi == "Kéo" and chon_may == "Giấy"):
        st.success("🎉 Bạn thắng!")
        st.session_state.diem_nguoi += 1
    else:
        st.error("😞 Bạn thua!")
        st.session_state.diem_may += 1

st.subheader("📊 Bảng điểm")
st.write(f"Bạn: {st.session_state.diem_nguoi} — Máy: {st.session_state.diem_may}")
