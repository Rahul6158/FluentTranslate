import streamlit as st
from googletrans import Translator as GoogleTranslator
from gtts import gTTS
import os
import base64

# Define the language mapping
language_mapping = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    # Add more languages as needed
}

# Function to translate text using Google Translate with error handling
def translate_text_with_fallback(text, target_language):
    try:
        if target_language in language_mapping:
            translator = GoogleTranslator()
            translation = translator.translate(text, dest=target_language).text
            return translation
        else:
            return "Language not found in the mapping"
    except Exception as e:
        return f"Translation error: {str(e)}"

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
    translated_text = translate_text_with_fallback(text, target_language_code)

    # Display translated text
    if translated_text:
        st.subheader(f"Translated text ({target_language}):")
        st.write(translated_text)
    else:
        st.warning("Translation result is empty. Please check your input text.")

    # Rest of your code remains the same

if __name__ == "__main__":
    main()
