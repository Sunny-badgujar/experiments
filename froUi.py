import streamlit as st
from transformers import pipeline

st.title("🧠 Text Summarizer")

summarizer = pipeline("summarization")

text = st.text_area("Enter a long paragraph:")

if st.button("Summarize"):
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    st.write("### ✨ Summary:")
    st.write(summary[0]['summary_text'])
