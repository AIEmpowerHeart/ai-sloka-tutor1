
import streamlit as st
from fpdf import FPDF

def export_text(transcription, sloka):
    st.download_button("⬇️ Download Transcription (.txt)", data=transcription, file_name="transcription.txt")

def export_pdf(transcription, sloka):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Sloka: {sloka['sanskrit']}

Transcription:
{transcription}")
    path = "/tmp/transcription.pdf"
    pdf.output(path)
    with open(path, "rb") as f:
        st.download_button("⬇️ Download Transcription (.pdf)", data=f, file_name="transcription.pdf")
