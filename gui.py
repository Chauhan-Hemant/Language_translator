import tkinter as tk
from tkinter import *

from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

# Language dictionary (code → full name)
language_dictionary = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'bg': 'Bulgarian',
    'bn': 'Bengali', 'ca': 'Catalan', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'cs': 'Czech', 'da': 'Danish',
    'nl': 'Dutch', 'en': 'English', 'et': 'Estonian', 'fi': 'Finnish',
    'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati',
    'he': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'id': 'Indonesian',
    'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada', 'ko': 'Korean',
    'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali', 'no': 'Norwegian',
    'pa': 'Punjabi', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
    'ru': 'Russian', 'es': 'Spanish', 'sv': 'Swedish', 'ta': 'Tamil',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'vi': 'Vietnamese'
}

# Reverse dictionary (Language name → code)
name_to_code = {value: key for key, value in language_dictionary.items()}

def detect_language():
    try:
        input_text = text.get("1.0", END).strip()
        if not input_text:
            result_label.config(text="Please enter some text.")
            return
        detected_code = detect(input_text)   # ✅ pass the string
        language_name = language_dictionary.get(detected_code, detected_code)
        result_label.config(
            text=f"Detected Language: {language_name} ({detected_code})"
        )
    except LangDetectException:
        result_label.config(text="Could not detect language. Enter more text.")

def translate_text():
    try:
        input_text = text.get("1.0", END).strip()
        if not input_text:
            result_label.config(text="Please enter text.")
            return
        selected_language_name = selected_language.get()
        if selected_language_name == "Select Language":
            result_label.config(text="Please select a target language.")
            return
        target_code = name_to_code[selected_language_name]
        translated = GoogleTranslator(source='auto', target=target_code).translate(input_text)
        result_label.config(text=f"Translated Text:\n\n{translated}")
    except Exception as e:
        result_label.config(text=f"Translation Error:\n{e}")


def clear_text():
    text.delete("1.0", END)
    result_label.config(text="")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Language Translator")
root.geometry("700x600")
root.resizable(False, False)

Label(root, text="Enter Text to Translate",
      font=("Arial", 16), fg="green").pack(pady=10)

text = Text(root, height=10, width=70)
text.pack(pady=10)

Button(root, text="Detect Language",
       fg="blue", command=detect_language).pack(pady=5)

Label(root, text="Select Target Language").pack()

selected_language = StringVar()
selected_language.set("Select Language")

"""Dropdown with all existing language with there code"""
OptionMenu(root, selected_language, *language_dictionary.values()).pack(pady=5)

Button(root, text="Translate",
       fg="green", command=translate_text).pack(pady=5)

Button(root, text="Clear",
       fg="red", command=clear_text).pack(pady=5)

result_label = Label(root, text="", wraplength=650, justify="left")
result_label.pack(pady=20)

root.mainloop()
