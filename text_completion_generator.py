import os
import streamlit as st
from transformers import pipeline

# Optional: Hide unnecessary warnings
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

# Set page configuration
st.set_page_config(page_title="Text Completion Generator", layout="centered")

# Load GPT-2 model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

text_generator = load_model()

# App title
st.title("📝 Text Completion Generator")

# Instruction
st.markdown("Enter the beginning of a sentence below and let AI complete it.")

# User input
input_text = st.text_input("✍️ Start your sentence below:")

# Generate text button
if st.button("🔍 Generate Completion"):
    if input_text.strip():
        with st.spinner("Generating text..."):
            result = text_generator(
                input_text,
                max_length=100,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7,
            )
            generated_text = result[0]["generated_text"]
        # Output
        st.markdown("### ✅ Completed Sentence:")
        st.write(generated_text)
    else:
        st.warning("Please enter a valid sentence.")
