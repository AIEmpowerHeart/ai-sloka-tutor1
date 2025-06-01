import streamlit as st
import whisper
import tempfile

st.set_page_config(page_title="🧘 AI Sloka Tutor", layout="centered")
st.title("🧘 AI Sloka Tutor (Voice to Meaning)")
st.write("Upload a Sanskrit sloka audio file (.wav) to hear and get simplified English explanation.")

uploaded_file = st.file_uploader("📤 Upload your sloka audio (WAV only)", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("🔄 Transcribing..."):
        model = whisper.load_model("base")
        result = model.transcribe(tmp_path)

    transcription = result["text"]
    st.subheader("📜 Transcription")
    st.success(transcription)

    st.subheader("🧘 Reflect & Write")
    st.text_area("💬 What did this sloka mean to you?", placeholder="Write your reflection here...")