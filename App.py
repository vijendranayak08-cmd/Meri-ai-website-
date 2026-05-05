import streamlit as st

st.set_page_config(page_title="Personal AI Tools", layout="wide")

st.title("🤖 Meri Personal AI Website")
st.write("Mobile se bani hui personal AI website.")

tab1, tab2, tab3, tab4 = st.tabs(["Text to Image", "Text to Video", "Image to Video", "Auto-Caption"])

with tab1:
    st.subheader("🖼️ Text to Image Generator")
    prompt_img = st.text_input("Prompt likhein:", key="img_prompt")
    if st.button("Generate Image"):
        if prompt_img:
            st.info("AI model load ho raha hai...")
            st.image("https://via.placeholder.com/512?text=Image+Generated", caption="Generated Image")
        else:
            st.warning("Kripya text likhein.")

with tab2:
    st.subheader("🎥 Text to Video")
    prompt_vid = st.text_input("Video prompt:", key="vid_prompt")
    if st.button("Generate Video"):
        if prompt_vid:
            st.info("Video processing shuru...")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with tab3:
    st.subheader("✨ Image to Video")
    uploaded_image = st.file_uploader("Ek image upload karein", type=["jpg", "png"], key="img_to_vid")
    if uploaded_image is not None:
        st.success("Image mil gayi!")

with tab4:
    st.subheader("📝 Auto Caption")
    uploaded_audio = st.file_uploader("Audio/Video file upload karein", type=["mp3", "wav", "mp4"], key="audio")
    if uploaded_audio is not None:
        st.success("Audio transcribe ho raha hai...")

