import streamlit as st
from translate import Translator
from gtts import gTTS
import os
import base64

language_mapping = {
    "en": "English",
    "gu": "Gujarati",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "mr": "Marathi",
    "bn": "Bengali",
}

# Function to translate text using the "translate" library
def translate_text(text, target_language):
    if target_language in language_mapping:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
    else:
        return "Language not found in the mapping"

# Rest of your code remains the same

def main():
    st.image("jangirii.png", width=50)
    st.title("Text Translation and Conversion to speech (English - other languages)")
    
    # Get user input
    text = st.text_area("Enter text to translate and convert to speech:")
    target_language = st.selectbox("Select target language:", list(language_mapping.values()))

    # Check if the target language is in the mapping
    target_language_code = [code for code, lang in language_mapping.items() if lang == target_language][0]

    # Translate the input text
    translated_text = translate_text(text, target_language_code)

    # Display translated text
    if translated_text:
        st.subheader(f"Translated text ({target_language}):")
        st.write(translated_text)
    else:
        st.warning("Translation result is empty. Please check your input text.")

    # Rest of your code remains the same

if __name__ == "__main__":
    main()
