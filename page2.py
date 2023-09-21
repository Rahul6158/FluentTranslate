import streamlit as st
from gtts import gTTS
import os
import base64
from docx import Document  # Import the Document class from python-docx
from googletrans import Translator

language_mapping = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "hi": "Hindi",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Simplified Chinese",
    "ru": "Russian",
    "ar": "Arabic",
    "th": "Thai",
    "tr": "Turkish",
    "pl": "Polish",
    "cs": "Czech",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "el": "Greek",
    "hu": "Hungarian",
    "uk": "Ukrainian",
    "no": "Norwegian",
    "id": "Indonesian",
    "vi": "Vietnamese",
    "ro": "Romanian",
    "bn": "Bengali",
    "fa": "Persian",
    "iw": "Hebrew",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "hr": "Croatian",
    "sr": "Serbian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "et": "Estonian",
    "is": "Icelandic",
    "ga": "Irish",
    "sq": "Albanian",
    "mk": "Macedonian",
    "hy": "Armenian",
    "ka": "Georgian",
    "mt": "Maltese",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
    "ne": "Nepali",
    "si": "Sinhala",
    "km": "Khmer",
    "lo": "Lao",
    "my": "Burmese",
    "jw": "Javanese",
    "mn": "Mongolian",
    "zu": "Zulu",
    "xh": "Xhosa"
}

# Function to translate text
def translate_text(text, target_language):
    if target_language in language_mapping:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
    else:
        return "Language not found in the mapping"

# Function to convert text to speech and save as an MP3 file
def convert_text_to_speech(text, output_file, language='en'):
    if text:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)
    else:
        st.warning("No text to speak")

# Function to convert text to a DOCX document
def convert_text_to_docx(text, output_file):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)

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

    # Create a button to perform both "Convert to Speech" and "Download DOCX" actions
    if st.button("Translate, Convert to Speech, and Download DOCX"):
        output_file_mp3 = "translated_speech.mp3"
        output_file_docx = "translated_text.docx"

        # Convert the translated text to speech
        convert_text_to_speech(translated_text, output_file_mp3, language=target_language_code)

        # Provide download link for the MP3 file
        st.audio(output_file_mp3, format='audio/mp3', key='audio')

        # Convert the translated text to a DOCX document
        convert_text_to_docx(translated_text, output_file_docx)

        # Provide download link for the DOCX document
        st.markdown(get_binary_file_downloader_html("Download DOCX Document", output_file_docx, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
